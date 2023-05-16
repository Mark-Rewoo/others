import os
import rasterio
import numpy as np
from rasterio.enums import Resampling
from pyproj import Transformer


input_folder = "/Users/renzhonghe/Desktop/jp2_4bands"
output_folder = "/Users/renzhonghe/Desktop/Geotiff_3bands"

# Get a list of JP2 files in the input folder
jp2_files = [file for file in os.listdir(input_folder) if file.endswith(".jp2")]


# Define the output projection as EPSG:3857
output_crs = "EPSG:3857"

print("Conversion started...")


# Iterate over the JP2 files
for jp2_file in jp2_files:
    jp2_path = os.path.join(input_folder, jp2_file)
    output_file = os.path.splitext(jp2_file)[0] + ".tif"
    output_path = os.path.join(output_folder, output_file)


    os.system("gdalwarp -overwrite -t_srs " + output_crs + " -dstalpha -r near -co tiled=yes -co compress=deflate -of GTiff \"" + jp2_path + "\" \"" + output_file + "\"")

    print(f"Converted {jp2_file} to {output_file}")



print("Conversion completed.")