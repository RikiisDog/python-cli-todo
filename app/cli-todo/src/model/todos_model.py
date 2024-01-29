from typing import Any, Optional

from exceptions.todo_not_found_error import TodoNotFoundError
from model.db_operation import DbOperation
from pydantic import BaseModel


class TodosModel(BaseModel):
    """todosテーブルの操作を担当するクラス"""

    db_operation: DbOperation = DbOperation()

    def get_todo_list(self) -> list[dict[str, Any]]:
        """TODO一覧を取得します

        Returns:
            list[dict[str, Any]]: TODO一覧リスト
        """
        query = "SELECT todo_id, title, status FROM todos ORDER BY todo_id"
        results: list[dict[str, Any]] = self.db_operation.fetch_all_data(query)
        return results

    def get_todo_by_id(self, todo_id: int) -> Optional[dict[str, Any]]:
        """一意のTODOを取得します

        Args:
            todo_id (int): TODOのID

        Returns:
            Optional[dict[str, Any]]: 一意のTODO
        """
        query = "SELECT todo_id, title, status FROM todos WHERE todo_id = %s"
        params = (todo_id,)
        results: Optional[dict[str, Any]] = self.db_operation.fetch_one_data(query, params)
        if not results:
            raise TodoNotFoundError
        return results

    def create_todo(self, title: str) -> None:
        """TODOを登録します

        Args:
            title (str): TODOのタイトル
        """
        query = "INSERT INTO todos (title) VALUES (%s)"
        params = (title,)
        self.db_operation.execute_query(query, params)

    def update_title_by_id(self, todo_id: int, title: str) -> None:
        """TODOのタイトルを更新します

        Args:
            todo_id (int): 更新対象のTODOのID
            title (str): 更新後のTODOのタイトル
        """
        query = "UPDATE todos SET title = %s WHERE todo_id = %s"
        params = (title, todo_id)
        self.db_operation.execute_query(query, params)

    def update_status_by_id(self, todo_id: int, status: int) -> None:
        """TODOのステータスを更新します

        Args:
            todo_id (int): 更新対象のTODOのID
            status (int): 更新後のTODOのステータス
        """
        query = "UPDATE todos SET status = %s WHERE todo_id = %s"
        params = (status, todo_id)
        self.db_operation.execute_query(query, params)

    def delete_todo_by_id(self, todo_id: int) -> None:
        """TODOを削除します

        Args:
            todo_id (int): 削除対象のTODOのID
        """
        query = "DELETE FROM todos WHERE todo_id = %s"
        params = (todo_id,)
        self.db_operation.execute_query(query, params)
