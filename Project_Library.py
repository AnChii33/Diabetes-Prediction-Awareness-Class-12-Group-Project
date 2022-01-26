import datetime
import pyttsx3
from selenium import webdriver
import matplotlib.pyplot as plt
import pywhatkit
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import csv
engine = pyttsx3.init()
engine.setProperty("voice", "english")
# ----------------------------------------------------------------------------------------------------------------------------
def voice_greetings():
    try:
        engine.runAndWait()
        now = datetime.datetime.now()
        dt = now.strftime("%d/%m/%Y %H:%M:%S")
        print()
        print(dt)
        dt = dt.split(" ")
        a = dt[1].split(":")
        b = int(a[0])
        if b < 12:
            engine.say("GOOD MORNING!")
            print("GOOD MORNING!")
        elif 12 <= b < 16:
            engine.say("GOOD AFTERNOON!")
            print("GOOD AFTERNOON!")
        else:
            engine.say("GOOD EVENING!")
            print("GOOD EVENING!")
        engine.runAndWait()
        print()
    except Exception:
        print("!!** Error encountered **!!")
# ----------------------------------------------------------------------------------------------------------------------------
def user_data_verified():
    user=input("Enter your FULL NAME: ")
    while True:
        try:
            age = int(input("Enter your AGE: "))
            if age<1:
                print("Age must be GREATER THAN 0 [ZERO]!\
 Check the input and re-enter...")
                print()
            else:
                break
        except Exception:
            print("Enter INTEGER only!")
            print()
    while True:
        gen = str(input("Enter your GENDER\
 [Male=>'M' || Female=>'F' || Others=>'X']: "))
        if gen not in ["M", "F", "X"]:
            print("Invalid option entered!\
 Check directions and re-enter...")
            print()
        else:
            break
        import pyttsx3
    while True:
        ph_no=input("Enter your INDIAN MOBILE NUMBER: +91-")
        if ph_no.isdigit()==False or len(ph_no)!=10:
            print("Invalid mobile number entered! Re enter...")
            print()
        else:
            break
    return [user, age, gen, ph_no]
# ----------------------------------------------------------------------------------------------------------------------------
def youtube():
    try:
        while True:
            print("**** ENTER 'BACK' to go back to MAIN MENU")
            print("--> Enter search-phrase with the word\
 'diabetes' in it for YouTube videos: ")
            print()
            command=input("ENTER HERE:<< ")
            if command=="BACK":
                break
            elif 'diabetes' in command.lower():
                print()
                engine.say("Playing ")
                print("Playing...")
                print()
                engine.runAndWait()
                pywhatkit.playonyt(command)
            else:
                engine.say("Key-word 'diabetes' missing!")
                print("Key-word 'diabetes' missing!")
                engine.runAndWait()
                print()
    except  Exception:
        print("!!** Error encountered **!!")
# ----------------------------------------------------------------------------------------------------------------------------
def onemg():
    url = 'https://www.1mg.com/categories/diabetes/diabetic-medicines-583'
    driver = webdriver.Chrome()
    driver.get(url)
    p_name = []
    p_price = []
    temp=0
    k=1
    for i in range(1, 4):
        pname = driver.find_element_by_xpath('//*[@id="category-container"]/div[2]\
/div[2]/div[2]/div/div[2]/div[1]/div['+str(i)+']/div/a/div['+str(4-i+k)+']/div[1]').text
        p_name.append(pname)
        pprice = driver.find_element_by_xpath('//*[@id="category-container"]/div[2]\
/div[2]/div[2]/div/div[2]/div[1]/div['+str(i)+']/div/a/div['+str(6-i+k)+']/div/div[2]/span').text
        plist = pprice.split()
        p_price.append(plist[0])
        temp, k = k, temp+k
    p_sname = []
    for i in p_name:
        p_sname.append((i.split())[0])
    for i in range(0, len(p_price)):
        p_price[i] = p_price[i].replace('₹', '')
        p_price[i] = float(p_price[i])
    d = {"product_name": p_sname,"product_price": p_price}
    df = pd.DataFrame(d)
    print(df)
    x = np.array(p_sname)
    y = np.array(p_price)
    plt.bar(x, y)
    plt.show()
    df.to_csv('deals.csv')
# ----------------------------------------------------------------------------------------------------------------------------
def diabetes_check(name, age, gender):
    while True:
        try:
            m_data = pd.read_csv("diabetes.csv")
            inp = m_data.drop(columns=['prediction'])
            output = m_data['prediction']
            model = DecisionTreeClassifier()
            model.fit(inp.values, output)
            if gender != "F":
                np =0
            else:
                np = int(input("Please enter your NUMBER OF PREGNANCIES: "))
            g = int(input("Please enter your GLUCOSE LEVEL: "))
            bp = int(input("Please enter your BLOOD PRESSURE (DIASTOLIC): "))
            sf = int(input("Please enter your SKIN FOLD: "))
            bmi = float(input("Please enter your BMI [Don't know your BMI? Enter '-1']: "))
            if bmi == -1:
                mass=float(input("Enter your numeric weight (in kilograms): "))
                height=float(input("Enter you numeric height (in metres): "))
                bmi=((mass)/(height)**2)
            predict = model.predict([[np, g, bp, sf, bmi, age]])
            if predict[0] == "yes":
                print("Hello", name+",", "you seem to be\
 PRONE to diabetes! Consult your GP at earliest.")
                print()
            else:
                print("Hello", name+",", "you are WELL OFF\
 at present! But do not forget to take care of your health.")
                print()
            chk=input("Want to re-use the diabetes predictor? (y/n): ")
            if chk=="Y" or chk=="y":
                print()
                continue
            else:
                break
        except ValueError:
            print("Invalid input! Enter numerical value only...")
            print()
# ----------------------------------------------------------------------------------------------------------------------------
def user_records(data:list):
    header=["User Name", "Age", "Gender", "Contact number", "Options used"]
    datafile=r"Customer_Records.csv"
    try: 
        with open(datafile, "r", newline=None) as recfile:
            chkrow=recfile.read()
            chkrow=chkrow.split("\n")[1].split(",")
            if header!=chkrow:
                data=[header]+[data]
            else:
                data=[data]
            recfile.close()
    except Exception:
        pass
    try:
        with open(datafile, "a", newline="") as recfile:
            f_writer=csv.writer(recfile)
            f_writer.writerows(data)
            recfile.close()
    except Exception:
        pass

