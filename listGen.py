import hashlib
import glob
import os


outfile = open("list.txt",'w')

cwd = os.getcwd()

for file in glob.iglob(cwd + '/**/*.exe', recursive=True):
    hash = hashlib.md5(open(file,'rb').read()).hexdigest()
    str = file.split('/')[-1]
    outfile.write(hash+','+str+'\r\n')

outfile.close
