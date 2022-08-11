import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1am@Rockstar",
    database="pysports"
)

#teams
cursor = db.cursor()

query = "SELECT team_id, team_name, mascot FROM team"

cursor.execute(query)

print("Displaying Player Records")

for team in cursor:
    print(team)

cursor.close()

print()

#players
cursor = db.cursor()

query = "SELECT player_id, first_name, last_name, team_id FROM player"

cursor.execute(query)

print("Displaying Player Records")

for player in cursor:
    print(player)

cursor.close()

db.close()