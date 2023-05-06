class nbaprofile:
    def __init__(self,team,name,position,age,intro):
        self.team = team
        self.name = name
        self.position = position
        self.age = age
        self.intro = intro
    print("**NBA PLAYOFFS STARS PER TEAM**\n")
    def profile(self):
        print(self.intro)
    def profile2(self):
        print("TEAM: " + self.team)
        print("NAME: " + self.name)
        print("POSITION: " + self.position)
        print("AGE: " + str(self.age))
LACprofile = nbaprofile("Los Angeles Clippers ","Paul George","Shooting Guard", 33,"--PLAYER PROFILE 1--")
GSWprofile = nbaprofile("Golden State Warriors","Steph Curry","Point Guard",31,"--PLAYER PROFILE 2--")
DALprofile = nbaprofile("Dallas Mavericks","Luka Doncic","Point Guard",24, "--PLAYER PROFILE 3--")
DENprofile = nbaprofile("Denver Nuggets","Nikola Jokic","Center",28,"--PLAYER PROFILE 4--")
PHXprofile = nbaprofile("Phoenix Suns","Devin Booker","Shooting Guard",26,"--PLAYER PROFILE 5--")
MEMprofile = nbaprofile("Memphis Grizzlies","Ja Morant","Point Guard",23,"--PLAYER PROFILE 6--")
LALprofile = nbaprofile("Los Angeles Lakers","Anthony Davis","Center",30,"--PLAYER PROFILE 7--")
SACprofile = nbaprofile("Sacramento Kings","Domantas Sabonis","Center",27,"--PLAYER PROFILE 8--")
LACprofile.profile()
LACprofile.profile2()
GSWprofile.profile()
GSWprofile.profile2()
DALprofile.profile()
DALprofile.profile2()
DENprofile.profile()
DENprofile.profile2()
PHXprofile.profile()
PHXprofile.profile2()
MEMprofile.profile()
MEMprofile.profile2()
LALprofile.profile()
LALprofile.profile2()
SACprofile.profile()
SACprofile.profile2()