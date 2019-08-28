from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import * 
import processing
import os
import shutil
import glob


src_folder = 'C:/input'
dst_folder = 'C:/output'

if not os.path.exists(dst_folder):
    os.mkdir(dst_folder)

capas = glob.glob(src_folder + '/*.shp')
print(capas)

for capa in capas:
    dst_name = os.path.splitext(os.path.basename(capa))[0] ###toma el primer argumento espliteado
    layer = QgsVectorLayer(capa,'puntos','ogr')
    if layer.wkbType() == QgsWkbTypes.Point:
        try:
            parameters = {'INPUT':capa,
            'OUTPUT':os.path.join(dst_folder,f'{dst_name}_withcoordinatesadded.shp')}
            feedback = QgsProcessingFeedback()
            processing.runAndLoadResults('saga:addcoordinatestopoints',parameters,feedback=feedback)
            print("points/coordinates correctly added")
        except:
             print("processing error")
    else:
        print(os.path.basename(capa) + ' ' +  "have not points available")