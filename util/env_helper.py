import os

from config import API_HOSTS


class EnvHelper:
    @staticmethod
    def get_app_env():
        app_env = os.environ.get('APP_ENV').lower() if os.environ.get('APP_ENV') else "staging"
        print("Working on application environment:{}".format(app_env))
        return app_env

    @staticmethod
    def get_base_url():
        return API_HOSTS[EnvHelper.get_app_env()]