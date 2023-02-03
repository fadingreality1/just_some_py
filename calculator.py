import os
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""



def add(n1:float,n2:float) -> float:
    return n1+n2

def sub(n1:float,n2:float) -> float:
    return n1-n2

def mul(n1:float,n2:float) -> float:
    return n1*n2

def div(n1:float,n2:float) -> float:
    return n1/n2

function = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div,
    }

def new():
    print(logo) 
    n1 = float(input("What's the first number ? "))
    cal(n1)

def cal(num : float) -> float:
    for i in function:
        print(i)
        
    op = input("pick an operation: ")

    n2 = float(input("What's the next number: "))

    res = function[op](num,n2)
    print(f"{num} {op} {n2} = {round(res,2)}")

    ch = input(f"Type 'y' to continue calculating with {round(res,2)}, or type 'n' to start a new calculation:")
    if ch[0] == 'y':
        return cal(res)
    else:
        os.system('cls')
        new()

new()