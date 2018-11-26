import geopandas as gpd
import os

# Read file
df = gpd.read_file("C:\Suzanne_R\Data\DAMSELFISH_distributions.shp")

# Group the data by column 'BINOMIAL'
grouped = df.groupby('BINOMIAL')

print grouped

# Iterate over the grouped object (similar to dictionary with keys and values)
for key, values in grouped:
    individual_fish = values

    print individual_fish
    print type(individual_fish)
    print key

#Determine output folder
out = r"C:/Suzanne_R/Data"

# Create a new folder called 'Results' (if does not exist) to that folder using os.makedirs() function
resultFolder = os.path.join(out, 'Results')
if not os.path.exists(resultFolder):
    os.makedirs(resultFolder)

# Iterate over the
for key, values in grouped:
    # Format the filename (replace spaces with underscores)
    outName = "%s.shp" % key.replace(" ", "_")

    # Print some information for the user
    print("Processing: %s" % key)

    # Create an output path
    outpath = os.path.join(resultFolder, outName)

    # Export the data
    values.to_file(outpath)
