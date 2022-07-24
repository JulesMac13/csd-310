#region python connection
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "1am@Rockstar",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on Host {} with database {}" .format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
#endregion

query = "SELECT team_id, team_name, mascot FROM team"

cursor = db.cursor()

cursor.execute("SELECT team_id, team_name, mascot FROM team")

teams = cursor.fetchall()

for team in teams:
    print("Team Name: {}".format(team[1]))

# query = "SELECT player_id, first_name, last_name, team_id FROM player"

# cursor = db.cursor()

# cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

# teams = cursor.fetchall()

# for player in players:
#     print("Player Name: {}".format(player[1]))