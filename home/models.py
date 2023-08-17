from pyexpat import model
from django.db import models
from statistics import mode
import os
# Create your models here.
import uuid
from uuid import uuid4

class Folder(models.Model):
    uid = models.UUIDField(primary_key= True, editable= False, default= uuid.uuid4)
    created_at = models.DateField(auto_now = True)

def get_upload_path(instance, filename):
    return os.path.join(str(instance.folder.uid), filename)

class Files(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_upload_path)
    created_at = models.DateField(auto_now = True)
