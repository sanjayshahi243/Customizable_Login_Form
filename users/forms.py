from django import forms
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUsers, Grades, Streams, MappedFields

class CustomUserForm(UserCreationForm):

    class Meta:
        model = CustomUsers
        fields = ['username', 'email', 'password1', 'password2', 'grades', 'streams']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        common_fields = ['username', 'email', 'password1', 'password2']
        # Get the current site (tenant)
        current_site = get_current_site(self)
        # Get the enabled fields for the current site
        extra_fields = MappedFields.objects.filter(site=current_site)
        enabled_fields = extra_fields.filter(is_enabled=True)

        # Create a set of field names from the enabled fields
        enabled_field_names = {field.field.field_name.lower() for field in enabled_fields}

        # Remove fields that are not in the enabled fields
        for field_name in list(self.fields.keys()):
            if field_name.lower() not in enabled_field_names and field_name.lower() not in common_fields:
                self.fields.pop(field_name)