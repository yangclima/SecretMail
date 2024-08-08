import json


class DatabaseAdmin:

    def __init__(self, path: str, databaseKey: str = None) -> None:
        self.path = path
        with open(self.path, 'r', encoding="utf-8") as file:
            self.data: dict = json.load(file)
            if self.data.get("restricted"):
                if not (databaseKey == self.data.get("password")):
                    self.data = None

    def get(self, key: str):
        return self.data["databaseContent"].get(key)
    
    def getKeys(self, key: str):
        return list(self.data["databaseContent"].get(key).keys())
    
    def post(self, content):
        with open(self.path, 'w', encoding="utf-8") as file:
            json.dump(content,file, ensure_ascii=False, indent=4)
