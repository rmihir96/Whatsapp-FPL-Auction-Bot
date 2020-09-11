# import pandas as pd

# # database = pd.read_csv('FPL.csv')
# # database = database.fillna('')
# # teamid = '1'
# # playername = "Mihir"
# # print(database)

# # if database.loc[database.TeamID == int(teamid), "Players"].values[0]:
# #     database.loc[database.TeamID == int(teamid), "Players"] += ", " + playername
# # else:
# #     database.loc[database.TeamID == int(teamid), "Players"] = playername

# # print(database)
# # table['Players'].fillna('', inplace = True)
# # print(table)
# # newplayer = "AV"
# # price = 30.0
# # teamid = 2





# # print(table.dtypes)
# # table.loc[table.TeamID == 1, "Players"] = list("Mihir"]
# # newlist = table.loc[table.TeamID == 2, "Players"].values[0]

# # if newlist:
# #     print("yes")
# # else:
# #     print("no")
# # print(newlist)
# # if table.loc[table.TeamID == teamid, "Players"].values[0]:
# #     table.loc[table.TeamID == teamid, "Players"] += ", " + newplayer
# # else:
# #     table.loc[table.TeamID == teamid, "Players"] = newplayer
# # table.loc[table.TeamID == teamid, "Budget"] -= price 

# # print(table.loc[table.TeamID == 1, "Owner"].values[0])
# # newlist.append("RV")
# # table.loc[table.TeamID == 1, "Players"] = newlist

# # (table[table['TeamID'] == 1]['Players']) = "Mihir"



# # print(newtable)
# # print(table)
# # table.to_csv('FPL.csv')


# # playerdata['Status'].fillna('unsold', inplace = True)
# # playerdata.to_csv('playerdata.csv')

# # print(type(playerdata['Player']))

# # unsold, sold = [], []
# # for index, row in playerdata.iterrows():
# #     if row['Status'] == "unsold":
# #         unsold.append(row['Player'])
# #     else:
# #         sold.append(row['Player'])
# pid = 5
# # playerdata.loc[playerdata.PID == id, "Status"] = 'sold'
# # print(playerdata)

# playerdata = pd.read_csv('playerdata.csv')
# playerdata.loc[playerdata.PID == pid, "Status"] = 'sold'
# playerdata.to_csv('playerdata.csv', index=False)

# # print(len(sold))
# # print(sold)
# # print(len(unsold))


# print(playerdata)
# # print(unsold)

v1 = "Mihir sold to Team1 for 20\n"
v2 = "Mihir sold to Team2 for 40\n"
# with open("file.txt", "w") as output:
#     output.write(str(values))

# data = open("file.txt", "a")
# data.write(v1)
# data.write(v2)
# data.close()

# f = open("file.txt", "r")
# for line in (f.readlines()):
#     print(line) 