from typing import Any, Optional

from model.db_connection import DbConnection
from pydantic import BaseModel


class DbOperation(BaseModel):
    """データベース操作を担当するクラス"""

    db_connection: DbConnection = DbConnection()

    def execute_query(self, query: str, params: tuple = ()) -> None:
        """クエリを実行し、コミットします

        Args:
            query (str): 実行するSQLクエリ
            params (tuple): SQLクエリパラメータ
        """
        with self.db_connection.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                conn.commit()

    def fetch_all_data(self, query: str, params: tuple = ()) -> list[dict[str, Any]]:
        """クエリを実行し、全データをフェッチします

        Args:
            query (str): 実行するSQLクエリ
            params (tuple, optional): SQLクエリパラメータ. Defaults to ().

        Returns:
            list[dict[str, Any]]: 取得したSQL結果セット
        """
        with self.db_connection.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                results: list[dict[str, Any]] = cursor.fetchall()
                return results

    def fetch_one_data(self, query: str, params: tuple = ()) -> Optional[dict[str, Any]]:
        """クエリを実行し、単一データをフェッチします

        Args:
            query (str): 実行するSQLクエリ
            params (tuple, optional): SQLクエリパラメータ. Defaults to ().

        Returns:
            list[dict[str, Any]]: 取得したSQL結果セット
        """
        with self.db_connection.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                results: Optional[dict[str, Any]] = cursor.fetchone()
                return results
