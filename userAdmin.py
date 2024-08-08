import os
from database.databaseAdmin import DatabaseAdmin
from getpass import getpass

FILE_NAME = "database\\localUsers.json"

DATABASE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        FILE_NAME
    )
)

class UserAdmin:
    def __init__(self, database: DatabaseAdmin) -> None:
        self.database = database
        self.users = self.database.getKeys("users")
        self.currentUser = self.users[0]
        self.userContent = self.database.get("users").get(self.currentUser).get("content")
    

    def switchUser(self, login: str = None, password: str = None):
        if not login:
            login = input("login: ")
            
        if login in self.users:

            userAcess = self.database.get("users").get(login).get("acess")

            if userAcess.get("restricted"):
                password = getpass("Password: ")
                if password == userAcess["password"]:
                    self.userContent =  self.database.get("users").get(login).get("content")
                    self.currentUser = login

    def storeVariable(self, variable, value):
        allData = self.database.data
        allData.get("databaseContent").get("users").get(self.currentUser).get("content").get("localVariables").update(
            {variable: value}
        )
        self.database.post(allData)

userAdmin = UserAdmin(DatabaseAdmin(DATABASE_PATH))