from django.db import models

# Create your models here.
class Users(models.Model):
    employee_id = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    ranking = models.FloatField()

def upload_photo(self,filename):
    path= 'hrm/photo/{}'.filename
    return path
def upload_file(self,filename):
    path= 'hrm/file/{}'.filename
    return path

