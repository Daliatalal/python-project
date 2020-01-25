def menu():
    print("\n")
    print("************WELCOME KAWKAB************")
    print("\n")
    print(  "A. Want to Parse access.log files and extract all information?")
    print(  "B. Want to monitor dictionary?")
    print(  "C. Want to gain the open ports And to pass them to Nmap ?")
    print(  "D. Want to detect ATTACK?")
    print("\n")
    print("*************************************") 
    print("\n")
   
loop=True
while loop:
    menu()
    choice=input("Please enter your choice:" )

    if choice == "A" or choice =="a":
        exec(open("one.py").read())

    elif choice == "B" or choice =="b":
        exec(open("two.py").read())

    elif choice == "C" or choice =="c":
        exec(open("th.py").read())

    elif choice == "D" or choice =="d":
        print("\n")
        print("please run the <four_client> file from github ")
        print("\n")
        exec(open("fourHon.py").read())
        loop=False
    else:
        print("\n")

        print("Please try again")

        input("You must only select either A,B,C, or D , press Enter please")
        print("\n")

        menu()