import json
import keyring



def Login():
    Login_Username_Given = False # loop switch
    while Login_Username_Given == False: # begin loop
        Login_Username = str(input("Login Username: ")) # input username
        with open("Profiles.json") as FileLoad: # open file
            Content = json.load(FileLoad) # load content of file to content variable
            if Login_Username in Content: # checks if username exists in content
                Username_Result = Login_Username # if it does exist save username as result variable
            else:
                Username_Result = "NotFound" # if it doesnt exist save NotFound as result variable
        if Username_Result != "NotFound": # if result doesnt equal NotFound finish loop
            Login_Username_Given = True # loop switch

            Login_Password_Given = False # loop switch
            while Login_Password_Given == False: # begin loop
                Login_Password = str(input("Login Password: ")) # input password
                Password_Result = keyring.get_password("Game", Login_Username) # load password for username given as result variable
                if Login_Password == Password_Result: # checks if password given matches stored password
                    print(f"Login Successful, Welcome {Login_Username}!") # if it does matches finish Login
                    Login_Password_Given = True # loop switch
                else:
                    print("Wrong Password") # if it doesnt match print wrong password
        else:
            print("No Username Found") # if result does equal NotFound restart loop



def Register():
    Register_Username_Given = False # loop switch
    while Register_Username_Given == False: # begin loop
        Register_Username = str(input("Register Username: ")) # input username to register
        with open("Profiles.json") as FileLoad: # open file
            Content = json.load(FileLoad) # load content of file to content variable
            if Register_Username in Content: # checks if username exists in content
                Register_Result = Register_Username # if it does exist save username as result variable
            else:
                Register_Result = "NotFound" # if it doesnt exist save NotFound as result variable
        if Register_Result == "NotFound": # if result equals not found meaning username is available
            Register_Username_Confirmation = False # loop switch
            while Register_Username_Confirmation == False: # begin loop
                Register_Username_Confirm = str(input("Username Available, Confirm? Y or N: ")).lower() # ask to confirm username
                if Register_Username_Confirm == "n": # if not confirmed restart loop
                    break
                elif Register_Username_Confirm == "y": # if confirmed finish loops
                    Register_Username_Confirmation = True # loop switch
                    Register_Username_Given = True # loop switch

                    Register_Password_Given = False # loop switch
                    while Register_Password_Given == False: # begin loop
                        Register_Password = str(input("Register Password: ")) # input password
                        Register_Password_Confirmation = False # loop switch
                        while Register_Password_Confirmation == False: # begin loop
                            Register_Password_Confirm = str(input("Confirm Password? Y or N: ")).lower() # ask to confirm password
                            if Register_Password_Confirm == "n": # if not confirmed restart loop
                                break
                            elif Register_Password_Confirm == "y": # if confirmed finish loops
                                Register_Password_Confirmation = True # loop switch
                                Register_Password_Given = True # loop switch
                            else:
                                print("invalid Option") # invalid yes no option
                else:
                    print("invalid Option.") # invalid yes no option
        else:
            print("Username not Available, Try Again.") # if result doesnt equal NotFound meaning username isnt available



    # Saving Register Username
    with open("Profiles.json") as FileLoad:
        FileObj = json.load(FileLoad)
    FileObj.update({Register_Username:{}})
    with open("Profiles.json","w") as FileWrite:
        json.dump(FileObj, FileWrite, indent=4)

    # Saving Register Password
    keyring.set_password("Game", Register_Username, Register_Password)



def LoginScreen():
    print("Login or Register?")
    User = str(input()).lower()
    if User == "login":
        Login()
    elif User == "register":
        Register()
        Login()



LoginScreen()