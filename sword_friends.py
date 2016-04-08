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
        
def rules():
    print ("")
    print ("---RULES---")
    print ("You are a student at Tokyo High School for Gifted Swords. It's filled with pretty ladies")
    print ("who are also swords. Do nice things for them, or other things that they would agree with,")
    print ("to garner their affection. Should you amass enough emotional wealth, you can become")
    print ("BEST FRIENDS.")

def name_check():
    global player_name
    print("Your name is %s.") % (player_name) 
    check = raw_input("Are you sure? Y/N: ")
    check = check.upper()
    if check == "Y":
        rules()
    else:
        ask_name()
        
def event_one():
    raw_input("....\n'RRRRR RRRRR RRRR' goes your alarm clock.")
    raw_input("....\nYou jolt awake and look at the time. Oh no!")
    raw_input("....\nYou're ten minutes late for school already!")
    raw_input("....\nYou rush out of your spartan one-room apartment.")
    raw_input("YOU:\n'I'm gonna be late!'")
    print ("--------------------------------------")
    event_two()
                
def event_two():
    raw_input("....\nYou rush out of the train doors as they slide open.")
    raw_input("....\nUnaware of your surroundings, you crash into someone and feel a\nsharp pain in your arm.")
    raw_input("RAPIER:\n'Watch where you're going, punk!'")
    raw_input("RAPIER:\nI mean, it's not a shame that shirt got cut. It's trash.")
    cont = raw_input("How do you respond?\n1. Stand up for yourself.\n2.Joke along with her.\n3. Apologize.")
    if cont == 1:
        raw_input("YOU:\n'Hey! It's not too trashy!'")
        raw_input("RAPIER:\n'Oh my~ I'm going to like you~' she says as she skips off.")
        raw_input("YOU:\nThis is going to be a long day...")
        relation_points['Rapier'] = relation_points['Rapier'] + 1;
    elif cont == 2:
        raw_input("YOU:\n'Yeah... It's totally bad...' you say quietly.")
        raw_input("RAPIER:\n'Hmph~ You're no fun~'")
        relation_points['Rapier'] = relation_points['Rapier'] - 1;
    else:
        raw_input("YOU:\n'Sorry about that.' you respond curtly.")
        raw_input("RAPIER:\n'Hmph~' she replies and walks off.")
        
def event_three():
    raw_input("....\nYou rush into the classroom, seeing the girl from earlier take her seat.")
    raw_input("....\nShe begins chatting with a long, blond-haired girl in the corner.")
    raw_input("....\nA girl with brown hair and pigtails is sitting in the front, listening\nattentively to the teacher.")
    raw_input("....\nThe teacher scolds you and the girl from earlier about being late, but\nresumes instructing the class.")
    raw_input("....\nYou take the empty seat next to the girl in pigtails, as it is the only\none open.")
    raw_input("....\nAs you look around the room, the two gossipy girls are passing notes.")
    cont = raw_input("....\nYou turn to the girl next to you. What do you ask?\n1. What's your name?\n2. Who are those girls back there?")
    if cont == 1:
        

        
print ("Welcome to Swordfriends!")
ask_name()
event_one()