from tools import *
import math

def run():
    f = input("Input the function you want to take the derivative of:\n")
    f = "(" + f + ")"
    x = input("Input the x value at which to calculate the derivative:\n")
    h = "10**(-6)"
    f = process_math_string(f)
    f1 = f.replace("x", "(" + x + "+" + h + ")")
    f2 = f.replace("x", "(" + x + "-" + h + ")")
    output = "(" + f1 + "-" + f2 + ")/(" + "2*h".replace("h", h) + ")"
    #print(output)
    print(eval(output))
   
#run()


