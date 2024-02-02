

from utils.login import login


def upload_file(path_file, parent_id):
    credentials = login()
    file = credentials.CreateFile({
        'parents': [{
            "kind": "drive#fileLink",
            "id": parent_id,
        }]})
    file['title'] = path_file.split('/')[-1]
    file.SetContentFile(path_file)
    file.Upload()
    print(f'El archivo: {file['title']} se subio con exito')