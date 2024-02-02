from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

credentials = "credentials_account.json"


authentication = GoogleAuth()
authentication.LocalWebserverAuth()

def login():
    auth = GoogleAuth()
    auth.LoadCredentialsFile(credentials)

    if auth.access_token_expired:
        auth.Refresh()
        auth.SaveCredentialsFile(credentials)
    else:
        auth.Authorize()


    return GoogleDrive(auth)