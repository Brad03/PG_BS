import pyautogui as pg
import webbrowser

answer = pg.confirm(text="Which book do you need to read?", title="Choose your book", buttons=['Of Mice and Men','To Kill a Mockingbird','Black Like Me'])

if answer == "Of Mice and Men":
    webbrowser.open("http://nisbah.com/summer_reading/ff_mice_and_men_steinbeck.pdf")

elif answer == "To Kill a Mockingbird":
    webbrowser.open("https://docs.google.com/viewer?a=v&pid=sites&srcid=YW5udXJpc2xhbWljc2Nob29sLm9yZ3xzaXN0ZXIta2F0ZWx5bnxneDo2NjVmZmE1NzNjNjc4NWM")

elif answer == "Black Like Me":
    webbrowser.open("https://www.westada.org/cms/lib8/ID01904074/Centricity/Domain/3984/blacklikeme_TEXT_.pdf")
