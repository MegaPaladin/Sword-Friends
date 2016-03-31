relation_points = {'Backsword' : 0, 'Katana' : 0, 'Longsword' : 0, 'Rapier' : 0, 'Szabla' : 0, 'Tulwar' : 0}
sword_names = ["KATANA", "BACKSWORD", "LONGSWORD", "RAPIER", "SZABLA", "TULWAR"]
player_name = ""

def ask_name():
    global player_name
    global sword_names
    player_name = raw_input("Please enter your name: ")
    player_name = player_name.upper()
    if player_name.isalpha() and player_name not in sword_names:
        print player_name
        name_check()
    else:
        print ("Invalid name!")
        ask_name()

def name_check():
    global player_name
    check = raw_input("Your name is %s. Are you sure? Y/N: ")
    check = check.upper()
    if check == "N":
        #continue
    else:
        ask_name()
        
        
print ("Welcome to Swordfriends!")
ask_name()