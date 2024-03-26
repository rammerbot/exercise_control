from django.db import models
from django.contrib.auth.models import BaseUserManager
from .models import *
from django.contrib.auth.hashers import check_password

class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, username, name, last_name, email, password, is_staff, is_superuser, is_active, **extra_fields):

        user = self.model(
            username = username.capitalize(),
            name = name.capitalize(),
            last_name = last_name.capitalize(),
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            is_active = is_active, 
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, name, last_name, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, False, **extra_fields)

    def create_superuser(self,username,name, last_name, email, password=None, **extra_fields):

        return self._create_user(username, name, last_name, email, password, True, True, True, **extra_fields )
    
# validar contraseña
    def password_validator(self, username):

        old_password = self.get(id=username)
        print(old_password.password)
        
        return old_password.password
         

#  validar codigo
    def code_validation(self, id, codigo):

        if self.filter(id=id, code_register=codigo).exists():
            return True