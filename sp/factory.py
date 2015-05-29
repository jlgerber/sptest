from sp import base

class WriterFactory(object):
    def __init__(self):
        self.base = base.Base("")
        self._writers = {}
        self.initWriters()

    def initWriters(self):
        for klass in self.base.__class__.__subclasses__():
            self._writers[klass.__name__.lower()] = klass

    def get(self, writerName):
        writer = self._writers.get(writerName)
        if writer:
            return writer()
        raise KeyError("Format %s not supported. Valid choices are:%s" % ( writerName, self._writers.keys()))
