Usernames_Passwords = {"Admin":"Password","Corey":"Password"}

def Login_Register():

    print("Login or Register?")
    User = str(input()).lower()

    if User == "login":
        Login_Username_Given = False
        while Login_Username_Given == False:
            Login_Username = str(input("Username: "))
            Login_Result = Usernames_Passwords.get(Login_Username, "NotFound")
            if Login_Result != "NotFound":
                Login_Username_Given = True
                Login_Password_Given = False
                while Login_Password_Given == False:
                    Login_Password = str(input("Password: "))
                    if Login_Password == Login_Result:
                        print(f"Login Successful, Welcome {Login_Username}!")
                        Login_Password_Given = True
                    else:
                        print("Wrong Password")
            else:
                print("No Username Found")

Login_Register()