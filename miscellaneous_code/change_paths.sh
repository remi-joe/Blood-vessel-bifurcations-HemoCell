#!/bin/bash

file="/scratch/s400531/HemoCell/cmake/find_parmetis.cmake"
tempfile="/scratch/s400531/HemoCell/cmake/find_parmetis_temp.cmake"

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
