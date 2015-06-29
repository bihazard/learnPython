#program to check whether one can vote or not
while (1):
    a=int(input("Enter your age"))
    if (a<18):
        print("You are small age to vote")
        print ('Testing')
    elif (a>18):
        print('''You have voted more than once.
              Please vote it again''')
    else:
        print ("This is your first vote")
    print ('hellow')
else:
    print ("Thank you for using this program")
              
              
    