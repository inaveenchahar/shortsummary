while True:             
    inp = input("Enter your name\n")
    if (inp == "q")|(inp=="Q"):       
        break   
    else:
        file1=open(f"{inp}.txt","a")
        for sub in range(0,6):
            marks=int(input(f"Enter marks in subject{sub+1}\n"))
            file1.write(f"Marks in subject {sub+1} is : {marks}")