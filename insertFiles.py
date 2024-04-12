import os
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7>>HhNN6/fZ",
    database="dataset"
)
cursor = conn.cursor()

# Path to the folder containing PDF and WinRAR files
folder_path = r"C:\Users\elmer\PycharmProjects\Freud_AI\dataset"

# Iterate through files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Check if the file is a PDF
    if filename.endswith(".pdf"):
        with open(file_path, "rb") as file:
            content = file.read()

        # Insert PDF file content into database
        sql = "INSERT INTO information (file_name, file_content) VALUES (%s, %s)"
        values = (filename, content)
        cursor.execute(sql, values)

        print (f" '{filename}' added successfully")

    # Check if the file is a WinRAR archive
    elif filename.endswith(".rar"):
        with open(file_path, "rb") as file:
            content = file.read()

        # Insert WinRAR file content into database
        sql = "INSERT INTO information (file_name, file_content) VALUES (%s, %s)"
        values = (filename, content)
        cursor.execute(sql, values)

    # Skip other file types
    else:
        print(f"Ignoring file: {filename}")

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()
