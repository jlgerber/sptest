#!/usr/bin/env python

import sys
from sp import factory
from sp.writers import *

  
def main():
    wtype = "text"

    if len(sys.argv) > 1:
        wtype = sys.argv[1]
        
    ft = factory.WriterFactory()
    try:
        ft.get(wtype).write("blablabla","/var/tmp/soundPublishFile")
    except KeyError,msg:
        print msg

if __name__ == "__main__":
    main()
