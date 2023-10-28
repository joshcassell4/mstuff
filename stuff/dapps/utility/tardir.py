from subprocess import Popen, call, run, PIPE
import uuid
from daarch.config import config
import os
import shutil
import time

def maketardir(path="."):
    if os.path.exists(str(path)):
        filename = 'da_' + uuid.uuid4().__str__() + ".tar.gz"
        call(['tar', '-czvf',filename,str(path)])
        shutil.move(filename, 'daarch/')

def listarch(path=config['archdir']):
    return [x for x in os.listdir(path=path) if x.endswith('tar.gz')]

def addf2arch(files=None,archfile=None):
    if not hasattr(files,'__getitem__'):
        print("files must be a list or with __getitem__")
    for x in files:
        if not os.path.exists(x):
            print("path error [files " + str(x) + "]")
            return
    if not os.path.exists(archfile):
        print("path error [archfile]")
    else:
        calllist = ['tar','-rvf',archfile] + files
        call(calllist,stdout=PIPE)