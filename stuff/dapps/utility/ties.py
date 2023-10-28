import subprocess as sb
from pprint import pprint
def cf(f):
    x = sb.call(['code',f])
    return x

def pfs(f):
    pprint(dir(f))

def pds(f):
    print(dir(f))

# def rf(f):
#      -i f

def c(l,*args):
    sb.call(l,args)

def rf(f,m={}):
    with open(f) as fi:
        u = fi.read()
        exec(u,globals=m)
    return m

def rfs(f):
    with open(f) as fi:
        d = fi.read()
    return d
    
    

    