from sp import base

class Text(base.Base):
    def __init__(self):
        super(Text,self).__init__("txt")

    def write(self, obj, path):
        print("writing %s to %s.%s" %(obj,path,self.extension))
