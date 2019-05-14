T = eval(input())
Stock = []
for i in range(T):
    #Num = eval(input())
    s = input().split()
    Left = eval(s[0])
    Operator = str(s[1])
    Right = eval(s[2])
    Result = eval(s[4])

    if Operator == '+':
        if Left + Right == Result:
            Stock.append("correct")
        else:
            Stock.append("wrong answer")
    elif Operator == '*':
        if Left * Right == Result:
            Stock.append("correct")
        else:
            Stock.append("wrong answer")
    elif Operator == '-':
        if Left - Right == Result:
            Stock.append("correct")
        else:
            Stock.append("wrong answer")
    elif Operator == '/':
        if Left / Right == Result:
            Stock.append("correct")
        else:
            Stock.append("wrong answer")

for l in Stock:
    print(l)