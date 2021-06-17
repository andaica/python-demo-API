import mysql.connector

class DB:
    def __init__(self, host = "", port = "", user = "", password = "", database = ""):
        self.connect = mysql.connector.connect(
            host=host if host else "127.0.0.1",
            port=port if host else 3306,
            user=user if user else "root",
            password=password if password else "password",
            database=database if database else "database"
        )
        self.cursor = self.connect.cursor(dictionary=True)

    def select(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    
    def insertone(self, table, record):
        fields = record.keys()
        fieldlist = ", ".join(fields)
        fieldmarks = ", ".join(["%s" for x in range(len(fields))])
        
        sql = "INSERT INTO {} ({}) VALUES ({})".format(table, fieldlist, fieldmarks)
        val = tuple(record.values())

        print("insert: ", sql, val)
        self.cursor.execute(sql, val)
        self.connect.commit()

        result = self.cursor.rowcount
        return result

    def insertmany(self, table, records):
        fields = records[0].keys()
        fieldlist = ", ".join(fields)
        fieldmarks = ", ".join(["%s" for x in range(len(fields))])
        
        sql = "INSERT INTO {} ({}) VALUES ({})".format(table, fieldlist, fieldmarks)
        val = [tuple(record.values()) for record in records]

        print("insert: ", sql, val)
        self.cursor.executemany(sql, val)
        self.connect.commit()

        result = self.cursor.rowcount
        return result

    def update(self, table, set, whereclause):
        def format(key, value):
            if isinstance(value, (int, float, bool)):
                return "{} = {}".format(key, value)
            else:
                return "{} = '{}'".format(key, value)
        setclause = ", ".join([ format(x, set[x]) for x in set ])
        sql = "UPDATE {} SET {} WHERE {}".format(table, setclause, whereclause)
        
        print("update: ", sql)
        self.cursor.execute(sql)
        self.connect.commit()

        result = self.cursor.rowcount
        return result