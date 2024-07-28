import json


class DatabaseAdmin:

    def __init__(self, path: str, databaseKey: str = None) -> None:
        with open(path, 'r', encoding="utf-8") as file:
            self.database: dict = json.load(file)
            if self.database.get("restricted"):
                if not (databaseKey == self.database.get("password")):
                    self.database = None

    def get(self, key: str):
        return self.database["databaseContent"].get(key)
    
    def getKeys(self, key: str):
        return list(self.database["databaseContent"].get(key).keys())
    
    def post(self, path, content):
        pass
