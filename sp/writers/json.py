from sp import base

class Json(base.Base):
    def __init__(self):
        super(Json,self).__init__("json")

    def write(self, obj, path):
        print("writing %s to %s.%s" %(obj,path,self.extension))
