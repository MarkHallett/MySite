# dag_dot

import time
import logging
import pygraphviz as pgv
#import mr_mess_bus
import threading
import publish

logger = logging.getLogger()

class DAG(object): # functionality
    '''Base DAG'''
    __shared_state = {}  # would be nice to use a collections.OrderedDict()
    #__filename = None

    def __init__(self, filename):
        self.__dict__ = self.__shared_state

        self.filename = filename
        self.G=pgv.AGraph(directed=True,strict=True,rankdir='LR')
        self.input_nodes=[]

    def makeNode(self,label,calc,usedby,nodetype):
        n = Node(label,calc,usedby,nodetype)
        if nodetype == 'in':
            self.input_nodes.append(n)
        self.defNode(n,usedby =usedby, nodetype=nodetype)
        return n

    def defNode(self,node,usedby,nodetype):
        doc = node.doc
        if nodetype == 'in':
            self.G.add_node(doc, shape="square")
            #node= self.AddInNode(doc)
            for n in usedby:
                self.AddEdge(doc,n.doc)
        elif nodetype == 'internal':
            #node= self.AddNode(doc,self.calcRateA)
            for n in usedby:
                self.AddEdge(doc,n.doc)
        elif nodetype == 'out':
            self.G.add_node(doc, color="white")


    def AddEdge(self,node1,node2):
        self.G.add_edge(node1,node2,label='Undefined')

    def update_node(self,node1,node2,value):
        #if node2.nodetype == 'out':
        #    mr_mess_bus.publish(node.doc,value)

        color = 'green'
        fontcolor='blue'
        if value == '-':
            fontcolor='black'
        elif value in ( 0, 'e'):
            fontcolor='red'
            color='red'

        #self.G.add_node(node1,color=color,fontcolor=fontcolor,tooltip='hello')
        #A [URL="[A|home]" tooltip="A link"]
        self.G.add_node(node1,color=color,fontcolor=fontcolor,URL=node1+'.html',tooltip=node1)
        self.G.add_edge(node1,node2, label=value,fontcolor=fontcolor,color=color)
        self.dot_pp()

        t = threading.Timer(1, self.fade, args=(node1, node2,value,color) )
        t.start()

    def fade(self,node1, node2,value,color):
        #print 'FADE'
        fontcolor=color
        color = color
        self.G.add_node(node1,color=color,fontcolor=fontcolor,URL=node1+'.html',tooltip=node1)
        self.G.add_edge(node1,node2, label=value,fontcolor=fontcolor,color=color)
        self.dot_pp()



    def set_input(self,doc,value):
        for node in self.input_nodes:
            if node.doc == doc:
                logger.info ('set %s %s' %(node.doc,value))
                for usedby in node.usedby:
                     self.update_node(doc,usedby.doc, value=value)
                self.setValue(node,value)
                return

    def dot_pp(self):
        #print 'print dot and convert to png'
        #print self.G
        self.G.layout(prog='dot') # layout with default (neato)
        #print 'Draw'
        self.G.draw(self.filename)

    def setValue(self,n,v):
        if v == n.value:
            return

        # build the DAG
        n.value = v
        for u in n.usedby:
           if u.calc == None:
               continue
           new_value = None
           try:
              #u.pp()
              new_value = u.calc(node=n)
           except Exception as e:
              print (str(e))

           self.setValue(u,new_value)

           # if output print
        print ('SET VALUE used by', n.usedby[0].doc)
        if n.usedby[0].usedby == []:
            #print '!! SET VALUE OF OUTPUT'
            msg = 'update dag_dot.py %s %s' %(n.usedby[0].doc, n.value)
            logger.info (msg)
            #print msg
            publish.run(n.usedby[0].doc,str(n.value))
            #mr_mess_bus.publish(n.usedby[0].doc,str(n.value))


    def pp(self): # must be over ridden by a borg
        # use doc string on class
        print (self.__doc__)
        for k, v in self.__dict__ .items():
            if type(v) == type(Node()):
                print (k,)
                v.pp()

    def ppInputs(self):
        print (self.__doc__, ' Inputs')
        for n in self.input_nodes:
            n.pp()

    def ppOutputs(self):
        print (self.__doc__, ' Outputs')
        for k, v in self.__dict__ .items():
            if type(v) == type(Node()):
                if v.usedby == []:
                    print (k,)
                    print ('=', v.value, v.doc)

def calc(f1):
        def f3(self,*args, **kwargs):
            node=kwargs['node']

            for u_node in node.usedby:
                for o_node in u_node.usedby:
                    self.update_node(u_node.doc,o_node.doc, value='-')

            try:
                rtn = f1(self,*args, **kwargs)
            except Exception as e:
                print ('Error in %s: %s' %(u_node.doc,str(e)))
                #rtn = str(e)
                rtn = 'e'

            for u_node in node.usedby:
                for o_node in u_node.usedby:
                    self.update_node(u_node.doc,o_node.doc, value=rtn)

            self.dot_pp()
            return rtn
        return f3



class Node(object):
    def __init__(self,doc=None, calc=None,usedby=None, nodetype=None):
        self.calc = calc
        self.doc = doc
        self.usedby = usedby
        self.value = None
        self.nodetype = nodetype

    def pp(self):
        if self.usedby:
            print ("= %s, %s, used by, %s" %( self.value , self.doc, [n.doc for n in self.usedby]))
        #else:
        #    print "= %s, %s, 'output node', %s" %( self.value , self.doc,  self.calc.__doc__)

#----------------------------------------------------------
