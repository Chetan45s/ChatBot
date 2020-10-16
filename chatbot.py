from sys import stdout
from time import sleep
import random

neg = ['bad','sad','depressed','stressed','stress','depress']
stoppers = ['yeah','ok','fine','yep','yes']
pos = ['good','happy','cool','fine']
bye = ['bye','See you later']
no = ['no','nope','nothing']
hey = ['hey','hi','hello']
dataset = {'Oh! Its not good then':neg,'Cool!':pos}

first = ['bollywood','hollywood']
second = ['java','c++','python','js','javascript']
third = ['development','problem']
forth = ['cricket','football']

weird = ['Write properly','Write again','Check again','spell it properly']

def is_valid(data,db):
    while data not in db:
        if data not in db:
            rand_idx = random.randrange(len(weird)) 
            random_str = weird[rand_idx]
            write(random_str)
            user = read()
            data = user[0]    
    return data

def chat_2():
    while True:
        user = read()
        for check in bye:
            if user[0] == check:
                return
        user = " ".join(user)
        ans = list(user.split(" or "))
        rand_idx = random.randrange(len(ans))
        random_str = ans[rand_idx]
        write(random_str)

def read():
    user = str(input("- You : "))
    user = user.lower()
    user = list(user.split(" "))
    return user

def write(response):
    li = list(response.split(" "))
    store = "- Bot : "
    for out in li:
        store += out + " "
        stdout.write("\r%s" % store)
        stdout.flush()
        sleep(0.3)
    stdout.write("\n")

def check_stoppers(response):
    if len(response) > 1:
        return False
    else:
        if response[0] in stoppers:
            return True

def neg_discuss(word):
    word_phrase = f"Why are you feeling so {word}. Anything happened ?"
    write(word_phrase)
    user = read()
    if user[0] not in no:
        write("Oh! Its not good then")
        read()
    word_phrase = f"For avoiding {word} feeling I suggest you to take some meditation\n.\n."
    write(word_phrase)
    write("Leave this and lets talk about you")
    user = read()
    is_valid(user[0],stoppers)  
    Name,lang,interest,run = pos_discuss()
    return Name,lang,interest,run

def pos_discuss():
    Name = "Human"
    write("Its weird to call you Human. Can I call by your real name ?")
    user = read()
    if check_stoppers(user):
        write("What is your name then ?")
        user = read()
        Name = user[0]
        write(f"ok {Name}")
    elif user[0] == 'no' or user[0] == 'nope':
        write("Ok Fine but it's kind of rude")
    else:
        Name = user[0]
        for check_name in range(1,len(user)):
            if user[check_name-1] == 'is' or user[check_name-1] == 'am':
                Name = user[check_name] + " "
        write(f"ok {Name}")

    # here we start the game
    write("Lets Play a Rapid Fire Game. First I will ask then you can If you wish")
    read()
    write("Lets Start.")

    # First Question
    write("Bollywood or Hollywood")
    user = read()
    is_valid(user[0],first)   # check whether user input the right value or not. If not then will ask again to enter valid input

    # Second question as part of data collection
    write("Java, Python, C++, JavaScript")
    user = read()
    lang = is_valid(user[0],second)

    # third question as part of data collection
    write("Development or Problem Solving")
    user = read()
    interest = is_valid(user[0],third)

    write("Cricket or Football")
    user = read()
    is_valid(user[0],forth)

    write("What if someone pays you to do murder of a murderer")
    read()

    write("Nicely played now you can ask me")
    chat_2()

    run = False
    return Name,lang,interest,run

def main():
    write("Hello! Human. Lets chat and discuss.")
    user = read()
    is_valid(user[0],hey)
    write("How are you ?")
    chat()

def chat():
    while True:
        run = True
        user = read() 
        for one,one1 in dataset.items():
            for two in one1:
                for three in user:
                    if three == two:
                        if 'bad' in one1:
                            Name,lang,interest,run = neg_discuss(three)
                        elif 'good' in one1:
                            Name,lang,interest,run = pos_discuss()
                        else:
                            write("Sorry! I can't understand")
        if run:
            user = " ".join(user)
            if user in bye:
                break
            else:
                write("Sorry! I can't understand. If you want to end this conversation you can just say bye")   
        else:
            write("----------- Summary ------------")
            if Name is not "Human":
                write(f"Name of the user : {Name}")
            write(f"Instered in : {interest}")
            write(f"Language : {lang}")
            return
    
if __name__ == "__main__":
    main()