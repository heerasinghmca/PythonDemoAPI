from util.env_helper import EnvHelper


class BaseClient:
    def __init__(self):
        self.base_url = f'{EnvHelper.get_base_url()}'
        self.headers = {"Accept": "application/json", "Content-Type": "application/json"}