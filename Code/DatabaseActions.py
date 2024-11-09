from langchain_community.utilities.sql_database import SQLDatabase

class DatabaseActions:
    
    def __init__(user, host, password, name):
        self.user = user
        self.host = host
        self.password = password
        self.name = name

    def createURI(dbType, tabelnames:list, rows=3):
        if dbType = 'MySQL':
            return SQLDatabase.from_uri(f"mysql+pymysql://{self.user}:{self.password}@{self.host}/{self.name}", sample_rows_in_table_info = rows, include_tables = tabelnames)
        elif dbType = 'Postgres':
            return SQLDatabase.from_uri(f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}/{self.name}", sample_rows_in_table_info = rows, include_tables = tabelnames)

    