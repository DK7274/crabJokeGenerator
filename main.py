from guizero import *
import random
app = App("CrabJokes")
app.bg = "red"
punchDict = {
    1: "crimes",
    2: "murder",
    3: "crabs",
    4: "he broke the claw",
    5:"he had a knife"
}
def crabGen():
    joke = Text(app, text="Why did the crab go to jail? " + punchDict[random.randint(1,5)])
    print("amogus")
message = Text(app,text="Welcome to crab jokes generator!")
button = PushButton(app,text="generate crab joke",command = crabGen)
app.display()