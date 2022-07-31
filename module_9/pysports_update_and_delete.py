import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1am@Rockstar",
    database="pysports"
)

cursor = db.cursor()

#insert player

insert_query = """INSERT INTO player(first_name, last_name, team_id)
    VALUES('Smeagol', 'Shire Folk', 1)"""

cursor.execute(insert_query)

db.commit()

#select query with INNER Join to display results

query = """SELECT player_id, first_name, last_name, team_name 
FROM player 
INNER JOIN team 
    ON player.team_id = team.team_id"""

cursor.execute(query)

result = cursor.fetchall()

print("-- Displaying Player Records AFTER INSERT--")

for player in result:
    print(player)

#Update player

update_query = """UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'"""

cursor.execute(update_query)

db.commit()

#select query with INNER Join to display results

query = """SELECT player_id, first_name, last_name, team_name 
FROM player 
INNER JOIN team 
    ON player.team_id = team.team_id"""

cursor.execute(query)

result = cursor.fetchall()

print("-- Displaying Player Records AFTER UPDATE--")

for player in result:
    print(player)

#Delete newly added player

delete_query = """DELETE FROM player WHERE first_name = 'Smeagol'"""

cursor.execute(delete_query)

db.commit()

#select query with INNER Join to display results

query = """SELECT player_id, first_name, last_name, team_name 
FROM player 
INNER JOIN team 
    ON player.team_id = team.team_id"""

cursor.execute(query)

result = cursor.fetchall()

print("-- Displaying Player Records AFTER DELETE--")

for player in result:
    print(player)