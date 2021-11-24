import json

import random
import requests
from datetime import datetime
import subprocess as sp
import config

# import ctypes

base_url = "https://discord.com/api/v9/"
token = config.token
header = {'authorization': f'{token}'}
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


def find_winner(chid: int, mid: int, emoji: str) -> list:
    reactions = []
    url = f"{base_url}channels/{chid}/messages/{mid}/reactions/{emoji}?limit=100"
    while True:
        r = requests.get(url=url, headers=header)
        if not r.ok:
            raise Exception(f"Ungültiger Datensatz (Debug: {r}, {r.text})")
        reactions += json.loads(r.text)
        if len(json.loads(r.text)) == 100:
            url = f"{base_url}channels/{chid}/messages/{mid}/reactions/{emoji}?limit=100&after={reactions[-1]['id']}"
        else:
            break
    print(f"Teilnehmer {len(reactions)}:")
    with open("output.txt", "w", encoding="UTF-8") as f:
        for i, j in enumerate(reactions):
            #print(f"{i}. {j['username']}#{j['discriminator']} ({j['id']})")
            # Gives the Output in a TXT file
            print(f"{i + 1}. {j['username']}#{j['discriminator']} ({j['id']})", file=f)
    winnerslist = []
    for i in range(int(aGewinner)):
        try:
            u = random.choice(reactions)
        except IndexError:
            print("Es gibt mehr Gewinner als Reaktionen.")
            break
        winnerslist.append(f"{u['username']}#{u['discriminator']} <@{u['id']}>\n")
        reactions.remove(u)
    return winnerslist
    # return f"{u['username']}#{u['discriminator']} <@{u['id']}>"


def write_file():
    file = open("Gewinner.txt", "w", encoding="UTF-8")
    file.write(gTitle + "\n")
    file.write("Die Gewinner wurden ausgelost. \n\n")
    file.write("Vielen Dank an alle die an dem Gewinnspiel teilgenommen haben.\n\n")
    file.write(f"Zeitpunkt der Auslosung: {dt_string}\n\n")
    f = open("output.txt", "r", encoding="UTF-8")
    file.write(f"Es haben folgende Teilnehmer am Giveaway teilgenommen:\n{''.join(f.readlines())}")
    f.close()
    file.write(f"\nEs hat gewonnen:\n{''.join(winner)}")
    file.write(f"Du hast ** {timeR} Minuten ** zeit um dich bei mir via PM zu melden.\n")
    file.write("Sollte sich der Gewinner nicht rechtzeitig melden, wird der Gewinn erneut ausgelost")
    file.close()


# def Mbox(title, text, style):
#     return ctypes.windll.user32.MessageBoxW(0, text, title, style)


if __name__ == "__main__":
    _chid = input("Bitte gib die Channel ID an\n>")
    _mid = input("Bitte gib die Message ID an\n>")
    _emoji = input("Bitte gib das Emoji an, das gewertet werden soll\n>")
    timeR = input("Bitte gib die Zeit an, bis sich der Gewinner melden muss (bsp: 5 Min)\n")
    gTitle = input("Bitte gib an, wie das Gewinnspiel heißt\n")
    aGewinner = input("Bitte gib an wieviele Gewinner es geben soll\n")
    winner = find_winner(int(_chid), int(_mid), _emoji, )
    # print(f"\nDatum der Ziehung:  {dt_string}")
    # print(f"\nDer Gewinner ist {winner}")
    print("Ziehung erfolgreich ausgeführt! Der Gewinntext wird dir im Editor ausgegeben")

    write_file()

    # f = open("Gewinner.txt", "r", encoding="UTF-8")
    # Mbox('Winner',f"{f.read()}", 6)
    # f.close()

    programmName = "notepad.exe"
    fileName = "Gewinner.txt"
    sp.Popen([programmName, fileName])
