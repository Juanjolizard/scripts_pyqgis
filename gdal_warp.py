import processing
import os
import glob

src_folder = 'C:/capas_nocrs'
dst_folder = 'C:/prueba_python'

rasters = glob.glob(src_folder + '/*.asc')
#print (rasters)

for raster in rasters:
    print(raster)
    dst_name = os.path.splitext(os.path.basename(raster))[0]
    parameters = {'DATA_TYPE' : 0,
    'EXTRA' : '', 
    'INPUT' : raster, 
    'MULTITHREADING' : False,
    'NODATA' : -9999, 
    'OPTIONS' : 'COMPRESS=LZW', 
    'OUTPUT' : os.path.join(dst_folder,f'{dst_name}.asc'),
    'RESAMPLING' : 1, 
    'SOURCE_CRS' : None, 
    'TARGET_CRS' : 'EPSG:32628',
    'TARGET_EXTENT' : None, 
    'TARGET_EXTENT_CRS' : None, 
    'TARGET_RESOLUTION' : None}
    feedback = QgsProcessingFeedback()
    processing.runAndLoadResults('gdal:warpreproject',parameters,feedback=feedback)
    print("Se ha reproyectado la capa" + ' ' + f'{dst_name}.asc')