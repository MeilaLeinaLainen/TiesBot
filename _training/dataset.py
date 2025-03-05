import os

def meilaleinalainen():
    names = ["tieskey7", "pbac742", "syne314", "silliestsophie", "spankiepankie", "n1kani", "Dyno", "nixxcore", "sanneee", ]
    user = "meilaleinalainen"
    with open(f"{os.getcwd()}\\_training\\data.txt", "r", encoding="utf-8") as file:
        contents = file.readlines()
        for line in contents:
            if f"{user}: " in line:
                line = line.replace(user, "TiesBot")
                print(f"Replaced: '{user}' with 'TiesBot'")

            with open(f"{os.getcwd()}\\_training\\data-{user}.txt", "a", encoding="utf-8") as e:
                e.write(line)
                print(line)

def tieskey():
    user = "tieskey7"
    with open(f"{os.getcwd()}\\_training\\data.txt", "r", encoding="utf-8") as file:
        contents = file.readlines()
        for line in contents:
            if f"{user}: " in line:
                line = line.replace(user, "TiesBot")
                print(f"Replaced: '{user}' with 'TiesBot'")

            with open(f"{os.getcwd()}\\_training\\data-{user}.txt", "a", encoding="utf-8") as e:
                e.write(line)
                print(line)

def pbac742():
    user = "pbac742"
    with open(f"{os.getcwd()}\\_training\\data.txt", "r", encoding="utf-8") as file:
        contents = file.readlines()
        for line in contents:
            if f"{user}: " in line:
                line = line.replace(user, "TiesBot")
                print(f"Replaced: '{user}' with 'TiesBot'")

            with open(f"{os.getcwd()}\\_training\\data-{user}.txt", "a", encoding="utf-8") as e:
                e.write(line)
                print(line)

def nixxcore():
    user = "nixxcore"
    with open(f"{os.getcwd()}\\_training\\data.txt", "r", encoding="utf-8") as file:
        contents = file.readlines()
        for line in contents:
            if f"{user}: " in line:
                line = line.replace(user, "TiesBot")
                print(f"Replaced: '{user}' with 'TiesBot'")

            with open(f"{os.getcwd()}\\_training\\data-{user}.txt", "a", encoding="utf-8") as e:
                e.write(line)
                print(line)

def syne314():
    user = "syne314"
    with open(f"{os.getcwd()}\\_training\\data.txt", "r", encoding="utf-8") as file:
        contents = file.readlines()
        for line in contents:
            if f"{user}: " in line:
                line = line.replace(user, "TiesBot")
                print(f"Replaced: '{user}' with 'TiesBot'")

            with open(f"{os.getcwd()}\\_training\\data-{user}.txt", "a", encoding="utf-8") as e:
                e.write(line)
                print(line)

def sanneee():
    user = "sanneee"
    with open(f"{os.getcwd()}\\_training\\data.txt", "r", encoding="utf-8") as file:
        contents = file.readlines()
        for line in contents:
            if f"{user}: " in line:
                line = line.replace(user, "TiesBot")
                print(f"Replaced: '{user}' with 'TiesBot'")

            with open(f"{os.getcwd()}\\_training\\data-{user}.txt", "a", encoding="utf-8") as e:
                e.write(line)
                print(line)

def americantruth():
    user = "americantruth"
    with open(f"{os.getcwd()}\\_training\\data.txt", "r", encoding="utf-8") as file:
        contents = file.readlines()
        for line in contents:
            if f"{user}: " in line:
                line = line.replace(user, "TiesBot")
                print(f"Replaced: '{user}' with 'TiesBot'")

            with open(f"{os.getcwd()}\\_training\\data-{user}.txt", "a", encoding="utf-8") as e:
                e.write(line)
                print(line)

def n1kani():
    user = "n1kani"
    with open(f"{os.getcwd()}\\_training\\data.txt", "r", encoding="utf-8") as file:
        contents = file.readlines()
        for line in contents:
            if f"{user}: " in line:
                line = line.replace(user, "TiesBot")
                print(f"Replaced: '{user}' with 'TiesBot'")

            with open(f"{os.getcwd()}\\_training\\data-{user}.txt", "a", encoding="utf-8") as e:
                e.write(line)
                print(line)

def hybrid1():
    users_to_replace = ["meilaleinalainen", "tieskey7", "nixxcore", "sanneee"]

    with open(f"{os.getcwd()}\\_training\\data.txt", "r", encoding="utf-8") as input_file:
        for line in input_file:
            user_name = line.split(":")[0].strip()
            
            if user_name in users_to_replace:
                line = line.replace(user_name, "TiesBot")
            
            with open(f"{os.getcwd()}\\_training\\data-hybrid.txt", "a", encoding="utf-8") as output_file:
                output_file.write(line)
                print(line)

def iterate():
     with open(f"{os.getcwd()}\\_training\\data.txt", "r", encoding="utf-8") as file:
        contents = file.readlines()
        write_user = True
        
        with open(f"{os.getcwd()}\\_training\\data-altered.txt", "a", encoding="utf-8") as e:
            for line in contents:
                if ": " in line:
                    line = line.split(": ", 1)[1] 
                    line = f"User: {line}" if write_user else f"TiesBot: {line}"
                
                e.write(line)
                print(f"Written: {('User' if write_user else 'TiesBot')}: {line.strip()}")
                
                # Toggle between User and TiesBot for the next line
                write_user = not write_user

#meilaleinalainen()
#tieskey()
#pbac742()
#nixxcore()
#syne314()
#sanneee()
#americantruth()
#n1kani()
#hybrid1()
iterate()

import re

txt_file_path = f'{os.getcwd()}\\_training\\data-hybrid.txt'

with open(txt_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

cleaned_lines = []
for line in lines:
    line = re.sub(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} ", "", line)
    
    username = re.match(r"^[^:]+: ", line)
    if username:
        line = line[len(username.group(0)):]  # remove username
    
    cleaned_lines.append(line.strip())

conversation = []
for i in range(0, len(cleaned_lines), 2):
    user_message = f"User: {cleaned_lines[i]}"
    bot_message = f"Bot: {cleaned_lines[i + 1]}" if i + 1 < len(cleaned_lines) else ""
    conversation.append(f"{user_message}\n{bot_message}")

formatted_conversation = "\n".join(conversation)

with open('processed_conversation.txt', 'w', encoding='utf-8') as file:
    file.write(formatted_conversation)
