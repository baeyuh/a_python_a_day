import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, Polygon
import fiona

# Read file
df = gpd.read_file("C:\Suzanne_R\Data\DAMSELFISH_distributions.shp")

print type(df)

print df.head()

print df.plot()

out = r"C:\Suzanne_R\Data\new.shp"
selection = df[0:10]

# Write to file
selection.to_file(out)

# Print first 5 geometries
print df['geometry'].head()

# Iterate over the selected rows
for index, row in selection.iterrows():
    poly_area = row.geometry.area  #get area
    print("Polygon at index {0} is: {1: .3f}".format(index, poly_area))

# Create new column and calculate and store area
df['area'] = df.area

print df['area'].head(2)

# Maximum area
max_area = df['area'].max()

# Mean area
mean_area = df['area'].mean()

print("Max area: %s\nMean area: %s" % (round(max_area, 2), round(mean_area, 2)))

# Create empty geopandas GeoDataFrame
newdata = gpd.GeoDataFrame()

print newdata

# Create a new column called 'geometry' to the GeoDataFrame
newdata['geometry'] = None

print newdata

# Coordinates of the Helsinki Senate square in Decimal Degrees
coordinates = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]

# Create shapely polygon from coordinate-tuple list
poly = Polygon(coordinates)

print poly

# Insert the polygon into 'geometry' -column at index 0
newdata.loc[0, 'geometry'] = poly

print newdata

# Add a new column and insert data
newdata.loc[0, 'Location'] = 'Senaatintori'

print newdata

print(newdata.crs) #check projection

# Import specific function 'from_epsg' from fiona module
from fiona.crs import from_epsg

# Set the GeoDataFrame's coordinate system to WGS84
newdata.crs = from_epsg(4326)

print newdata.crs

# Determine the output path for the Shapefile
outfp = r"C:\Suzanne_R\Data\new_2.shp"

# Write the data into that Shapefile
newdata.to_file(outfp)
