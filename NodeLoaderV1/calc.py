#file name - calculator
#description - do calculations in seconds! 
def main():
    userOperation = input("what operation would you like?")
    userNo1 = int(input("what is your first number?"))
    userNo2 = int(input("and your second?"))
    if userOperation == "+":
        answer = userNo1 + userNo2
        print ("answer is", answer)
    elif userOperation == "-":
        answer = userNo1 - userNo2
        print ("answer is", answer)
    elif userOperation == "*":
        answer = userNo1 * userNo2
        print ("answer is", answer)
    elif userOperation == "/":
        answer = userNo1 / userNo2
        print("answer is", answer)
    else:
        print("syntax error.")