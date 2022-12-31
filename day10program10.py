import sqlite3
carData=[
    (1,'Audi',52642),
    (2,'Mercedes',57127),
    (3,'Skoda',9000),
    (4,'Volva',29000),
    (5,'Bentley',350000),
    (6,'Hummer',41400),
    (7,'Volkswa',21600),
    (8,'yuvaraj',100000)
    ]
con=sqlite3.connect('mtica.db')
cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute("CREATE TABLE Cars(Id INT,Name TEXT,price INT)")
cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)",carData)
con.commit()
con.close()
print("values inserted.")
