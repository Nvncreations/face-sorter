import shutil
import os
def file_copy(srs,dat,file):
    dst_file = os.path.join(dat, file)
    #with open(dst_file, "wb") as f:  # Create the file
    shutil.copy(srs, dst_file)
        


