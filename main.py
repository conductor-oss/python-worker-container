from conductor.client.automator.task_handler import TaskHandler, logger
from conductor.client.configuration.configuration import Configuration
from conductor.client.configuration.settings.authentication_settings import AuthenticationSettings
import logging
import sys
import os

from workers import workers


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
