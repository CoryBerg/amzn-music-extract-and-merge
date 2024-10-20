import os, shutil
import zipfile
wd = "C:/temp/music/";
if not os.path.isdir(wd):
    os.makedirs(wd);
path = "C:/Users/Cory/Music/tmp/";
entries = os.scandir(path);
for i in entries:
    #if mp3, move to manual handling dir
    #else, if zipped file, unzip but ignore initial file name
    if(i.name.split(".")[-1] == 'mp3'):
        srce = os.path.join(path,i)
        dest = os.path.join(wd)
        print("Copying mp3 " + srce + " to " + dest)
        try:
            shutil.copy2(srce, dest);
        except Exception as ex:
            print("Failed to copy: " + i + " Error: " + ex.message)
    elif(i.name.split(".")[-1] == 'zip'):
        try:
            zipfile.ZipFile(os.path.join(path,i)).extractall(path=wd);
        except Exception as ex:
            print("Failed to extract " + i + " to " + wd + " Error: " + ex.message)
    else:
        print("Not sure what to do with: " + i);
