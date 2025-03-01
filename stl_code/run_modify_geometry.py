#----------- Written By ------------
#------------ Wei Wei ------------
#---- PhD Scholar @ Oxford University -------

import os

freecad_path = '/usr/lib/freecad/bin/freecad-python3'

D1 = 0.93
D2 = ((1)-((0.93)**3))**(1/3)

os.system(freecad_path + ' modify_geometry.py ' + str(D1) + ' ' + str(D2))

#exit()
