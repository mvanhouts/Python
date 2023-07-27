for number in range(2,101,1):
    prime = True
    for number2 in range(2, number, 1):
        if number % number2 == 0:
            prime = False
    if prime == True:
        print(number)