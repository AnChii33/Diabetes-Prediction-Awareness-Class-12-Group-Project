import pyttsx3
from Project_Library import *
voice_greetings()
name, age, gender, phn_no = user_data = user_data_verified()
options_used = []
engine = pyttsx3.init()
engine.setProperty("voice", "english")
engine.say("WELCOME TO <HEALTH AWARENESS DEVICE>")
engine.runAndWait()
while True:
    print()
    print("|*|*|*|*|*|*** WELCOME TO <HEALTH AWARENESS DEVICE> ***|*|*|*|*|*|")
    print()
    print("Enter '1' To watch videos in YouTube on diabetes")
    print("Enter '2' To check for bestselling diabetic medicine in TATA 1mg")
    print("Enter '3' To check if you have a tendency to be diabetic or not")
    print("**** Enter 'EXIT' to Exit")
    print()
    a = input("ENTER HERE:<< ")
    print()
    if a == "1":
        if a not in options_used:
            options_used.append(a)
        youtube()
    elif a == "2":
        if a not in options_used:
            print()
            engine.say("Redirecting to website...")
            
            print("Redirecting to website [TATA 1mg]...")
            engine.runAndWait()
            options_used.append(a)
        onemg()
    
    elif a == "3":
        if a not in options_used:
            options_used.append(a)
        diabetes_check(name, age, gender)
        
    elif a == "EXIT":
        chk = input("Do you really want to Exit? (y/n): ")
        if chk == "y" or chk == "Y":
            engine.say("Thank You for using the <HEALTH AWARENESS DEVICE>!")
            print("Thank You for using the <HEALTH AWARENESS DEVICE>!")
            engine.runAndWait()
            if not options_used:
                options_used = "NONE"
            user_data.append(options_used)
            user_records(user_data)
            print("User data recorded!")
            print()
            break
        else:
            continue
        
    else:
        engine.say("Invalid Input! Re enter...")
        print("Invalid Input! Re enter...")
        engine.runAndWait()
