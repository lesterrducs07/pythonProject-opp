# class Character:
#     def __init__(self,name,team,position):
#         self.name = name
#         self.team = team
#         self.position = position
# charOne = Character("Westbrook","LA Clippers","Point Guard")
# print(charOne.name)
# print(charOne.team)







# class Character:
#     def __init__(self,name,gender,age):
#         self.name = name
#         self.gender = gender
#         self.age = age
# charOne = Character("Lester","Male",28)
# print(charOne.name)
# print(charOne.gender)
#




#
# class laclippers:
#     def __init__(self,name,position,playstyle):
#         self.name = name
#         self.position = position
#         self.playstyle = playstyle
# lac = laclippers("russel","pg","attacker")
# lac2 = laclippers("paul","sg","allaround")
# print(lac.name)
#
#



# class character:
#     name = "name"
#     age = 28
#     gender = "gender"
# hero = character
# hero.name = "Lester"
# hero. gender = "male"
# print(hero.name)
# print(hero.gender)

# class nba:
#     def __init__(self,name,position,team):
#         self.name = name
#         self.position = position
#         self.team = team
# playerprofile = nba("westbrook","pointguard","laclippers")
# playerprofile2 = nba("curry","pointguard","gswarriors")
# playerprofile3 = nba("harden","shootingguard","76ers")
# print(playerprofile.name)
# print(playerprofile2.name)
# print(playerprofile3.name)
#
# class User:
#     def __init__(self,firstName,lastName,likesCount,friendsName):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.likesCount = likesCount
#         self.friendsName = friendsName
#     def introduce(self):
#         print("Full Name :" + self.firstName+ " " + self.lastName)
#     def count(self):
#         print("Likes     :" + str(self.likesCount))
#         print("Friends   :")
#         for friend in self.friendsName:
#             print("  -" + friend)
#
# aw = User("Lester","Ducil",100,["Russel","Steph"])
# aw2 = User("James","Harden",100000,["Joel Embiid","Tobias Harris"])
#
# aw2.introduce()
# aw2.count()


# class user:
#     def __init__(self,firstName,lastName,likesCount,friendsCount):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.likesCount = likesCount
#         self.friendsCount = friendsCount
#     def introduce(self):
#         print("Hi I am, " + self.firstName + self.lastName)
#     def fullProfile(self):
#         print("Full Name: " + self.firstName + self.lastName)
#         print("Likes    : " + str(self.likesCount))
#         print("Friends  : ")
#         for friend in self.friendsCount:
#             print("    -" + friend)
# profile = user("Lester","Ducil",100,["Marlon","Dann"])
#
# profile.introduce()
# profile.fullProfile()


#
# class user:
#     def __init__(self,firstName,lastName,likesCount,friendsList):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.likesCount = likesCount
#         self.friendsCount = friendsList
#     def introduce(self):
#         print("Hi I am, " + self.firstName, self.lastName)
#     def fullProfile(self):
#         print("Full Name: " + self.firstName + " " + self.lastName)
#         print("Likes Count: " + str(self.likesCount))
#         print("Friends: ")
#         for friend in self.friendsCount:
#             print("   " + friend)
# profile = user("Lester","Ducil",100000,["Marlon Cris","Leo (wala daw syang apelido)","Dann Villaflor","Edgar Guzman"])
#
# profile.introduce()
# profile.fullProfile()
#


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
# class Mother:
#     def __init__(self,firstName,lastName):
#         self.firstName = firstName
#         self.lastName = lastName
#     def greet(self):
#         print("Hi!!, " + self.firstName + self.lastName)
#
# class Father(Mother):
#     def __init__(self,firstName,lastName,middleName):
#         super().__init__(firstName,lastName)
#         self.middleName = middleName
#     def greet(self):
#         super().greet()
#         print(self.middleName)
#
# class Son(Mother):
#     def __init__(self,firstName,lastName,middleName):
#         super().__init__(firstName,lastName)
#         self.middleName = middleName
#     def greet(self):
#         super().greet()
#         print(self.middleName)
#
# x1 = Mother("Juanita","Ducil")
# x2 = Father("Lucino","Ducil","Barrera")
# x3 = Son("Lester","Ducil","Morales")
#
# x1.greet()
# x2.greet()
# x3.greet()

# class Character:
#     def __init__(self,Name):
#         self.name = Name
#         print("Created by, " + self.name)
# input("Type Something: ")
# pOne = Character("J")

# class Person:
#     def __init__(self,firstName,middleName,lastName):
#         self.firstname = firstName
#         self.middlename = middleName
#         self.lastname = lastName
#
# Player1 = Person("Marlon","Cris","Tabudlong")
# Player2 = Person("Dann","Ml","Villaflor")
# Player3 = Person("Leo","Ml","Austria")
#
# solidGaming = [Player1,Player2,Player3]
# print(solidGaming[0].middlename)








