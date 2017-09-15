# cacl1_dag

import time
import logging
import dag_dot

logger = logging.getLogger()


class MyDAG(dag_dot.DAG): # implementation
    '''my dag'''
    #def __init__(self,filename):
    def __init__(self,filename):

        super(MyDAG, self).__init__(filename)

        if hasattr(self,'o'):
            return

        # output node
        self.o = self.makeNode(label='GBP/USD/EUR',calc=None,usedby = [],    nodetype='out')

        # internal node
        self.bb = self.makeNode(label='calc_B',calc=self.calcRateB,usedby=[self.o], nodetype='internal')
        self.i = self.makeNode(label='calc_A',calc=self.calcRateA,usedby=[self.bb], nodetype='internal')

        # input nodes
        self.a = self.makeNode(label='gbp/usd',calc=None,usedby=[self.i], nodetype='in')
        self.b = self.makeNode(label='usd/eur',calc=None,usedby=[self.i], nodetype='in')
        self.c = self.makeNode(label='eur/gbp',calc=None,usedby=[self.bb], nodetype='in')

        self.dot_pp()


    @dag_dot.calc
    def calcRateA(self, node=None):
        #time.sleep(1)
        return self.a.value * self.b.value

    @dag_dot.calc
    def calcRateB(self, node=None):
        #time.sleep(1)
        return self.i.value * self.c.value

'''
print '-1------------'

p = 1
d = MyDAG('./G.png') #'G.png')
time.sleep(p)
print 'set a 1'
d.set_input('gbp/usd',1)
time.sleep(p)
print 'set b 2'
d.set_input('usd/eur',2)
time.sleep(p)
print 'set c 3'
d.set_input('eur/gbp',3)
time.sleep(p)
#d.pp()
#d.ppInputs()
#d.ppOutputs()
print '-2---------'
d.set_input('gbp/usd',2)
time.sleep(p)
d.set_input('usd/eur',0)
time.sleep(p)
d.set_input('usd/eur',4)
time.sleep(p)
d.pp()
'''
