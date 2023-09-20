from django.contrib import admin

from users.models import CustomUsers, Fields, MappedFields, Grades, Streams

# Register your models here.

admin.site.register(CustomUsers)

admin.site.register(Fields)

admin.site.register(MappedFields)

admin.site.register(Grades)

admin.site.register(Streams)

