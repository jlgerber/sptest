from sp import base

class Yaml(base.Base):
    def __init__(self):
        super(Yaml,self).__init__("yaml")

    def write(self, obj, path):
        print("writing %s to %s.%s" %(obj,path,self.extension))
