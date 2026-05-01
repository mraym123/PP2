Quick guide for direction:
1. assets: needed files to load: background music, coin_take etc.
2. settings.json: settings for game to run
3. db.py - python file to execute queries to PostgreSQL
4. database.ini - database configuration
5. db_connection.log - logging connections and executions to sql server (need to be ignored)
6. game.py - game mechanics
7. config.py - use configurations to connect with DB
8. main.py - main executable program to play the game
9. archive_files/main_safe.py -> safe version if any error occurs (just a file with all codes combined from main.py + game.py)