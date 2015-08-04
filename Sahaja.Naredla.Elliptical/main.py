"""
SahajaReddy Naredla
Cryptography - Program 3
Elliptical Curve
"""

import argparse
import graph
import fractions as s

    
def main():
    print("--------------------------------------------------")
    print("Program by SahajaReddy Naredla")
    print("Elliptical curves cryptography")
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", dest="a", help="Part 'a' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-b", dest="b", help="Part 'b' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-x1",dest="x1", help="")
    parser.add_argument("-y1",dest="y1", help="")
    parser.add_argument("-x2",dest="x2", help="")
    parser.add_argument("-y2",dest="y2", help="")

    args = parser.parse_args()
    a = s.Fraction(args.a)
    b = s.Fraction(args.b)
    
    x1 = s.Fraction(args.x1)
    y1 = s.Fraction(args.y1)
    
    x2 = s.Fraction(args.x2) 
    y2 = s.Fraction(args.y2)
    
    mygraph = graph.plotTheGraph(x1,y1,x2,y2,a,b)
    mygraph.findPoint()
    mygraph.drawGraph()
    print("--------------------------------------------------")           
    # Example:
    # python3 program_name.py -x1 2 -y1 3 -x2 -1 -y2 -1 -a 2 -b 1
    
    #print("a=",args.a," b=",args.b,"x1=",args.x1," y1=",args.y1," x2=",args.x2," y2=",args.y2)
    
if __name__ == '__main__':
    main()
