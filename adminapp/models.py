from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.contrib.auth.models import User
class StudentList(models.Model):
    Register_Number = models.CharField(max_length=20,unique=True)
    Name = models.CharField(max_length=100)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.Register_Number


from django.db import models
from django.core.validators import EmailValidator

class Contact(models.Model):
    name = models.CharField(max_length=100)  # Field for the name
    email = models.EmailField(validators=[EmailValidator()])  # Field for the email
    phone = models.CharField(max_length=15)  # Field for the phone number
    address = models.TextField()  # Field for the address

    def __str__(self):
        return self.name  # Display name in the admin interface

