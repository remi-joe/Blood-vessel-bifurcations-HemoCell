#----------- Written By ------------
#------------ Wei Wei ------------
#---- PhD Scholar @ Oxford University -------

import FreeCAD as App
import Mesh
import os
from numpy import sin, cos, tan, pi
from sys import argv
# Store working directory
wdir = os.getcwd()
# Open the geometry file
App.openDocument(os.path.join(wdir,'single_bifurcation.FCStd'))
#
# Geometry:
#           S005
#            /\
#           /  \
#        S003  S007
#         /      \
#S------S001    S006--------
#         \      /
#        S002  S008
#           \  /
#            \/
#           S004
# S is for Sketch
#
# Read D1 and D2 
D1 = float(argv[2])
D2 = float(argv[3])
D1_mm = str(D1) + ' mm'
D2_mm = str(D2) + ' mm'
# Change the diameter of the 1st branch
App.ActiveDocument.Sketch003.setDatum(0, App.Units.Quantity(D1_mm))
App.ActiveDocument.Sketch005.setDatum(0, App.Units.Quantity(D1_mm))
App.ActiveDocument.Sketch007.setDatum(0, App.Units.Quantity(D1_mm))
# Change the diameter of the 2ns branch
App.ActiveDocument.Sketch002.setDatum(0, App.Units.Quantity(D2_mm))
App.ActiveDocument.Sketch004.setDatum(0, App.Units.Quantity(D2_mm))
App.ActiveDocument.Sketch008.setDatum(0, App.Units.Quantity(D2_mm))
# Set the length of each branch in x-direction
D_max = max(D1, D2)
S23_z = 0.5 / tan(pi / 12)
S45_x = (0.5 / sin(pi / 12) + 5 * D_max * cos(pi / 12)) * sin(pi / 12)
S45_z = (0.5 / sin(pi / 12) + 5 * D_max * cos(pi / 12)) * cos(pi / 12)
S6_z = 2 * S45_z
S78_z = S6_z - S23_z
App.ActiveDocument.Sketch002.AttachmentOffset = App.Placement\
    (App.Vector(- 0.5, 0, S23_z),\
     App.Rotation(0, 0, 0))
App.ActiveDocument.Sketch003.AttachmentOffset = App.Placement\
    (App.Vector(0.5, 0, S23_z),\
     App.Rotation(0, 0, 0))
App.ActiveDocument.Sketch004.AttachmentOffset = App.Placement\
    (App.Vector(- S45_x, 0, S45_z),\
     App.Rotation(0, 0, 0))
App.ActiveDocument.Sketch005.AttachmentOffset = App.Placement\
    (App.Vector(S45_x, 0, S45_z),\
     App.Rotation(0, 0, 0))
App.ActiveDocument.Sketch006.AttachmentOffset = App.Placement\
    (App.Vector(0, 0, S6_z),\
     App.Rotation(0, 0, 0))
App.ActiveDocument.Sketch007.AttachmentOffset = App.Placement\
    (App.Vector(0.5, 0, S78_z),\
     App.Rotation(0, 0, 0))
App.ActiveDocument.Sketch008.AttachmentOffset = App.Placement\
    (App.Vector(-0.5, 0, S78_z),\
     App.Rotation(0, 0, 0))
# Recompute the geometry
App.ActiveDocument.recompute()
# Shift the whole geometry to satisfy y<0 and that the geometry is symmetric 
# with the y-z plane
#App.ActiveDocument.Body.Placement = App.Placement\
#    (App.Vector(- 5 - S45_z, - D1 / 2 - S45_x, 0),\
#     App.Rotation(0, 0, 0), App.Vector(0, 0, 0))
#
# Output the total length in y-coordinate
#open('mesh_' + str(D1) + '_' + str(round(D2,2)) + '.dat', 'w+').\
#    write(str(S45_x * 2 + D1 / 2 + D2 / 2))
#
# Generate the mesh
#__objs__=[]
#__objs__.append(App.getDocument("single_bifurcation").getObject("Body"))
#Mesh.export(__objs__,os.path.join(wdir,'mesh_'+str(D1)+'_'+str(round(D2,2))+'.stl'))

#exit()
#del __objs__
#
#exit()
