from django.db import models
import uuid
from django.contrib.auth.models import User


# Create your models here.


class Roles(models.Model):
    class Meta():
        db_table = 'Roles'
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=225, null = False)
    status = models.BooleanField(default=True)

class UserProfile(models.Model): #adding role field with one to one mapping for user table
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roles_id = models.ForeignKey(Roles, on_delete=models.CASCADE, null = True, blank=True)
    
class Books(models.Model):
    class Meta():
        db_table = 'Books'
    id = models.UUIDField(primary_key=True)
    book_title=models.CharField(max_length=225, null = False)
    book_number=models.IntegerField(default=0)
    author=models.CharField(max_length=225, null = False)
    added_by = models.ForeignKey(User , on_delete=models.CASCADE, null = True, blank=True)
    last_modified_by = models.CharField(max_length=225, null = False)
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    return_date_min=models.DateTimeField(null=True,blank=True)
    return_date_max=models.DateTimeField(null=True,blank=True)
    return_by=models.CharField(max_length=225, null = True,blank=True)

class Student_Record(models.Model):
    class Meta():
        db_table = 'Student_Record'
    id = models.UUIDField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, db_column='user_id',null = True, blank=True)
    number_of_books=models.IntegerField(default=0)
    book_id=models.ForeignKey(Books, on_delete=models.CASCADE, db_column='book_id',null = True, blank=True)
    borrowed_date=models.DateTimeField(auto_now=True)
    renewed=models.BooleanField(default=False)
    return_date=models.DateTimeField()
    returned=models.BooleanField(default=False)
    returned_date=models.DateTimeField(null=True,blank=True)
