from dataclasses import dataclass

from conductor.client.worker.worker_task import worker_task


@dataclass
class UserInfo:
    """
        Python data class for User Info
        """
    user_id: int
    name: str
    address: str
    country: str


@worker_task(task_definition_name='simple_task')
def greet(name: str) -> str:
    return f'hello, {name}'


@worker_task(task_definition_name='get_user_info')
def get_user_info(name: str) -> UserInfo:
    return UserInfo(user_id=1, name=name, address='100 fine street', country='USA')