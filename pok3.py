# TODO json dostat do pythonu, načítať do rozumnej štruktúry

# url lib 123, request = kniznice na stahovanie suborov z netu
# https://raw.githubusercontent.com/yorkcshub/Miscellanous/master/effectiveness.json

import requests
import json
import random

attacks = {}

translated = {"super effective": 2, "normal effective": 1, "not very effective": 0.5, "no effect": 0}

data = requests.get("https://raw.githubusercontent.com/yorkcshub/Miscellanous/master/effectiveness.json")
# print(data.text)
data_json = json.loads(data.text)

# for i in data_json:
# print(i,data_json[i])


for power in data_json:  # prechaza "skodlivost"
    for attacker in data_json[power]:  # "prechaza utocnikov
        temp = attacks.get(attacker, {})  # do zoznamu pripadi utockika a k nemu prazdny list
        for defender in data_json[power][attacker]:  # prechaza values pre daneho utocnika
            temp[defender] = translated[power]  # do premennej priradi value
        attacks[attacker] = temp  # premennu priradi ku key

print(attacks)

def attack(n1, n2, list_pok):
    list_pok = list_pok.split(",")
    team1 = []
    team2 = []
    team1_points = 0
    team2_points = 0
    temp = 0
    for pt1 in range(0, n1):
        team1.append(list_pok[pt1])
    for pt2 in range(n1, len(list_pok)):
        team2.append(list_pok[pt2])
    for pok_team_1 in team1: #prechadza prvy team
        pok_team_1 = pok_team_1.split(" ")
        for pok_team_2 in team2: #prechadza 2 team
            pok_team_2 = pok_team_2.split()
            if len(pok_team_1)>1 and len(pok_team_2) == 1: #ak je v t1 2zlozkovy pokemon
                if attacks[pok_team_1[0]][pok_team_2[0]]>attacks[pok_team_1[1]][pok_team_2[0]]:
                    team1_points+=attacks[pok_team_1[0]][pok_team_2[0]]
                else:
                    team1_points += attacks[pok_team_1[1]][pok_team_2[0]] #vyriesene body pre t1
                team2_points+= attacks[pok_team_2[0]][pok_team_1[0]]*attacks[pok_team_2[0]][pok_team_1[1]] #vyriesene body pre t2

            elif len(pok_team_1)>1 and len(pok_team_2)>1: #ak su oba dvojzlozkove
                if attacks[pok_team_1[0]][pok_team_2[0]]*attacks[pok_team_1[0]][pok_team_2[1]] >attacks[pok_team_1[1]][pok_team_2[0]]*attacks[pok_team_1[1]][pok_team_2[1]]:
                    team1_points+=attacks[pok_team_1[0]][pok_team_2[0]]*attacks[pok_team_1[0]][pok_team_2[1]]
                else:
                    team1_points += attacks[pok_team_1[1]][pok_team_2[0]]*attacks[pok_team_1[1]][pok_team_2[1]] #vyriesene body pre t1
                if attacks[pok_team_2[0]][pok_team_1[0]]*attacks[pok_team_2[0]][pok_team_1[1]]>attacks[pok_team_2[1]][pok_team_1[0]]*attacks[pok_team_2[1]][pok_team_1[1]]:
                    team2_points+=attacks[pok_team_2[0]][pok_team_1[0]]*attacks[pok_team_2[0]][pok_team_1[1]]
                else:
                    team2_points+=attacks[pok_team_2[1]][pok_team_1[0]]*attacks[pok_team_2[1]][pok_team_1[1]] #vyriesene body pre t2

            elif len(pok_team_1) == 1 and len(pok_team_2)>1:
                if attacks[pok_team_2[0]][pok_team_1[0]] > attacks[pok_team_2[1]][pok_team_1[0]]:
                    team2_points += attacks[pok_team_2[0]][pok_team_1[0]]
                else:
                    team2_points += attacks[pok_team_2[1]][pok_team_1[0]]  # vyriesene body pre t2
                team1_points += attacks[pok_team_1[0]][pok_team_2[0]] * attacks[pok_team_1[0]][pok_team_2[1]]  # vyriesene body pre t2

            elif len(pok_team_1)== 1 and len(pok_team_2) == 1:
                team1_points +=  attacks[pok_team_1[0]][pok_team_2[0]]
                team2_points +=  attacks[pok_team_2[0]][pok_team_1[0]]

    if team1_points>team2_points:
        print(f"{team1_points},{team2_points},ME")
    elif team1_points<team2_points:
        print(f"{team1_points},{team2_points},FOE")
    else:
        print(f"{team1_points},{team2_points},EQUAL")


print(attack(2, 6, "Psychic Dark,Fire,Ghost Ice,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug"))