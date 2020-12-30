from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

# application에 대한 작업을 시작하기전에 settings.py의 project_apps에 'apps.py' application의 config를 추가해줘야함.
