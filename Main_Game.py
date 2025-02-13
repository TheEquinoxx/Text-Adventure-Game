Usernames_Passwords = {}



def Login():
    Login_Username_Given = False
    while Login_Username_Given == False:
        Login_Username = str(input("Login Username: "))
        Login_Result = Usernames_Passwords.get(Login_Username, "NotFound")
        if Login_Result != "NotFound":
            Login_Username_Given = True

            Login_Password_Given = False
            while Login_Password_Given == False:
                Login_Password = str(input("Login Password: "))
                if Login_Password == Login_Result:
                    print(f"Login Successful, Welcome {Login_Username}!")
                    Login_Password_Given = True
                else:
                    print("Wrong Password")
        else:
            print("No Username Found")



def Register():
    Register_Username_Given = False
    while Register_Username_Given == False:
        Register_Username = str(input("Register Username: "))
        Register_Result = Usernames_Passwords.get(Register_Username, "NotFound")
        if Register_Result == "NotFound":
            Register_Username_Confirmation = False
            while Register_Username_Confirmation == False:
                Register_Username_Confirm = str(input("Username Available, Confirm? Yes or No: ")).lower() 
                if Register_Username_Confirm == "no":
                    break
                elif Register_Username_Confirm == "yes":
                    Register_Username_Confirmation = True
                    Register_Username_Given = True

                    Register_Password_Given = False
                    while Register_Password_Given == False:
                        Register_Password = str(input("Register Password: "))
                        Register_Password_Confirmation = False
                        while Register_Password_Confirmation == False:
                            Register_Password_Confirm = str(input("Confirm Password? Yes or No: ")).lower()
                            if Register_Password_Confirm == "no":
                                break
                            elif Register_Password_Confirm == "yes":
                                Register_Password_Confirmation = True
                                Register_Password_Given = True
                            else:
                                print("invalid Option")
                else:
                    print("invalid Option.")
        else:
            print("Username not Available, Try Again.")

    Usernames_Passwords.update({Register_Username:Register_Password})



def Main_Menu():
    print("Login or Register?")
    User = str(input()).lower()
    if User == "login":
        Login()
    elif User == "register":
        Register()
        Login()



Main_Menu()