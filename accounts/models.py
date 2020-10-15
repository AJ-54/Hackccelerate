from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.conf import settings 
FEES = [1000*i for i in range(1,13)]

class User(AbstractUser) :
    class Role(models.TextChoices) :
        STUDENT = "S" ,_("Student")
        PARENT = "P" ,_("Parent")
        TEACHER = "T",_("Teacher")

    role = models.CharField(max_length = 255,choices=Role.choices)


class Parent(models.Model) :
    user = models.OneToOneField(settings.AUTH_USER_MODEL,null=True,on_delete=models.CASCADE)
    @property
    def total_fees_to_be_paid(self) :
        for child in self.children.all():
            fees+= child.fess
        return fees
        



class Student(models.Model) :
    user = models.OneToOneField(settings.AUTH_USER_MODEL,null=True,on_delete=models.CASCADE)
    roll_no = models.IntegerField(max_length=20,unique=True)
    parent = models.ForeignKey(Parent,related_name="children",null=True,on_delete=models.CASCADE)
    standard = models.IntegerField(default =1)
    is_fees_paid = models.BooleanField(default = False)
    date_of_joining = models.DateField(default =timezone.now)


    @property
    def fees(self) :
        return  0 if self.fess_is_paid else Fess[self.standard]


class Teacher(models.Model) :
    user = models.OneToOneField(settings.AUTH_USER_MODEL,null=True,on_delete=models.CASCADE)
    position = models.CharField(max_length=255,blank=True)
    department = models.CharField(max_length=255,blank=True)
    date_of_joining = models.DateField(default=timezone.now)
