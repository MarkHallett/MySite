# dag


import logging

import publish

logger = logging.getLogger()

class DAG(object): # functionality
    '''Base DAG'''
    __shared_state = {}  # would be nice to use a collections.OrderedDict()
    def __init__(self):
        self.__dict__ = self.__shared_state

    def setValue(self,n,v):
        if v == n.value:
            return

        # build the DAG
        n.value = v
        for u in n.usedby:
           new_value = None
           try:
              new_value = u.calc()
           except:
               pass # leave value as None # Could set as error string ??
           self.setValue(u,new_value)

           # if output print
        if n.usedby == []:
            msg = 'update %s %s' %(n.doc, n.value)
            logger.info (msg)
            publish.run(n.doc,str(n.value))

    def pp(self): # must be over ridden by a borg
        # use doc string on class
        print (self.__doc__)
        for k, v in self.__dict__ .items():
            if type(v) == type(Node()):
                print (k,)
                v.pp()

    def ppInputs(self):
        print (self.__doc__, ' Inputs')
        print ('Override in local class')

    def ppOutputs(self):
        print (self.__doc__, ' Outputs')
        for k, v in self.__dict__ .items():
            if type(v) == type(Node()):
                if v.usedby == []:
                    print (k,)
                    print ('=', v.value, v.doc)

class Node(object):
    def __init__(self,doc=None, calc=None):
        self.calc = calc
        self.doc = doc
        self.usedby = []
        self.value = None

    def pp(self):
        print ('=', self.value , self.doc , 'used by', [n.doc for n in self.usedby], self.calc.__doc__)

#----------------------------------------------------------
