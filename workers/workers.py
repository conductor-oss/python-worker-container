#  Copyright 2024 Orkes Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
#  the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
#  an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
#  specific language governing permissions and limitations under the License.

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