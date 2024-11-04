module load cmake
module load cray-hdf5
module load cray-mpich
module load cray-python

export CC=cc
export CXX=CC
export LDFLAGS="-L${CRAYLIBS_X86_64} $(CC --cray-print-opts=libs) -lmpi"

first="/work/e745/e745/remi23/HemoCell/examples/"

name_generated=0
selected="0"
for j in $selected
    do
    for i in $(seq 0 4)
        do
        name[$name_generated]="D31.5_"$j"_"$i
        name_generated=$(($name_generated+1))
        done
    done
selected="0"
for j in $selected
    do
    for i in $(seq 0 4)
        do
        name[$name_generated]="D40.0_"$j"_"$i
        name_generated=$(($name_generated+1))
        done
    done

third="/output_0/checkpoint/checkpoint.xml"

for i in $(seq 0 9)
    do
    cd $first${name[i]} && python revise_timestep.py
    done
