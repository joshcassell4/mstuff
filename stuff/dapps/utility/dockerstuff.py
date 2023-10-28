import docker
import shutil
import os

cdk = docker.from_env()

#a_dir = '/workspaces/codespaces-flask/things2'
#port=5000

class DockerApp():
    def __init__(self,tdir,adir,tagname,port,client,network):
        self.adir = adir
        self.port = port
        self.client = client
        self.tagname = tagname
        self.tdir = tdir
        self.network = network
        self.im = None
        self.cont = None
    
    # def delete_a_dir(self):
    #     shutil.rmtree(self.a_dir)
    

    def _makeadir(self):
        if not os.path.exists(self.adir):
            print(f"creating {self.adir}")        
            shutil.copytree(self.tdir,self.adir)
        else:
            print(f'adir path: {self.adir} already exists!')

    def _builddocker(self):
        print(f"building with Dockerfile:{self.adir}/Dockerfile tagname:{self.tagname}")
        return self.client.images.build(tag=self.tagname,path=f'{self.adir}/.')
    
    def _runapp(self,file=None):
        #if file:
         #  pass
           # self.client.containers.run(self.tagname,network=self.network,name=self.tagname,detach=True,volumes=[f'{self.adir}/things:/things'],ports={5000:self.port})
        print(f"running {self.tagname}")
        return self.client.containers.run(self.tagname,network=self.network,name=self.tagname,detach=True,volumes=[f'{self.adir}/things:/things'],ports={5000:self.port})
            
    def build_run(self,makeadir=False):
        if makeadir:
            self._makeadir()
        self.im = self._builddocker()
        self.cont = self._runapp()

    def stop(self):
        print("stopping container " + self.cont.name + "-" + str(self.cont.id))
        self.cont.stop()
        print("returning container " + self.cont.name + "-" + str(self.cont.id))
        return self.cont
        
