import pymysql
from pydantic import BaseModel
from pymysql.connections import Connection
from pymysql.cursors import DictCursor


class DbConnection(BaseModel):
    """データベース接続を担当するクラス"""

    host: str = "db"
    user: str = "python"
    password: str = "python"
    db: str = "todo"
    charset: str = "utf8mb4"

    def connect(self) -> Connection:
        """データベースに接続します

        Returns:
            Connection: 接続コネクション
        """
        return pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db,
            charset=self.charset,
            cursorclass=DictCursor,
        )
