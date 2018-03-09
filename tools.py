def print_vector(vector):
    a = "("
    for i in range(0, len(vector)):
        if i == len(vector)-1:
            a += str(vector[i])
        else:
            a += str(vector[i]) + ", "
    a += ")"
    print(a)

def process_math_string(f):
    f = f.replace("^", "**")
    f = f.replace("lg(", "math.log10(")
    f = f.replace("pi", "math.pi")
    f = f.replace("e", "math.e")
    f = f.replace("cos(", "math.cos(")
    f = f.replace("sin(", "math.sin(")
    f = f.replace("tan(", "math.tan(")
    f = f.replace("log(", "math.log(")
    f = f.replace("ln(", "math.log(")
    
    return f

#acos is written as cosa