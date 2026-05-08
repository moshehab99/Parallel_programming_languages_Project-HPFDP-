from sqlalchemy import create_engine

DB_URL = "mysql+pymysql://root:12345678@localhost/hpfdp_db"

class DatabaseConnection:
    _instance = None

    @staticmethod
    def get_instance():
        if DatabaseConnection._instance is None:
            DatabaseConnection._instance = create_engine(DB_URL)
        return DatabaseConnection._instance