import json
import Login_Register as LR



def New_Game():
    with open("Profiles.json") as Profiles_json_read:
        Profiles_Load = json.load(Profiles_json_read)
    Loggedin_User = LR.Username()
    Availability = False
    while Availability == False:
        Game_Slot_Name = str(input("New Game Title: "))
        if Game_Slot_Name not in Profiles_Load[Loggedin_User]:
            Confirmation = False
            while Confirmation == False:
                Confirm = str(input("Name Available, Confirm? Yes/No: ")).lower()
                if Confirm =="no":
                    break
                elif Confirm == "yes":
                    Availability = True
                    Confirmation = True
                    Profiles_Load[Loggedin_User].update({Game_Slot_Name: {}})
                    with open("Profiles.json","w") as Profiles_json_write:
                        json.dump(Profiles_Load, Profiles_json_write, indent=4)
                else:
                    print("Invalid Option.")
        else:
            print("Name Not Available")



def Main_Menu():
    User = str(input("New/Load/Quit: ")).lower()
    if User == "new":
        New_Game()
    elif User == 'load':
        print("COMING SOON")
    elif User == 'quit':
        print("COMING SOON")

# GIT update: New Game Setup logic