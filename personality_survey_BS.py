print("What's your name?")
name = input()
print("Hello, " + name)



print("What's your favorite color?")
color = input()


if color == "blue":
    print("I love " + color + " too!")
elif color == "green":
    print("Oh, I like green too.")

elif color == "magenta":
    print("That's oddly specific")
else:
    print("I think " + color + " is pretty as well.")


print("What's your favorite subject?")
subject = input()

if subject == "Math":
    print("I love Math too!")



print("What's your favorite TV show?")
tvshow = input()
if tvshow == "The Flash":
    print("I love The Flash also.")
    print("Who's your favorite character?")
    character = input().title()

    if character == "Barry":
        print("The fastest man alive!")
