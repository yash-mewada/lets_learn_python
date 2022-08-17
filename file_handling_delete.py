import os
import shutil

path = 'text.txt'

try:
    os.remove(path)          #deletes a file
    os.rmdir(path)           #deletes an empty directory
    shutil.rmtree(path)      #deletes a directory containing files
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("you do not have permission to delete that")
except OSError:
    print("you cannot delete that using that function")