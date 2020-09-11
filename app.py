from flask import Flask, request
import requests
import pandas as pd
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    database = pd.read_csv('FPL.csv')
    playerdata = pd.read_csv('playerdata.csv')
    # database['Players'].fillna('', inplace = True)
    database = database.fillna('')
    # print(database)

    if 'help' in incoming_msg:
        reply = ("Hello and welcome to the FPL 2020/21 WhatsApp bot!\n\n"
                "You can ask questions like:\n\n"
                "- Team IDs? Command - teamid \n\n"
                "- List of players? Command - playerlist\n\n"
                "- Player Auction Status ? Command - playerstatus-id\n\n"
                "- Team Budget? Command - budget\n\n"
                "- Team Players? Command - teamstatus\n\n"
                "- Player Auctioned? Command - buy-teamid-playerid-playername-price\n\n"
                "- List of Sold players? Command - soldlist\n\n"
                "- List of unsold players? Command - unsoldlist\n\n"
                "- Transactions so far? Command - history\n\n"
                )

        msg.body(reply)
        return str(resp)
    
    if 'soldlist' == incoming_msg:
        sold = ""
        for index, row in playerdata.iterrows():
            if row['Status'] == "sold":
                 sold += str(row['PID']) + " - " + row['Player'] + "\n"
        msg.body(sold)
        return str(resp)
    
    if 'unsoldlist' == incoming_msg:
        unsold = ""
        for index, row in playerdata.iterrows():
            if row['Status'] == "unsold":
                unsold += str(row['PID']) + " - " + row['Player'] + "\n"
        msg.body(unsold)
        return str(resp)

    if 'playerlist' == incoming_msg:
        playerlist = ""
        for index, row in playerdata.iterrows():
            playerlist += str(row['PID']) + " - " + row['Player'] + "\n"
        msg.body(playerlist)
        return str(resp)

    if 'playerstatus' in incoming_msg:
        pid = incoming_msg.split("-")[1]
        pname = playerdata.loc[playerdata.PID == int(pid), "Player"].values[0]
        status = playerdata.loc[playerdata.PID == int(pid), "Status"].values[0]
        reply = "Player id: " + pid +" - name: " + pname +" is " + status
        msg.body(reply)
        return str(resp)

    if 'teamid' in incoming_msg:
        reply = ""
        for index, row in database.iterrows():
            reply += str(row['TeamID']) + " - " +  row['Owner']  + "-" + row['Team'] + "\n"
            print(reply)
        msg.body(reply)
        return str(resp)

    if 'budget' in incoming_msg:
        reply = " Remaining budget:\n\n"
        # teamid = incoming_msg.split("-")[1]
        # teamowner = database.loc[database.TeamID == int(teamid), "Owner"].values[0]
        # print("Teamid", teamid)

        # teambudget = database.loc[database.TeamID == int(teamid), "Budget"].values[0]
        # print("Budget:",teambudget)

        for index, row in database.iterrows():
            reply += str(row['TeamID']) + " - " +  row['Team']  + "-" + str(row['Budget']) + "\n\n"

        # reply = ' Remaining budget for ' + teamowner + " is :" + " " + str(teambudget)
        msg.body(reply)
        return str(resp)

    if 'teamstatus' in incoming_msg:
        reply = "Current Roaster\n\n"
        # teamid = incoming_msg.split("-")[1]
        # players = database.loc[database.TeamID == int(teamid), "Players"].values[0]
        # teamowner = database.loc[database.TeamID == int(teamid), "Owner"].values[0]
        # reply = "Current roaster for " + teamowner + " is: " + players

        for index, row in database.iterrows():
            reply += str(row['TeamID']) + " - " +  row['Team']  + "-" + str(row['Players'])+ "\n\n"
        msg.body(reply)
        return str(resp)

    if 'buy' in incoming_msg:
        message = incoming_msg.split("-")
        teamid, pid, playername, price = message[1], message[2], message[3], message[4]
        print(teamid, pid, playername, price)

       
        print("Player Status:")
        print(playerdata.loc[playerdata.PID == int(pid), "Status"])
        playerdata.loc[playerdata.PID == int(pid), "Status"] = 'sold'
        playerdata.to_csv('playerdata.csv', index=False)

        teamname = database.loc[database.TeamID == int(teamid), "Team"].values[0]
        if database.loc[database.TeamID == int(teamid), "Players"].values[0]:
            database.loc[database.TeamID == int(teamid), "Players"] += ", " + playername
        else:
            database.loc[database.TeamID == int(teamid), "Players"] = playername
        if database.loc[database.TeamID == int(teamid), "Budget"].values[0] > 0: 
            database.loc[database.TeamID == int(teamid), "Budget"] -= float(price) 
        database.to_csv('FPL.csv', index=False)
        
        txt = playername +" sold to " + teamname +" for " + price + "\n"
        f = open("file.txt", "a")
        f.write(txt)
        f.close()
        reply = ('Successfully updated!')
        msg.body(reply)
        return str(resp)

    if 'history' in incoming_msg:
        f = open("file.txt", "r")
        reply = ""
        for line in f.readlines():
            reply += line
        msg.body(reply) 
        return str(resp)
        
    
if __name__ == '__main__':
    app.run()