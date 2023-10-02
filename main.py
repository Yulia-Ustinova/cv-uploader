from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder_id = '1FNuu7w_3hDVKDbiTBXJnbrOdGhYLDdQV'
upload_file = '/Users/yuliaustinova/Documents/Документы/Резюме/Резюме Юлия Устинова Аналитик данных.docx'

gfile = drive.CreateFile({
    'title': ['Резюме Юлия Устинова Аналитик данных.docx'],
    'parents': [{'id': folder_id}]
    })
gfile.SetContentFile(upload_file)
gfile.Upload()
