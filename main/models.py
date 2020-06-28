
from django.db import models

# Create your models here.

from django.contrib.auth.models import User
# from oauth2_provider.models import AccessToken, Application

import uuid
import os


genderChoices = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Nothing', 'Nothing'),
    ('Notspecified', 'Not Specified'))

userTypeChoices = (
    ('patient', 'Patient'),
    ('doctor', 'Physician'),
)



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True, blank=True, default='')
    last_name = models.CharField(max_length=255, null=True, blank=True, default='')
    address = models.TextField(null=True, blank=True, default='')
    gender = models.CharField(default="", choices=genderChoices, max_length=15, null=True, blank=True)
    user_type = models.CharField(choices=userTypeChoices, max_length=10, null=True, blank=True)


    active = models.BooleanField(default=True, db_index=True)
    created_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    uuid = models.CharField(max_length=50, default=uuid.uuid4, db_index=True, primary_key=True)

    def __unicode__(self):
        return unicode(self.user.username)