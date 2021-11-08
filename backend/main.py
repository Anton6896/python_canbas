from typing import Optional

from fastapi import FastAPI

server = FastAPI()


# uvicorn backend.main:server --reload


@server.get("/")
def get_board():
    board_data = {
        'tasks': {
            'task_1': {'id': 'task_1', 'content': 'content1'},
            'task_2': {'id': 'task_2', 'content': 'content2'},
            'task_3': {'id': 'task_3', 'content': 'content3'},
        },
        'columns': {
            'column_1': {
                'id': 'column_1',
                'title': 'todo',
                'tasks_id': ['task_1', 'task_2']
            },
            'column_2': {
                'id': 'column_2',
                'title': 'done',
                'tasks_id': ['task_3', ]
            }
        },
        'column_order': ['column_1', 'column_2']
    }
    return {"boards": board_data}
