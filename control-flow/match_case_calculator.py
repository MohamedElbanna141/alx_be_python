num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")


match num1 :
    case 0 :
        print("Cannot divide by zero.")
    case _ :
        match num2 :
            case 0 :
                print("Cannot divide by zero.")
            case _ :
                match operation :
                    case "+" :
                        print("The result is ", num1 + num2,".")
                    case "-" :
                        print("The result is ", num1 - num2,".")
                    case "*" :
                        print("The result is ", num1 * num2,".")
                    case "/" :
                        print("The result is ", num1 / num2,".")