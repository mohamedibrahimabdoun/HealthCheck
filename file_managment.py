import os, sys
import xml


def getdirectoryfile(path):
   # path = "D:\HealthCheck\SQL"
    dirs = os.listdir( path )

    files=[]
    # This would print all the files and directories
    for file in dirs:   
        fullpath=os.path.join(path,file)
        files.append(fullpath)
    return files

#print(getdirectoryfile("D:\HealthCheck\SQL"))

def getfiletext(filename):
    
    with open(filename, 'r') as f:
        data=f.read()
    f.close()
    return data
  
