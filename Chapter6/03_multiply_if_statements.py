a = int(input("Enter your age: "))
# if statements no: 1
if(a%2 == 0):
    print("a is even")
#end of if statements no: 1

# if statements no: 2
if(a>=18):
    print("You are above the age of consent ")
    print("God for you")
elif(a==0):
    print("you are entering 0 which is not a valid age")
else:
    print("you are below the age of consent")
    #end of if statements no: 2
print("End of program")