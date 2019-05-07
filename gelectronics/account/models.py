from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Account(models.Model):
    user=models.OneToOneField(User,
    on_delete=models.CASCADE,related_name='account')
    dp_image=models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    birth_date=models.DateField(null=True)
