from django.db import models
from django.contrib.auth.models import User
class product(models.Model):
    image=models.ImageField(upload_to="images")
class pollsuser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nickname=models.CharField(max_length=20,null=False)
