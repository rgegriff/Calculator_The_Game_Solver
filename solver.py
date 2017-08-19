from itertools import product
# button functions
def add(x):
    f = lambda n: n+x
    f.name = "add(%s)"%x
    return f

def sub(x):
    f = lambda n: n-x
    f.name = "sub(%s)"%x
    return f
    
def reverse():
    f = lambda n: int("".join(reversed(str(n))))
    f.name = "reverse()"
    return f
    
def div_by(x):
    f = lambda n: float(n)/float(x)
    f.name = "div_by(%s)"%x
    return f
    
def mul_by(x):
    f = lambda n: n*x
    f.name = "mul_by(%s)"%x
    return f
    
def append_digit(x):
    f = lambda n: int("%s%s"%(str(n),str(x)))
    f.name = "append_digit(%s)"%x
    return f
    
def drop_last():
    f = lambda n: int(str(n)[:-1])
    f.name = "drop_last()"
    return f

def replace(old, new):
    f = lambda n: int(str(n).replace(str(old), str(new)))
    f.name = "replace(%s, %s)"%(old, new)
    return f

def sum_value():
    f = lambda n: sum(map(int, str(n)))
    f.name = "sum()"
    return f

def invert_sign():
    f = lambda n: n*-1
    f.name = "invert_sign()"
    return f

# solver
def solve(moves=5,
          goal=-17,
          start=105,
          functions=[
    invert_sign(),
    sum_value(),
    mul_by(4),
    sub(5),
    div_by(5)
          ]):
    combinations=product(enumerate(functions), repeat=moves)
    for combo in combinations:
        value = start
        values = [value]
        combo_numbers = map(lambda m: m[0], combo)
        combo_names = map(lambda m: m.name, map( lambda n: n[1], combo))
        try:

            for move in map(lambda m: m[1], combo):
                value = move(value)
                values.append(value)
                if type(value) is float:
                    if value.is_integer():
                        value = int(value)
                    else:
                        raise Exception 
            if value == goal:
                print "Winner! Winner! Chicken Dinner!"
                print combo_names
                break
        except:
            continue

solve()
