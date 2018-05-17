import webbrowser

name = "Brad"

subjects = ["English", "Spanish", "Math", "History", "Science"]

print("Hello " + name)

for i in subjects:
    print("One of my classes is " + i)
videogames = ["Fortnite", "Call of Duty", "Destiny", "Overwatch", "Star Wars Battlefront"]

for i in videogames:
    if i == "Fortnite":
        print( i + " is currently the best game in the world.")
    elif i == "Call of Duty":
        print(i + " has seen better days.")
    elif i == "Overwatch":
        print( i + " is not fun.")
    else:
        print("One of the best games in the world is " + i)

movies = []

while True:
    print("What is a movie you like? Type 'end' to quit.")
    answer = input()
    if answer == "end":
        break
    else:
        movies.append(answer)

for i in movies:
    print("One of your favorites is " + i)
    webbrowser.open(i)
