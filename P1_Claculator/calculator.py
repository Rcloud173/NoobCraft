

def cal():
    current_value = None
    operator = None

    while True:
        num = (input("enter the entire expression as a single line: "))
        
        if num == '=':
            print(current_value)
            break
        
        nu = num.split()
            
           
        if len(nu) != 3:
            print("invalid expression put something like this 3 + 4")
            continue

        num1, op, num2 = nu

        try:
            num1 = int(num1)
            num2 = int(num2)
        except ValueError:
            print("enter valid numbers.")
            continue

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("cannot divide by 0")
                continue
            result = num1 / num2
        else:
            print("Unsupported operator. Use +, -, *, or /.")
            continue

        current_value = result
        print("current result: ", current_value)

    
cal()
