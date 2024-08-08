from database.databaseAdmin import DatabaseAdmin
from userAdmin import userAdmin
from commandProcessor import CommandKernel

commandAdmin = CommandKernel([("defaltUser", "*")])
userController = userAdmin

tempVariables = {}

while True:
    command = commandAdmin.getCommand(
        userAdmin.currentUser, 
        userAdmin.userContent["localVariables"], 
        tempVariables)
    
    commandAdmin.runCommand(command)