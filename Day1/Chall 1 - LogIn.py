# Challenge 1 - Create a Login System
success = False
count = 0
while success == False and count < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open("credential.txt","r") as file:
        for line in file:
            text = line.strip()
            user, pasw =  text.split(",")
            if username == user and password ==pasw:
                success = True
                break
        if success ==False:
                count+=1
                print("Retry, you have ",(5-count), " attempts left.")
    file.close()
if success== True:
    print("LogIn Successful")
else:
    print("LogIn Failed")
