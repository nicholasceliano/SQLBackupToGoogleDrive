import pickle
import os.path
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request


SCOPES = ['https://www.googleapis.com/auth/drive']

class GoogleDriveService:
	googleDriveCredentials = 'GoogleDriveCreds.txt'
	def __init__(self, localFilePath, driveFolder = ''):
		self.drive = self.__authenticate__()
		uploadFolderId = self.__getUploadFolderId__(driveFolder)
		self.__uploadFile__(localFilePath, uploadFolderId)

	def __authenticate__(self):
		g_login = GoogleAuth()
		g_login.LoadCredentialsFile(self.googleDriveCredentials)
		if g_login.credentials is None:
			g_login.LocalWebserverAuth()
		elif g_login.access_token_expired:
			g_login.Refresh()
		else:
			g_login.Authorize()
		
		g_login.SaveCredentialsFile(self.googleDriveCredentials)

		return GoogleDrive(g_login)

	def __getUploadFolderId__(self, driveFolder):
		uploadFolderId = 'root'

		file_list = self.drive.ListFile({'q': '\'root\' in parents and trashed=false'}).GetList()
		for f in file_list:
			if (f['title'] == driveFolder):
				uploadFolderId = f['id']
				break

		return uploadFolderId
				
	def __uploadFile__(self, localFilePath, uploadFolderId):
		with open(localFilePath,"r") as file:
			file_drive = self.drive.CreateFile({'title':os.path.basename(file.name), 'parents': [{'kind': 'drive#fileLink', 'id': uploadFolderId}] })
			file_drive.SetContentString(file.read()) 
			file_drive.Upload()
