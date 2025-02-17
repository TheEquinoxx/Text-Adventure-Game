import json
import keyring



def Login():
    with open("Profiles.json") as FileLoad: # open file
        Content = json.load(FileLoad) # load content of file to content variable
    Login_Username_Given = False # loop switch
    while Login_Username_Given == False: # begin loop
        global Login_Username
        Login_Username = str(input("Login Username: ")) # input username
        if Login_Username in Content: # checks if username exists in content
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
            print("No Username Found") # if result does equal NotFound
            No_Username = False # loop switch
            while No_Username == False: # begin loop
                RegisterQuestion = str(input("Register? Yes/No: ")).lower() # switch from login to register?
                if RegisterQuestion == "no": # if not confirmed restart login loop
                    break
                elif RegisterQuestion == "yes": # if confirmed exit loop  and enter registering
                    Login_Username_Given = True # loop switch
                    No_Username = True# loop switch
                    Register()
                else:
                    print("Invalid Option.") # invalid yes no response



def Register():
    with open("Profiles.json") as FileLoad: # open file
        Content = json.load(FileLoad) # load content of file to content variable
    Register_Username_Given = False # loop switch
    while Register_Username_Given == False: # begin loop
        Register_Username = str(input("Register Username: ")) # input username to register
        if Register_Username not in Content: # checks if username exists in content
            Register_Username_Confirmation = False # loop switch
            while Register_Username_Confirmation == False: # begin loop
                Register_Username_Confirm = str(input("Confirm Username? Yes/No: ")).lower() # ask to confirm username
                if Register_Username_Confirm == "no": # if not confirmed restart loop
                    break
                elif Register_Username_Confirm == "yes": # if confirmed finish loops
                    Register_Username_Confirmation = True # loop switch
                    Register_Username_Given = True # loop switch

                    Register_Password_Given = False # loop switch
                    while Register_Password_Given == False: # begin loop
                        Register_Password = str(input("Register Password: ")) # input password
                        Register_Password_Confirmation = False # loop switch
                        while Register_Password_Confirmation == False: # begin loop
                            Register_Password_Confirm = str(input("Confirm Password? Yes/No: ")).lower() # ask to confirm password
                            if Register_Password_Confirm == "no": # if not confirmed restart loop
                                break
                            elif Register_Password_Confirm == "yes": # if confirmed finish loops
                                Register_Password_Confirmation = True # loop switch
                                Register_Password_Given = True # loop switch
                            else:
                                print("Invalid Option") # invalid yes no option
                else:
                    print("Invalid Option") # invalid yes no option
        else:
            print("Username not Available.") # if result doesnt equal NotFound meaning username isnt available

    # Saving Register Username
    with open("Profiles.json") as FileLoad:
        FileObj = json.load(FileLoad)
    FileObj.update({Register_Username:{}})
    with open("Profiles.json","w") as FileWrite:
        json.dump(FileObj, FileWrite, indent=4)
    # Saving Register Password
    keyring.set_password("Game", Register_Username, Register_Password)
    Login()



def Username():
    Username = Login_Username
    return(Username)



def Login_Register():
    User = str(input("Login/Register: ")).lower()
    if User == "login":
        Login()
        Username()
    elif User == "register":
        Register()
        Username()

# GIT update: can now register if login username doesnt exist without having to restart
# GIT update: saves username as variable to be used in other scripts when calling json Profile