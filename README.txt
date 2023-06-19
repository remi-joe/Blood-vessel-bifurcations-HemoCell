# Just make sure to identify lines with file paths and change them to your own
# Hint: On the terminal, the command 'pwd' should give you the file paths needed for the directories
# Change the versions of the dependencies to the latest ones but make sure they are built consistently with the same versions 


# There was a error: identifier "siginfo_t" is undefined
# This error seems to happen on the crescent cluster on older versions of CMake and GCC 
    # to solve this I followed the thread posted here: https://github.com/KarypisLab/GKlib/issues/13
        # I uncommented the lines in the file as instructed in the link above 
        # The lines to be uncommented in the files are given here: https://github.com/KarypisLab/GKlib/commit/a7f8172703cf6e999dd0710eb279bba513da4fec#diff-430d86fdb6c4a558ab0f1b6648bbfae1720e8bde84f026e95a52740014752040R17 
        
# The file change_path.sh is a script for changing the paths to locate both ParMETIS and METIS after they have been built
