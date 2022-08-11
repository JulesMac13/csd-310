import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1am@Rockstar",
    database="pysports"
)

#inner join
# SELECT player_id, first_name, last_name, team_name
# FROM player
# INNER JOIN team
#     ON player.team_id = team.team_id

cursor = db.cursor()

query = """SELECT player_id, first_name, last_name, team_name 
FROM player 
INNER JOIN team 
    ON player.team_id = team.team_id"""

cursor.execute(query)

result = cursor.fetchall()

print("-- Displaying Player Records --")

for player in result:
    print(player)