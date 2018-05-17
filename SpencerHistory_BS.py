import pyautogui as q
import webbrowser


website = ["https://sites.google.com/a/gcds.net/spencer-history-8/welcome"]

textbook = ["https://www.pearsonsuccessnet.com/snpapp/ois/getStudentHomepage.do?newServiceId=6000&newPageId=12100"]

classroom = ["https://classroom.google.com/c/NzUyNjY1MDYwMFpa"]


answer = q.prompt(
    """
Which do you need to access

a) The textbook

b) The Classroom

c)The website

"""

    )

if answer == "a":
    for i in textbook:
        webbrowser.open(i)
elif answer == "b":
    for i in classroom:
        webbrowser.open(i)
elif answer == "c":
    for i in website:
        webbrowser.open(i)
