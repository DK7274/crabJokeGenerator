from guizero import *
import random
app = App("CrabJokes")
app.bg = "red"
punchDict = {
    1: "Crimes",
    2: "Murder",
    3: "Crabs",
    4: "He broke the claw",
    5:"He had a knife",
    6:"I put him there",
    7:"International drug smuggling",
    8:"Aggravated assault",
    9:"Money Laundering",
    10:"Fraud",
    11:"Because it didn't",
    12:"Homicide",
    13:"Tax Evasion",
    14:"Viewed moose from the air"
}
def crabGen():
    joke = Text(app, text="Why did the crab go to jail? " + punchDict[random.randint(1,14)])
    print("amogus")
message = Text(app,text="Welcome to crab jokes generator!")
button = PushButton(app,text="generate crab joke",command = crabGen)
app.display()