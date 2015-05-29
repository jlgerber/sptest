
class Base(object):
    def __init__(self,extension):
        self.extension=extension
        
    def write(self, obj, path):
        raise NotImplementedError()
