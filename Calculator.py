print("Welcome to Calculator")
print("Type 'Q' to exit\n")

previous = 0
run = True

def calc():
    global run
    global previous
    equation = input("Enter equation : ")
    if equation == 'Q':
        run = False
    else:
        previous = eval(equation)
        print("Answer is ", previous)

while run:
    calc()
