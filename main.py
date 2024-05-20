#  Copyright 2024 Orkes Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
#  the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
#  an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
#  specific language governing permissions and limitations under the License.

from conductor.client.automator.task_handler import TaskHandler
from conductor.client.configuration.configuration import Configuration


def start_workers() -> TaskHandler:
    configuration = Configuration()

    task_handler = TaskHandler(
        workers=[],
        configuration=configuration,
        scan_for_annotated_workers=True
    )
    task_handler.start_processes()
    print('started all workers')
    return task_handler


def main():
    print("Python workers are starting")
    start_workers()


if __name__ == '__main__':
    main()
