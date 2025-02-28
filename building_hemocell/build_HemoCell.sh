#---------------- Written by ------------
#------------- Remigius J Selvaraj ----------
#--------- Computational Fluid Dynamics ----------
#------------- Cranfield University ---------
#!/bin/bash

# We install the dependencies that are necessary

sudo apt-get install -y make
sudo apt-get install -y cmake
sudo apt-get install -y g++
sudo apt-get install -y g++-12
sudo apt-get install -y libopenmpi-dev
sudo apt-get install -y libhdf5-dev
sudo apt-get install -y patch
sudo apt-get install -y git
sudo apt-get install -y pip
pip install numpy scipy matplotlib pandas h5py

# The path for building HemoCell
export MAIN=~/Desktop/learn

# To download HemoCell, comment this out if you have already done it
git clone https://github.com/UvaCsl/HemoCell.git

# To install the palabos dependencies
cd $MAIN/HemoCell/ && ./setup.sh

# To install other dependencies like ParMETIS and METIS
# Both require GKlib which we first need to downlaod
cd $MAIN/HemoCell/external
git clone https://github.com/KarypisLab/GKlib.git # For GKlib
git clone https://github.com/KarypisLab/METIS.git # For METIS
git clone https://github.com/KarypisLab/ParMETIS.git # For ParMETIS

# First lets build GKlib
cd $MAIN/HemoCell/external/GKlib
make config prefix=$MAIN/HemoCell/external/GKlib # assumming that you ane using the GNU environment and gcc ( you can change this with additional arguments - see GitHub) (the prefix= stores all the files in the specified location, the default location is ~/usr/local)
make
make install

# Building METIS
cd $MAIN/HemoCell/external/METIS
make config prefix=$MAIN/HemoCell/external/METIS gklib_path=$MAIN/HemoCell/external/GKlib
make install

# Building ParMETIS
cd $MAIN/HemoCell/external/ParMETIS
make config prefix=$MAIN/HemoCell/external/ParMETIS gklib_path=$MAIN/HemoCell/external/GKlib metis_path=$MAIN/HemoCell/external/METIS
make install
cd $MAIN/HemoCell

#  Before building HemoCell we need to associate the paths in CMake (find_parmetis.cmake) so that HemoCell finds ParMETIS and METIS
# The lines 21, 29, 37, 45 of the file need to be updated with the path of ParMETIS and METIS and the following section of the code achieves that
file="$MAIN/HemoCell/cmake/find_parmetis.cmake"
tempfile="$MAIN/HemoCell/cmake/find_parmetis_temp.cmake"

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
cd $MAIN/HemoCell
mkdir build && cd build/
cmake ..
cmake --build .
