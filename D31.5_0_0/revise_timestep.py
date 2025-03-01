dt=int(open('dt.txt','r').read())
timestep=int(open('timestep.txt','r').read())
timestep=timestep+dt
open('timestep.txt','w').write(str(timestep))
