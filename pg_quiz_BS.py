import pyautogui as pg
import time
import webbrowser

points = 0


# Question 1

answer = pg.prompt(
"""
Which would you rather play?

a) Fortnite Battle Royale
b) Call of Duty
c) Destiny
d) Star Wars Battlefront

"""
    )

# Give points

if answer == "a":
        points += 1
elif answer == "b":
        points += 2
elif answer == "c":
        points += 3
elif answer == "d":
        points += 4


# Question 2

answer = pg.prompt(
"""
Where would you rather go?

a) Titled Towers
b) Retail Row
c) Loot Lake
d) Fatal Fields

"""
    )

# Give points

if answer == "a":
        points += 1
elif answer == "b":
        points += 2
elif answer == "c":
        points += 3
elif answer == "d":
        points += 4

# Question 3

answer = pg.prompt(
"""
What do you do in your free time?

a) Play video games
b) Sleep
c) Play Outside
d) Read

"""
    )

# Give points

if answer == "a":
        points += 1
elif answer == "b":
        points += 2
elif answer == "c":
        points += 3
elif answer == "d":
        points += 4

# Question 4

answer = pg.prompt(
"""
Which gun do you prefer?

a) Sniper
b) Shotgun
c) AR
d) SMG

"""
    )

# Give points

if answer == "a":
        points += 1
elif answer == "b":
        points += 2
elif answer == "c":
        points += 3
elif answer == "d":
        points += 4


#END OF SURVEY

pg.alert("You are...")

# Black Knight
if points < 8:
        pg.alert("Black Knight")
        webbrowser.open("http://orcz.com/images/thumb/2/26/FortniteBattleRoyaleBlackKnight.jpg/400px-FortniteBattleRoyaleBlackKnight.jpg")
# Raptor
if points >= 8 and points < 12:
        pg.alert("Raptor")
        webbrowser.open("https://i.imgur.com/Ip1VmLD.jpg")
# Red Knight
if points >= 12 and points < 16:
        pg.alert("Red Knight")
        webbrowser.open("https://www.stormshield.one/images/items/cid_034_athena_commando_f_medieval.png")
# Funk Ops
if points >=16:
        pg.alert("Funk Ops")
        webbrowser.open("http://orcz.com/images/c/c5/FortniteBattleRoyaleFunkOps.jpg")
