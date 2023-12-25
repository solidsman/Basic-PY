print(" █     █░▓█████  ██▓     ▄████▄   ▒█████   ███▄ ▄███▓▓█████    ▄▄▄█████▓ ▒█████      ▄████▄   ▒█████  ▓█████▄ ")
print("▓█░ █ ░█░▓█   ▀ ▓██▒    ▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓█   ▀    ▓  ██▒ ▓▒▒██▒  ██▒   ▒██▀ ▀█  ▒██▒  ██▒▒██▀ ██▌")
print("▒█░ █ ░█ ▒███   ▒██░    ▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▒███      ▒ ▓██░ ▒░▒██░  ██▒   ▒▓█    ▄ ▒██░  ██▒░██   █▌")
print("░█░ █ ░█ ▒▓█  ▄ ▒██░    ▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒▓█  ▄    ░ ▓██▓ ░ ▒██   ██░   ▒▓▓▄ ▄██▒▒██   ██░░▓█▄   ▌")
print("░░██▒██▓ ░▒████▒░██████▒▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒░▒████▒     ▒██▒ ░ ░ ████▓▒░   ▒ ▓███▀ ░░ ████▓▒░░▒████▓ ")
print("░ ▓░▒ ▒  ░░ ▒░ ░░ ▒░▓  ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░░ ▒░ ░     ▒ ░░   ░ ▒░▒░▒░    ░ ░▒ ▒  ░░ ▒░▒░▒░  ▒▒▓  ▒ ")
print("  ▒ ░ ░   ░ ░  ░░ ░ ▒  ░  ░  ▒     ░ ▒ ▒░ ░  ░      ░ ░ ░  ░       ░      ░ ▒ ▒░      ░  ▒     ░ ▒ ▒░  ░ ▒  ▒ ")
print("  ░   ░     ░     ░ ░   ░        ░ ░ ░ ▒  ░      ░      ░        ░      ░ ░ ░ ▒     ░        ░ ░ ░ ▒   ░ ░  ░ ")
print("    ░       ░  ░    ░  ░░ ░          ░ ░         ░      ░  ░                ░ ░     ░ ░          ░ ░     ░    ")
print("                        ░                                                           ░                  ░      ")

start = input("Do you agree to Continue the offer (y/n): ")
if start == "y":
    print("|  |  ___       __   __         ___  ")
    print("|  | |__  |    /  ` /  \  |\/| |__   ")
    print("|/\| |___ |___ \__, \__/  |  | |___  ")
else:
    quit()


def login():
    login_q = ['Enter your full name: ', 'Enter your refrence number: ']
    login_ans = []
    for confirm in login_q:
        login_ans.append(input(confirm))
        print(login_ans)
login()



score = int(input('what is your score: '))
if score >= 1000:
    s = "Squad"
elif score >= 4000:
    s = "pro"
elif score >= 10000:
    s = "Master"
else:
    s = "Lieutenant"

print("score : ", s)

print("There is a new offer with special skins")

while True:
    import random

    print("Welcome to Skin Draw !")
    print("just give you luck (PRESS ENTER)")
    input()
    skin = random.randint(1, 10)
    if skin == 1:
        print("Type 25 - Geometry")
    if skin == 2:
        print("Cordite- Zero-G")
    if skin == 3:
        print("ASM-10 Plasma")
    if skin == 4:
        print("GKS - Tactical Unicorn")
    if skin == 5:
        print("HG 40's Ghoul Bound ")
    if skin == 6:
        print("AK117's Platinum Raider ")
    if skin == 7:
        print("Thumper's Surprise Party skin")
    if skin == 8:
        print("CR-56 AMAX – Red Death.")
    if skin == 9:
        print("Locus – Neptune.")
    if skin == 10:
        print("GKS – Tactical Unicorn.")
