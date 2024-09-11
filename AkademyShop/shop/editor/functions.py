
from django.core.files.storage import default_storage

def UploadFileToDB(f):
    with default_storage.open('editor/static/images/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)