import os
import sys

from exceptions.todo_not_found_error import TodoNotFoundError
from model.todos_model import TodosModel
from view.todos_view import TodosView


class TodosController:
    """アプリケーションの制御を担当するクラス"""

    def __init__(self) -> None:
        self.model = TodosModel()
        self.view = TodosView()
        self.actions = {
            "1": self.display_todos,
            "2": self.create_todo,
            "3": self.update_todo,
            "4": self.delete_todo,
            "E": self.exit_app,
        }

    def run(self) -> None:
        """アプリケーションのメインループを実行します"""
        while True:
            # 標準出力をクリア
            os.system("clear")
            # メニュー表示
            self.view.display_menu()
            # ユーザーからの入力を取得
            user_input = self.view.get_user_input()
            # 入力に紐づいたコールバック関数を取得
            user_action = self.actions.get(user_input)
            if user_action:
                user_action()
            else:
                self.view.display_message("無効な入力です")
                self._wait_for_user()

    def display_todos(self) -> None:
        """Todo一覧を表示します"""
        try:
            todos = self.model.get_todo_list()
            self.view.display_todos(todos)
            self._wait_for_user()
        except Exception as e:
            self.view.display_message(f"予期せぬエラーが発生しました\n{e}")
            self._wait_for_user()

    def create_todo(self) -> None:
        """Todo新規登録を実行します"""
        try:
            title = self.view.display_create_todo()
            self.model.create_todo(title)
            todo = self.model.get_todo_list()[-1]
            self.view.display_create_completed_todo(todo)
            self._wait_for_user()
        except Exception as e:
            self.view.display_message(f"予期せぬエラーが発生しました\n{e}")
            self._wait_for_user()

    def update_todo(self) -> None:
        """Todo更新を実行します"""
        try:
            todo_id = int(self.view.display_update_todo_01())
            self.model.get_todo_by_id(todo_id)
            update_choice = self.view.display_update_todo_02()
            if update_choice == "1":
                todo_title = self.view.display_update_todo_03()
                self.model.update_title_by_id(todo_id, todo_title)
            elif update_choice == "2":
                todo_status = int(self.view.display_update_todo_04())
                self.model.update_status_by_id(todo_id, todo_status)
            else:
                raise ValueError
            updated_todo = self.model.get_todo_by_id(todo_id)
            self.view.display_update_completed_todo(updated_todo)
            self._wait_for_user()
        except ValueError:
            self.view.display_message("無効な入力です")
            self._wait_for_user()
        except TodoNotFoundError:
            self.view.display_message("TODOが存在しません")
            self._wait_for_user()
        except Exception as e:
            self.view.display_message(f"予期せぬエラーが発生しました\n{e}")
            self._wait_for_user()

    def delete_todo(self) -> None:
        """Todo削除を実行します"""
        try:
            todo_id = int(self.view.display_delete_todo())
            todo = self.model.get_todo_by_id(todo_id)
            self.model.delete_todo_by_id(todo_id)
            self.view.display_delete_completed_todo(todo)
            self._wait_for_user()
        except ValueError:
            self.view.display_message("無効な入力です")
            self._wait_for_user()
        except TodoNotFoundError:
            self.view.display_message("TODOが存在しません")
            self._wait_for_user()
        except Exception as e:
            self.view.display_message(f"予期せぬエラーが発生しました\n{e}")
            self._wait_for_user()

    def exit_app(self) -> None:
        """アプリケーションを終了します"""
        print("アプリケーションを終了します")
        sys.exit()

    def _wait_for_user(self) -> None:
        """ユーザーの入力(E)を待機します"""
        while self.view.get_user_input("メニューに戻る(E)\n>>") != "E":
            pass
