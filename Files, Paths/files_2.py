#  use shutil to access copy, move, rename 
# copy(target,destination)  <<< changing the name of destination can also copy and rename simoultaneously
# copytree(target,dest) << copies folder structure to a new location
# move() >>> moves a file. no copy remains at target
# move()  >>> used to rename a file by keeping the destination the same as target and using a different filename
# .rmtree() >> removes a folder structure


# using os.unlink() to delete a single file 
# using os.rmdir() << remove a folder

# use send2trash module to delete files and send them to the recylce bin 
