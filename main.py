import sys
sys.path.append('kernels')
import add, multiply, divide, vectorCrossMult, tools, derivative


running = True
last = 0

mode = input("Which mode do you want to use? (1: Interpreter 2: Individual Programs)\n")
if mode == '1':
    while running:
        cmd = input("§-> ")
        cmd = cmd.split(" ")
        try:
            for i, com in enumerate(cmd):
                if com == "last":
                    cmd[i] = last
            if cmd[0] == "exit" or cmd[0] == "quit":
                running = False
                
            elif cmd[0] == "add" or cmd[0] == "+":
                result = add.work(cmd[1], cmd[2])
                answer = result[0]
                if result[1]:
                    last = answer
                print(answer)
            elif cmd[0] == "multiply" or cmd[0] == "*":
                result = multiply.work(cmd[1], cmd[2])
                answer = result[0]
                if result[1]:
                    last = answer
                print(answer)  
            elif cmd[0] == "divide" or cmd[0] == "/":
                result = divide.work(cmd[1], cmd[2])
                answer = result[0]
                if result[1]:
                    last = answer
                print(answer)
                
            else:
                print("Did not recognize cmd")
            
        except:
            print("False arguments")
            
elif mode == "2":
    while running:
            cmd = input("§-> ")
            cmd = cmd.split(" ")
            try:
                for i, com in enumerate(cmd):
                    if com == "last":
                        cmd[i] = last
                if cmd[0] == "exit" or cmd[0] == "quit":
                    running = False
                
                elif cmd[0] == "crossMult":
                    vectorCrossMult.run()
                
                elif cmd[0] == "add":
                    add.run()
                
                elif cmd[0] == "multiply":
                    multiply.run()
                    
                elif cmd[0] == "derivative":
                    derivative.run()
                    
                else:
                    print("Did not recognize cmd")
                
            except:
                print("False arguments")
print("Thanks for using Mathtoolbox by Hugo Granström")
#print(last)