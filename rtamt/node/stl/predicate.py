# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:30:09 2019

@author: NickovicD
"""

from rtamt.node.stl.node import Node

class Predicate(Node):
    """A class for storing STL real-valued Variable nodes
                Inherits Node

    Attributes:
        var : String
        field : String
        io_type : IOType enumeration (INPUT, OUTPUT or UNKNOWN)
        threshold : double
        operator : OperatorType (LEQ, GEQ, LESS, GREATER, EQ or NEQ)
    """
    def __init__(self, child1, child2, io_type, operator, is_pure_python):
        """Constructor for Predicate node

        Parameters:
            var : String
            field : String
            io_type : IOType enumeration (INPUT, OUTPUT or UNKNOWN)
            operator : OperatorType (LEQ, GEQ, LESS, GREATER, EQ or NEQ)
        """

        super(Predicate, self).__init__()
        self.addChild(child1)
        self.addChild(child2)
        self.io_type = io_type
        self.operator = operator
        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars


        if is_pure_python:
            name = 'rtamt.operation.stl.predicate_operation'
            mod = __import__(name, fromlist=[''])
            self.node = mod.PredicateOperation(operator, io_type)
        else:
            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_node'
            mod = __import__(name, fromlist=[''])

            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_predicate_node'
            mod = __import__(name, fromlist=[''])
            self.node = mod.StlPredicateNode(operator, io_type)


        
    @property
    def io_type(self):
        """Getter for io_type"""
        return self.__io_type
    
    @io_type.setter
    def io_type(self, io_type):
        """Setter for io_type"""
        self.__io_type = io_type
        
    @property
    def operator(self):
        """Getter for operator"""
        return self.__operator
    
    @operator.setter
    def operator(self, operator):
        """Setter for operator"""
        self.__operator = operator
        
    @property
    def threshold(self):
        """Getter for threshold"""
        return self.__threshold
    
    @threshold.setter
    def threshold(self, threshold):
        """Setter for threshold"""
        self.__threshold = threshold
