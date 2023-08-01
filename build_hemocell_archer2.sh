#!/bin/bash
if [[ "$0" == "$BASH_SOURCE" ]]; then
 echo "Script is a subshell, this wont work, source it instead!"
 exit 1
fi

module load cray-hdf5
module load cray-mpich
module load cray-python
module list

export CC=cc
export CXX=CC
export LDFLAGS="-L${CRAYLIBS_X86_64} $(CC --cray-print-opts=libs) -lmpi"
export MAIN= install_directory_path

# To download HemoCell, comment this out if you have already done it
git clone https://github.com/UvaCsl/HemoCell.git
export HEMOCELL=$MAIN/HemoCell
export DEPEND=$HEMOCELL/external

# To install the palabos dependencies
cd $HEMOCELL && ./setup.sh

# To install other dependencies like ParMETIS and METIS
# Both require GKlib which we first need to downlaod
cd $DEPEND
git clone https://github.com/KarypisLab/GKlib.git # For GKlib
git clone https://github.com/KarypisLab/METIS.git # For METIS
git clone https://github.com/KarypisLab/ParMETIS.git # For ParMETIS

# First lets build GKlib
cd ./GKlib
make config prefix=$DEPEND/GKlib # assumming that you ane using the GNU environment and gcc ( you can change this with additional arguments - see GitHub) (the prefix= stores all the files in the specified location, the default location is ~/usr/local)
make
make install

# Building METIS
cd $DEPEND/METIS
make config prefix=$DEPEND/METIS gklib_path=$DEPEND/GKlib
make install

# Building ParMETIS
cd $DEPEND/ParMETIS
make config prefix=$DEPEND/ParMETIS gklib_path=$DEPEND/GKlib metis_path=$DEPEND/METIS
make install
cd $HEMOCELL

# Before building HemoCell we need to associate the paths in CMake (find_parmetis.cmake) so that HemoCell finds ParMETIS and METIS
# The lines 21, 29, 37, 45 of the file need to be updated with the path of ParMETIS and METIS and the following code achieves that
file="$HEMOCELL/cmake/find_parmetis.cmake"
tempfile="$HEMOCELL/cmake/find_parmetis_temp.cmake"

# Define the lines and their new contents
declare -A lines_to_change
lines_to_change[21]="                HINTS external/ParMETIS/include"
lines_to_change[29]="                HINTS external/ParMETIS/lib"
lines_to_change[37]="                HINTS external/METIS/include"
lines_to_change[45]="                HINTS external/METIS/lib"

# Read the contents of the file and modify the specific lines
count=1
while IFS= read -r line; do
    if [ "${lines_to_change[$count]+_}" ]; then
        echo "${lines_to_change[$count]}"
    else
        echo "$line"
    fi
    count=$((count + 1))
done < "$file" > "$tempfile"

# Replace the original file with the modified temporary file
mv "$tempfile" "$file"

echo "The specified lines in $file have been changed."

# Building HemoCell
cd $HEMOCELL
mkdir build && cd build/
cmake ..
cmake --build .                                                                         
