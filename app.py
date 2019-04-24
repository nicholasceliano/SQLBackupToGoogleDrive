import os, json
from models.DatabaseConnInfo import DatabaseConnInfo
from services.GoogleDriveService import GoogleDriveService
from services.SQLDumpService import SQLDumpService

appRoot = os.path.split(os.path.abspath(__file__))[0]
config = json.load(open(os.path.join(appRoot, 'config.json')))
dbConnInfo = DatabaseConnInfo(config["databaseConn"])

dmpPath = SQLDumpService(appRoot, dbConnInfo).dump()
GoogleDriveService(dmpPath, config["googleDriveFolder"])
