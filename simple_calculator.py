def check_number(n):
    while(n.isnumeric()==False):
        n=input('Please enter numeric value ')
    return n
def check_operation(n):
    def cc():
            if(n=='+'):
                return True
            elif (n=='-'):
                return True
            elif (n=='*'):
                return True
            elif (n=='/'):
                return True
            elif (n=='**'):
                return True
            elif (n=='%'):
                return True
            else:
                return False          
    while (cc()==False):
        n=input('Please enter either + or - or * or / or ** or % ')
    return n
def main():
    print("Hello! I am your simple Calulator!!")
    first_number = input('First number? ')
    first_number=check_number(first_number)
    operation= input('Operation? ')
    operation= check_operation(operation)
    check_operation(operation)
    second_number= input('Second number? ')
    second_number = check_number(second_number)
    work=' '
    total=0
    if(first_number.isnumeric()==True):    
        if(operation=='+'):
            total=int(first_number)+int(second_number)
            work='Sum '
        elif(operation=='-'):
            total=int(first_number)-int(second_number)
            work='Difference '
        elif(operation=='*'):
            total=int(first_number)*int(second_number)
            work='Product '
        elif(operation=='/'):
            total=int(first_number)/int(second_number)
            work='Quotient '
        elif(operation=='**'):
            total=int(first_number)**int(second_number)
            work='Exponent '
        elif(operation=='%'):
            total=int(first_number)%int(second_number)
            work='Modulus '

    print(work +'of ' + first_number + operation + second_number + " equals: "+ str(total))

main()