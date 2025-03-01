import os
#
dt=int(open('dt.txt','r').read())
tmax_old=int(open('timestep.txt','r').read())
tmax=tmax_old+dt
def revise_checkpoint(tmax_new):
    os.system("cp output_0/checkpoint/checkpoint.xml .")
    check_point=open('checkpoint.xml','r').read()
    tmax_position=check_point.find("tma")
    check_point_list=list(check_point)
    tmax_new_string=str(tmax_new)
    tmax_new_length=len(tmax_new_string)
    for i in range(0,tmax_new_length):
        check_point_list[tmax_position+6+i]=tmax_new_string[i]
    #
    open('checkpoint.xml','w').write(''.join(check_point_list))
#
revise_checkpoint(tmax)
os._exit(0)
