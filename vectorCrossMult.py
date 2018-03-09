from tools import *


def run():
    print("hello")
    output = [0,0,0]
    vector1 = input("Write the first vector in the format: vx vy vz ...")
    vector1 = vector1.split(" ")
    vector2 = input("Write the second vector in the format: vx vy vz ...")
    vector2 = vector2.split(" ")
    output[0] = int(vector1[1]) * int(vector2[2]) - int(vector1[2]) * int(vector2[1])
    output[1] = int(vector1[2]) * int(vector2[0]) - int(vector1[0]) * int(vector2[2])
    output[2] = int(vector1[0]) * int(vector2[1]) - int(vector1[1]) * int(vector2[0])
    #print(output)
    print_vector(output)

    

def work():
    print("Working...")
