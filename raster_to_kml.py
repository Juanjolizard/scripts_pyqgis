import processing
import os
import glob

src_folder = 'C:/rasters'
dst_folder = 'C:/output_kml'

if not os.path.exists(dst_folder):
    os.mkdir(dst_folder)

rasters = glob.glob(src_folder + '/*.asc')
#print (rasters)

for raster in rasters:
    try:
        dst_name = os.path.splitext(os.path.basename(raster))[0]
        parameters = {
        'BAND' : 1, 
        'EIGHT_CONNECTEDNESS' : True, 
        'EXTRA' : '',
        'FIELD' : 'VALUE',
        'INPUT' : raster,
        'OUTPUT' : os.path.join(dst_folder,f'{dst_name}_kml.kml')}
        feedback = QgsProcessingFeedback()
        processing.runAndLoadResults('gdal:polygonize',parameters,feedback=feedback)
    except:
        print("processing error")