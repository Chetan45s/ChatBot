from sys import stdout
from time import sleep
import random

neg = ['bad','sad','depressed','stressed','stress','depress']
stoppers = ['yeah','ok','fine','yep','yes']
pos = ['good','happy','cool','fine']
greeting_r = ['how are you','what about you','and you','you']
bye = ['bye','See you later']
excitment = ['excit','exicted']
dataset = {'Oh! Its not good then':neg,'Cool!':pos}
dataset_1 = {'You shoudd be. lol!':excitment,'Cool!':pos}
first = ['bollywood','hollywood']
second = ['java','c++','python','js','javascript']
third = ['development','problem solving']
weird = ['Write properly','Write again','Check again']

def is_valid(data,db):
    while data not in db:
        if data not in db:
            rand_idx = random.randrange(len(weird)) 
            random_str = weird[rand_idx]
            write(random_str)
            user = read()
            data = user[0]
        else:
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
        sleep(0.1)
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
    read()
    write("Oh! Its not good then")
    read()
    word_phrase = f"For avoiding {word} feeling I suggest you to take some meditation"
    write(word_phrase)
    write("Leave this and lets talk about you")
    read()
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
        for check_name in range(1,len(user)):
            if user[check_name-1] == 'is' or user[check_name-1] == 'am':
                Name = user[check_name] + " "
        write(f"ok {Name}")
    write("Lets Play a Rapid Fire Game. First I will ask then you can I you wish")
    read()
    write("Lets Start.")
    write("Bollywood or Hollywood")
    user = read()
    is_valid(user[0],first)
    write("Java, Python, C++, JavaScript")
    user = read()
    lang = is_valid(user[0],second)
    write("Development or Problem Solving")
    user = read()
    interest = is_valid(user[0],third)
    write("Cricket or Football")
    is_valid(user[0],['cricket','football'])
    write("What if someone pays you to do murder of a murderer")
    read()
    write("Nicely played now you can ask me")
    chat_2()
    run = False
    return Name,lang,interest,run


def main():
    write("Hello! Human. Lets chat and discuss.")
    read()
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
            write("Sorry! I can't understand. If you want to end this conversation you can just say bye")   
        else:
            print("----------- Summary ------------")
            if Name is not "Human":
                print(f"Name of the user : {Name}")
            print("Instered in : ",interest)
            print("Language : ", lang)
            return

    
if __name__ == "__main__":
    main()