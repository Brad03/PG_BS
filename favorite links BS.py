import pyautogui as pg
import webbrowser

videos = ["https://www.youtube.com/watch?v=hgCP30cepwA", "https://www.youtube.com/watch?v=XzVWTk-Bg3M"]

music = ["https://soundcloud.com/", "https://www.spotify.com/us/"]

answer = pg.prompt(
"""
Which would you rather do?
a) Watch videos
b) Listen to music

"""
    )

if answer == "a":
    for i in videos:
        webbrowser.open(i)
elif answer == "b":
    for i in music:
        webbrowser.open(i)
