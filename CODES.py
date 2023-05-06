#list and tuples tutorial
# index(+) = 0 1 2 ascending // index(-) = -1 -2 -3 descending
#to specify list [:5] [5:] [1:5] last is excluded
#to assign list  games[2]="mobile legends"
#to see lenght print(len(games))
#to see count print(games.count("subway surfer"))
#games.append("sim city")
#games.insert(0,"sim city")
#games.remove("subway surfer")
#games.pop(4)
#del list[0] del list
#games.clear()
#games2 =games.copy
#combining list
#games.append(sports)
#games.reverse()
#games.sort() games.sort(reverse=True)
#nested list- a list inside a list ["list1","list2"["anotherlist"]] print(list[2])
#TUPLES
#tuples uses parenthesis ( ) list uses [ ]
#casting or convert tuples(list) list(tuples)
#
games =["cod","ml","coc","subway surfer","plant vs zombies","league of legends","2021","bleacher report","nba","fifa","rugby","voleyball"]
sports =["basketball","volleyball","football","soccer","tennis","boxing"]
games.append("sim city")
games.insert(5,"sim city")
games.pop(4)
games2 =games.copy
combination =games + sports
games.append(sports)
sports.sort()
print(games)