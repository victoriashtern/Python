def calculate(num1,sign,num2):
    total =0
    if sign=="+":
        total=num1 + num2
    elif sign=="-":
        total=num1 - num2
    elif sign=="/":
        total=num1 / num2    
    elif sign=="*":
            total=num1 * num2    
    return total
 

def insert_number():
    num =0
    while True:
        try:
            num   = int(input("Number :")) 
            return num
        except:
            print("The number should be numeric. Try again.")
    

def insert_operation():

    operation_list =["+","-","/","*","="]
    while True:
        operation   = input("Enter numeric opetration +, -, *, /:")
        if operation in operation_list:
            return operation
        else:
            print("Print try again")
    

def main():

    expression =[]
    total  = insert_number()
    expression.append(total)
    operation  = insert_operation()
    
    while operation!="=":
        expression.append(operation)
        num2  = insert_number()
        expression.append(num2)
        total = calculate(total,operation,num2)
        operation  = insert_operation()
        
    print("Expression:")
    for item in expression:
        print(item, end=" ")

    print("= :",total )

if __name__=="__main__":
    main()