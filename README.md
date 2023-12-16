# Geospatial-Analysis
Analyse the different geolocations


### Geospatial mapping using Google Earth and KML
* [Placemarks-Nearest-Neighbors.kml](Placemarks-Nearest-Neighbors.kml): Placed 12 coords (and home coordinates) in four KML 'folders' - 'libraries', 'eateries', 'waterworks' and 'department buildings'.
* Install Google Earth and visualize the data from the KML file
  * Simply copy and paste your KML data into the textbox on the left
  * Click 'Show it on the map' to have it be displayed

<p align="center"><img src="images/spatial_visualization.png" width="500"></p>

### Geospatial Queries using POSTGIS
1. Compute Convex Hull
   * [Spatial_queries.sql](spatial_queries.sql): Compute the convex hull for the 13 points (a convex hull for a set of 2D points is the smallest convex polygon that contains the point set). 
   * Use the query results to create a polygon in the .kml file 
   * Load this into Google Earth and visually verify that all your points are on/inside the convex hull

2. Compute Nearest Neighbors
   * [Spatial_queries.sql](spatial_queries.sql): Compute the four nearest neighbors from home location
   * Use the query's results to create four line segments in your .kml file
   * Load this into Google Earth and visually verify if it looks correct

<p align="center"><img src="images/spatial_queries.png" width="500"></p>


### Spirograph