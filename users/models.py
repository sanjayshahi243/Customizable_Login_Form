from django.db import models
from django.db.models.query import QuerySet

# Create your models here.

from django.contrib.sites.models import Site
from django.contrib.auth.models import AbstractUser, User


class Grades(models.Model):
    
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Streams(models.Model):
    
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CustomUsers(AbstractUser):
    designation = models.TextField(max_length=255, blank=True, null=True)
    grades = models.ManyToManyField(Grades, related_name="user_grades", blank=True, null=True)
    streams = models.ManyToManyField(Streams, related_name="user_streams", blank=True, null=True)


# class UserGrade(models.Model):

#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
#     grades = models.ForeignKey(Grades, on_delete=models.CASCADE, related_name="grades")

class FieldsManager(models.Manager):

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_deleted=False)

        
class Fields(models.Model):

    field_name = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    objects: FieldsManager = FieldsManager()  # Attach the custom manager to the model

    def __str__(self) -> str:
        return self.field_name


class MappedFields(models.Model):

    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="sites")
    field = models.ForeignKey(Fields, on_delete=models.CASCADE, related_name="fields")
    is_enabled = models.BooleanField(default=False)
    is_required = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.site} - {self.field}"


