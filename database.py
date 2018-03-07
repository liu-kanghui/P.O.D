import sqlite3
import config

sqlite_file = config.sqlite_file
print(sqlite_file)
table_name1 = 'my_table_1'   # name of the table to be created
table_name2 = 'my_table_2'   # name of the table to be created
new_field = 'my_1st_column'  # name of the column
field_type = 'INTEGER'  # column data type


conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


# Creating a new SQLite table with 1 column
c.execute('CREATE TABLE {tn} ({nf} {ft})'
          .format(tn=table_name1, nf=new_field, ft=field_type))


# Creating a second table with 1 column and set it as PRIMARY KEY
# note that PRIMARY KEY column must consist of unique values!
c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'
          .format(tn=table_name2, nf=new_field, ft=field_type))


# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
