import psycopg2
from psycopg2 import Error
import pandas as pd

# fill in these variables for your own cluster
#You need to construct the server in pgAdmin First

host = "c-jde7silvercluster.azph6jziee3sfh.postgres.cosmos.azure.com"
dbname = "jde7silverdb"
user = "citus"
password = "jde7_silver"
sslmode = "require"

def connect():
    try:
        # Connect to an existing database
        conn = psycopg2.connect(host=host, port=5432, user=user, password=password, database=dbname, sslmode=sslmode)
        # Create a cursor to perform database operations
        cursor = conn.cursor()

        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(conn.get_dsn_parameters(), "\n")
        # Executing a SQL query
        cursor.execute("SELECT version();")
        # Fetch result
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")
        return conn
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return False

def exeQuery(cur, query, value=None):
    try:
        # connect to the PostgreSQL server
        print(query)
        resp = cur.execute(query, value)
        print('resp:', resp)
        # close communication with the PostgreSQL database server
        return True
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return False

def create_table(conn, table_name, columns:dict, pk=None):
    cur = conn.cursor()
    query = f"CREATE TABLE IF NOT EXISTS {table_name} ("

    for column_name, data_type in columns.items():
        query += f"{column_name} {data_type}, "
    
    if pk != None:
        query += f"PRIMARY KEY ({pk}))"
    else:
        query = query.rstrip(", ") + ")"
    
    sucess = exeQuery(cur, query)
    cur.close()
    conn.commit()
    return sucess

def insert_values(conn, table_name, data):
    cur = conn.cursor()
    for row in data:
        columns = ', '.join(row.keys())
        placeholders = ', '.join(['%s'] * len(row.values()))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        values = tuple(row.values())
        exeQuery(cur, query, values)
    cur.close()
    conn.commit()

def createColumn(df):
    dtypes = df.dtypes.to_dict()
    sql_type=dict(zip(['int64','float64','bool','object'], ["INTEGER","NUMERIC","BOOLEAN","VARCHAR(255)"]))
    data = {(col.lower().replace(' ', '_')): sql_type[str(dtype)] for col, dtype in dtypes.items()}
    columns=",".join(list(data.keys()))
    return columns, data

def df_to_postgresql(conn, df, table_name):
    columns, data_types = createColumn(df)
    create_table(conn, table_name, data_types)
    # insert data

    df.rename(columns=dict(zip(df.columns, columns)))
    data = df.to_dict("records")
    insert_values(conn, table_name, data)

def search(connection, query):
    cursor = conn.cursor()
    print(query)
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows

#query for select table
#"*" for all col, "a,b" for select column a and b
#you may assign subquery to f"a, ({qst(b,y)})" if needed
def qst(col, table_name):
    return f"SELECT {col} FROM {table_name}"
    return f"SELECT {', '.join(col_list)} FROM {table_name}"
def printAll(rows):
    for row in rows:
        print(row)
def qsmt(col, table_list):
    #select table1.col,table2.col from table1 join table2

    return " UNION ".join([s1c1t(col, table) for table in table_list])
if __name__ == '__main__':
    conn=connect();
    df_to_postgresql(conn, pd.read_csv("dummy.csv"), "dummy")
    #q=qst(col, table_name)
    #printAll(SelectQuery(conn, q))
    conn.close();