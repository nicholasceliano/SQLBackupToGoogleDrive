# SQLBackupToGoogleDrive

Create client_secrets.json in root folder to hold Google Drive API info (auto-generated file from Google API Dashboard)
```
{
	"installed":{
		"client_id":"",
		"project_id":"",
		"auth_uri":"",
		"token_uri":"",
		"auth_provider_x509_cert_url":"",
		"client_secret":"",
		"redirect_uris":[]
	}
} 
```

Create config.json in /sqlbackuptogoogledrive to hold database credentials:
```
{
	"googleDriveFolder": "", //can be empty
	"databaseConn": {
		"host": "",
		"database": "",
		"user": "",
		"password": ""
	}
}
```

Install locally
```
sudo pip install -e /home/pi/Documents/git/SQLBackupToGoogleDrive
```

Run locally
```
gnucashBackup
```