def add(n1 , n2):
    return n1 + n2

def subtract(n1 , n2):
    return n1 - n2

def multiply(n1 , n2):
    return n1 * n2

def divide(n1 , n2):
    return n1 / n2

opretions = {
    "+" : add ,
    "-" : subtract , 
    "*" : multiply ,
    "/" : divide ,
}

def caculate():
    qustions_1 = float(input("what is your number? "))
    should_continue = True

    while should_continue :

        for symbol in opretions :
            print(symbol)
        opretion_symbol = input("pick an opertion: ")
        qustion_2 = float(input("what is the next answer? "))
        answer = opretions[opretion_symbol](qustions_1 , qustion_2)
        print(f"{qustions_1} {opretion_symbol} {qustion_2} = {answer}")
        last_qustion = input(f"TYPE 'Y' to continue the caculating or Type 'n' to finish it. " )
        if last_qustion == "y" :
            qustions_1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            caculate()

caculate()
