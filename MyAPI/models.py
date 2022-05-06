from django.db import models

# Create your models here.
class Daktarzuser(models.Model):
    phone_number = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=255)
    user_age = models.IntegerField(default=18)
    user_gender = models.CharField(default="male",max_length=255)
    symptom_names = models.CharField(max_length=255)
    diagnosis_name = models.CharField(max_length=255)