class Votes:
  def __init__(self, name, age, votes, party):
    self.name = name
    self.age = age
    self.votes = votes
    self.party = party

scott = Votes("Scott","26", 0, "Elephantial Party")
steve = Votes("Steven", "36", 0, "Workers Party")
max = Votes("Max", "13", 0, "Slave Party")
rene = Votes("Rene", "29", 0, "Rene Party")

can = [scott, steve, max, rene]

x = True

def info():
    for i in can:
        print(i.name,"| Age:",i.age,"| Votes:",i.votes,"| Party:",i.party)

while x:
    z = input("Enter a vote: (Scott [0], Steve [1], Max [2], Rene [3]) | Type 'i' for information | Type 'x' once done: ")
    if z == "i":
        info()
    elif z == "x":
        print("\n\n\n")
        info()
        print("\n\n\n")
        x = False
    else:
        z = int(z)
        can[z].votes += 1
