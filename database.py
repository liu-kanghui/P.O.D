import sqlite3
import config

db_file = config.sqlite_file
print(db_file)
table_name1 = 'pods'   # name of the table to be created
table_name2 = 'groups'   # name of the table to be created
new_field = 'my_1st_column'  # name of the column
field_type = 'INTEGER'  # column data type

sql_create_groups_table = """CREATE TABLE IF NOT EXISTS groups(
                                    name text PRIMARY KEY,
                                    lightpattern text NOT NULL,
                                    pic_interval integer NOT NULL,
                                    water_interval integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL
                                );"""

sql_create_pods_table = """CREATE TABLE IF NOT EXISTS pods(
                                    name text PRIMARY KEY,
                                    mac_address text NOT NULL,
                                    host_address integer NOT NULL,
                                    group_name text NOT NULL
                                );"""

def initializeTable():
    conn = create_connection(db_file)
    if conn is not None:
        create_table(conn, sql_create_pods_table)
    else:
        print("error! cannot create the database")




# Creating a new SQLite table with 1 column
# c.execute('CREATE TABLE {tn} ({nf} {ft})'
#           .format(tn=table_name1, nf=new_field, ft=field_type))

# # Creating a second table with 1 column and set it as PRIMARY KEY
# # note that PRIMARY KEY column must consist of unique values!
# c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'
#           .format(tn=table_name2, nf=new_field, ft=field_type))


# Committing changes and closing the connection to the database file
# conn.commit()
# conn.close()

def main():
    print("shit")



def create_connection(db_file):
    """ Create a database connection to the SQLite database
        specified by db_file
    : param db_file: database file
    : return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as err:
        print(err)

    return None


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql
    : param conn: COnnection object
    : param create_table_sql: a CREATE TABLE statement
    : return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as err:
        print(err)



if __name__ == '__main__':
    main()