# cacl1_dag

import logging
import dag

logger = logging.getLogger()


class MyDAG(dag.DAG): # implementation
    '''my dag'''
    def __init__(self):
        super(MyDAG, self).__init__()

        if hasattr(self,'a'):
            return
        self.a = dag.Node('gbp_usd')
        self.b = dag.Node('usd_eur')
        self.c = dag.Node('eur_gbp')

        self.i = dag.Node('I', self.calcRateA )
        self.a.usedby.append(self.i)
        self.b.usedby.append(self.i)

        self.o = dag.Node('GBP/USD/EUR', self.calcRateB )
        self.c.usedby.append(self.o)
        self.i.usedby.append(self.o)


    # set input node functions
    def set_a(self,v):
            logger.info ('set %s %s' %(self.a.doc,v))
            self.setValue(self.a,v)

    def set_b(self,v):
            logger.info ('set %s %s' %(self.b.doc,v))
            self.setValue(self.b,v)

    def set_c(self,v):
            logger.info ('set %s %s' %(self.c.doc,v))
            self.setValue(self.c,v)

    def ppInputs(self):
        print (self.__doc__, ' inputs')
        print ('a', '=', self.a.value, self.a.doc)
        print ('b', '=', self.b.value, self.b.doc)
        print ('c', '=', self.c.value, self.c.doc)


    def calcUSD(self ):
        '''Use ccy'''
        ccy = self.h.value
        a = self.a.value
        if ccy == 'USD':
            return a * 2
        return  0

    def calcRateA(self):
         return self.a.value * self.b.value

    def calcRateB(self):
        return self.i.value * self.c.value

#class Dag(MyDAG):
#    pass

'''
print '-------------'
MyDAG().set_a(1)
MyDAG().set_b(2)
MyDAG().set_c(3)
MyDAG().pp()
MyDAG().ppInputs()
MyDAG().ppOutputs()
print '----------'
MyDAG().set_a(2)
MyDAG().set_b(0)
MyDAG().set_b(4)
MyDAG().pp()
'''
