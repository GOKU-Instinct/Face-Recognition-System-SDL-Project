import sqlite3
conn = sqlite3.connect('customers.sqlite')
cursor = conn.cursor()
print("Opened database successfully")

# cursor.execute(''' create table customer
#         (Id BLOB primary key not null,
#         Name text,
#         Entry_time text,
#         Entry_happiness real,
#         Exit_happiness real,
#         Exit_time text);''')
# cursor.close()

val = 1.0
cursor = conn.cursor()
conn.execute(''' insert into customer (Id,entry_happiness) values (?,?)''',('1',val))
cursor.close
conn.commit()
conn.close()
