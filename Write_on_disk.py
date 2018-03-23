import os
from shutil import copyfile
n=0
if (os.name == 'nt'):
    
    while (n<10):
        copyfile(os.getcwd()+'\Write_on_disk.*', os.getcwd()+'\Write_on_disk_copy_{}.py'.format(n))
        n+=1
    
    
    
print (os.getcwd())
print (os.name)