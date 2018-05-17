import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.speak("What is your name?")
answer = pg.prompt("Enter your name.")

if answer == "Brad":
    speak.speak ("Hello " + answer + " nice to meet you.")

elif answer == "Luke":
    speak.speak ("Hello " + answer + "I am your father.")

else:
    speak.speak("Nice to meet you, " + answer)

speak.speak("What is your Favorite game?")
game = pg.prompt("Enter your favorite game.")

if game == "Fortnite":
    speak.speak("Stop watching Fortnite videos during school!")
    wb.open("https://www.youtube.com/results?search_query="+game)
else:
    speak.speak("I also like to play " + game + "." + " Lets watch a video about" + game + ".")
    wb.open("https://www.youtube.com/results?search_query=" +game)
