class ConnectionFactory:
    """
    A simple Database connection factory.
    Usage:
        >>> with ConnectionFactory("mysql") as c:
        ...     print(c)
        ...

    """
    def __init__(self, db_type):
        self.db_type = db_type

    def __enter__(self):
        if self.db_type.startswith("mysql"):
            class MySQLConnection: pass
            self.conn = MySQLConnection()
        elif self.db_type.startswith("sqlite"):
            class SQLiteConnection: pass
            self.conn = SQLiteConnection()
        return self.conn

    def __exit__(self, et, ev, tb):
        #self.conn.close()
        pass

#cf = ConnectionFactory("mysql")
#print(cf)

with ConnectionFactory("sqlite") as c:
    print(c)




