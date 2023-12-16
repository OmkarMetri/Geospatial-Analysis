import math

# Spiro parameters
R = 36
r = 9
a = 30

# Calculate x and y co-ordinates
x0 = R + r - a
y0 = 0

# Tommy Trojan (long, lat)
tommy = (-118.28517813897285, 34.02025806530462)

nRev = 32
t = 0.0

coords = []
while t < (math.pi * nRev):
    # Use the equations specified in the quiz
    x = (R+r) * math.cos((r/R) * t) - a * math.cos((1+r/R) * t)
    y = (R+r) * math.sin((r/R) * t) - a * math.sin((1+r/R) * t)

    # Reduce the x and y coordinates by 0.0001 and add to tommy's coordinates
    x = tommy[0]+(x * 0.0001)
    y = tommy[1]+(y * 0.0001)
    coords.append(f"{x},{y}")

    t += 0.01

coords = "\n                ".join(coords)

KML = f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
    <Document>
        <Style id="blueLine">
            <LineStyle>
                <color>ffff0000</color>
                <width>3</width>
            </LineStyle>
        </Style>
    <Placemark>
        <name>Spirograph Curve</name>
        <styleUrl>#blueLine</styleUrl>
        <LineString>
            <coordinates>
                {coords}
            </coordinates>
        </LineString>
    </Placemark>
  </Document>
</kml>

"""

with open("spiro.kml", "w") as fp:
    fp.write(KML)
