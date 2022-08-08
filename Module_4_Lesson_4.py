import sqlite3
from tkinter.tix import Select

#check that it has been imported successfully
# print("Module imported successfully!")

#Connect to a database
conn = sqlite3.connect('celebs.db')
# print("Connected successfully!")

#Create a cursor object
curs = conn.cursor()
# print("Cursor connected successfully!")

#Creating a new table
# curs.execute("""CREATE TABLE celebrity(
#             Name TEXT,
#             Genre TEXT,
#             Num_albums INTEGER,
#             Age INTEGER,
#             Awards INTEGER,
#             Years_in_industry INTEGER
#             )
# """)
# print("Table created successfully!")

#Inserting values to the table
music_data_set = [('Ariana Grande', 'RnB', '6', '29', '45', '14'),
                 ('Ed Sheeran', 'Hip Hop', '5', '31', '60', '11'),
                 ('Jason Derulo', 'RnB', '7', '33', '58', '12'),
                 ('Shawn Mendes', 'RnB', '4', '28', '20', '7'),
                 ('The Weekend', 'Rock', '5', '30', '25', '10'),
                 ('Adele', 'RnB', '8', '30', '70', '16'),
                 ('Beyonce', 'RnB', '12', '35', '89', '25'),
                 ('Camilla Cabelo', 'Hip Hop', '3', '26', '15', '6'),
                 ('David Guetta', 'Metal', '5', '31', '40', '30'),
                 ('Ellie Goulding', 'RnB', '6', '28', '50', '8'),
                 ('Katy Perry', 'Hip Hop', '8', '30', '80', '15'),
                 ('Jess Glyne', 'Jazz', '4', '28', '30', '9'),
                 ('Lea Michelle', 'RnB', '3', '30', '35', '17'),
                 ('Rita Ora', 'Blues', '6', '32', '45', '15'),
                 ('Taylor Swift', 'Soul', '10', '30', '75', '10'),
                 ('Pink', 'Country', '8', '33', '88', '20'),
                 ('Fifth Harmony', 'Jazz', '9', '34', '70', '25'),
                 ('Kelly Clarkson', 'Soul', '8', '36', '85', '25'),
                 ('Liam Payne', 'Blues', '5', '32', '60', '6'),
                 ('Maroon 5', 'Rock', '7', '38', '77', '25')
                ]
# print("music_data_set created successfully!")

curs.executemany("INSERT INTO celebrity VALUES (?, ?, ?, ?, ?, ?)", music_data_set)

#querying the database
curs.execute("SELECT * FROM celebrity")
# print("Query executed successfully!")

#format output to display in a tabular form
items = curs.fetchall()
# print("Name" + "\t\t\tGenre" + "\t\tNum_albums" + "\t\tAge" + "\t\tAwards" + "\t\tYears_in_industry" "\n" f"{'.' * 120}")
# print(items)

#looping through the items
for item in items:
    Name, Genre, Num_albums, Age, Awards, Years_in_industry = item
    # print(f"{Name:25}{Genre:10}{Num_albums:10}{Age:22}{Awards:18}{Years_in_industry:18}")

conn.commit()
# print("Committed successfully!")

#The most decorated celebrity
curs.execute("""
SELECT NAME,MAX(Awards)
FROM celebrity
""")
item = curs.fetchall()
print(item)

#The oldest celebrity
curs.execute("""
SELECT NAME,MAX(Age)
FROM celebrity
""")
item = curs.fetchall()
print(item)

#The celebrity that has been in the industry the longest
curs.execute("""
SELECT NAME,MAX(Years_in_industry)
FROM celebrity
""")
item = curs.fetchall()
print(item)

#The celebrity with the least number of albums
curs.execute("""
SELECT NAME,MIN(Num_albums)
FROM celebrity
""")
item = curs.fetchall()
print(item)

#The most popular genre of music amongst all celebrities in the dataset
curs.execute("""
SELECT MAX(Genre)
FROM celebrity
""")
item = curs.fetchall()
print(item)


#commit the database and table
conn.commit()

#close the connection to the database
conn.close()