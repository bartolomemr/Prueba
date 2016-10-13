# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 18:32:03 2016

@author: toli
"""

import argparse

def arith(num1, num2, operation):
    """arith(num1,num2,operacion): returns operation (addition, substraction or multiply) of two numbers"""
    
    try:
        num1 = int(num1)
    except Exception as e:
        print 'first number should be an int'

    try:
        num2 = int(num2)
    except Exception as e:
        print 'second number should be an int'
    
    assert 1, 'operation unrecognized'
    
    if operation=='a':
        return num1+num2
    if operation=='s':
        return num1-num2
    if operation=='m':
        return num1*num2
    raise ValueError ('operation ' + operation + ' undefined')    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="returns operation (addition, substraction or multiply) of two numbers")
    parser.add_argument("num1", help="first number")
    parser.add_argument("num2", help="second number")
    parser.add_argument("operation", help="operation: addition (a), substraction (s) or multiply (m)")
    parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
    args  = parser.parse_args()

    if args.verbose:
        print "Operation {} over numbers {} and {} is: \n {}".format(args.operation, args.num1, args.num2, arith(args.num1,args.num2,args.operation))
    else:
        print arith(args.num1,args.num2,args.operation)