from django.db import models
from django.conf import settings
User= settings.AUTH_USER_MODEL
class Post(models.Model):
    Name = models.CharField(max_length=30, unique=True)
    password = models.CharField( max_length=10,unique=True)

    class Meta:
        db_table = 'login1'

    def __str__(self):
        return 'Name : ' + self.Name+ 'Password : '+self.password
