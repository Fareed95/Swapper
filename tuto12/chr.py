import os
import sqlite3
import shutil

def fetch():
    # Chrome history file path for Windows
    history_path = os.path.join(os.environ['LOCALAPPDATA'], 'Google', 'Chrome', 'User Data', 'Default', 'History')

    # Copying the history file to a temporary location
    temp_history_path = 'chrome_history'
    shutil.copy2(history_path, temp_history_path)

    # Connect to the database
    connection = sqlite3.connect(temp_history_path)
    cursor = connection.cursor()

    # Query to retrieve history
    query = "SELECT url, title, last_visit_time FROM urls ORDER BY last_visit_time DESC LIMIT 10;"
    cursor.execute(query)

    # Fetch and print results
    results = cursor.fetchall()
    for result in results:
        print(result)

    # Close the database connection
    connection.close()

    # Remove the temporary history file
    os.remove(temp_history_path)
