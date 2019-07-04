import os
import shutil
import glob

src_folder = r'c:/pyqgis/CURSO_PYQGIS/CAPAS'
if os.path.isdir(src_folder):
    print("folder ok")

shp_lista = glob.glob(src_folder + '/*.shp')
print(shp_lista)
for shapefile in shp_lista:
    layer = QgsVectorLayer(shapefile,os.path.splitext(os.path.basename(shapefile))[0],'ogr')
    QgsProject.instance().addMapLayer(layer)

###funciona correctamente

