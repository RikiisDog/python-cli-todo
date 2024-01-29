from typing import Any


class TodosView:
    """アプリケーションの画面表示を担当するクラス"""

    def display_menu(self) -> None:
        """メニュー画面を表示します"""
        self.display_message("メニュー画面")
        self.display_message("1. Todo一覧表示")
        self.display_message("2. Todo登録")
        self.display_message("3. Todo更新")
        self.display_message("4. Todo削除")
        self.display_message("E. 終了")

    def get_user_input(self, message: str = ">>") -> str:
        """ユーザーの入力を受け取ります

        Args:
            message (str, optional): 任意のinput出力値. Defaults to ">>".

        Returns:
            str: ユーザーからの入力値
        """
        return input(message)

    def display_todos(self, todos: list[dict[str, Any]]) -> None:
        """Todo一覧を表示します

        Args:
            todos (list[dict[str, Any]]): todo一覧
        """
        self.display_message("id   title   status")
        for todo in todos:
            status = self._check_status(todo)
            self.display_message(f"{todo.get('todo_id')} {todo.get('title')} {status}")

    def display_create_todo(self) -> str:
        """Todo登録画面を表示します

        Returns:
            str: 登録するTodoタイトル
        """
        return self.get_user_input("登録するTodoのタイトルを入力してください\n>>")

    def display_create_completed_todo(self, todo: dict[str, Any]) -> None:
        """Todo登録完了画面を表示します

        Args:
            todo (list[dict[str, Any]]): 登録したTodo
        """
        status = self._check_status(todo)
        self.display_message("以下のTodoを登録しました")
        self.display_message("id   title   status")
        self.display_message(f"{todo.get('todo_id')} {todo.get('title')} {status}")

    def display_update_todo_01(self) -> str:
        """Todo更新画面1を表示します

        Returns:
            str: 更新するTodoのID
        """
        return self.get_user_input("更新するTodoのIDを入力してください\n>>")

    def display_update_todo_02(self) -> str:
        """Todo更新画面2を表示します

        Returns:
            str: 更新したい項目の番号
        """
        self.display_message("更新する項目を選択してください\n")
        self.display_message("1. タイトル")
        self.display_message("2. ステータス")
        return self.get_user_input()

    def display_update_todo_03(self) -> str:
        """Todo更新画面3を表示します

        Returns:
            str: 更新するTodoのタイトル
        """
        return self.get_user_input("新しいタイトル名を入力してください\n>>")

    def display_update_todo_04(self) -> str:
        """Todo更新画面4を表示します

        Returns:
            str: 更新するステータスの番号
        """
        self.display_message("ステータス番号を選択してください\n")
        self.display_message("0. 未完了")
        self.display_message("1. 完了")
        return self.get_user_input()

    def display_update_completed_todo(self, todo: dict[str, Any]) -> None:
        """Todo更新完了画面を表示します

        Args:
            todo (list[dict[str, Any]]): 更新したTodo
        """
        status = self._check_status(todo)
        self.display_message("以下ようにTodoを更新しました")
        self.display_message("id   title   status")
        self.display_message(f"{todo.get('todo_id')} {todo.get('title')} {status}")

    def display_delete_todo(self) -> str:
        """Todo削除画面を表示します

        Returns:
            str: 削除するTodoのID
        """
        return self.get_user_input("削除するTodoのIDを入力してください\n>>")

    def display_delete_completed_todo(self, todo: dict[str, Any]) -> None:
        """Todo削除完了画面を表示します

        Args:
            todo (dict[str, Any]): 削除するTodoデータ
        """
        status = self._check_status(todo)
        self.display_message("以下のTodoを削除しました")
        self.display_message("id   title   status")
        self.display_message(f"{todo.get('todo_id')} {todo.get('title')} {status}")

    def display_message(self, message: str) -> None:
        """任意のメッセージを表示します

        Args:
            message (str): メッセージ
        """
        print(message)

    def _check_status(self, todo: dict[str, Any]) -> str:
        """Todo変換済みステータスを返します

        Args:
            todo (dict[str, Any]): Todoデータ

        Returns:
            str: Todoステータス
        """
        status = todo.get("status")
        if isinstance(status, int):
            status_map = {0: "未完了", 1: "完了"}
            return status_map.get(status, "Unknown")
        else:
            return "Unknown"
