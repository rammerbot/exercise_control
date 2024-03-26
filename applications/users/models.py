from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

# Create your models here.

# User model
class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M','Masculino'),
        ('F', 'Femenino'),
        ('T', 'Transgenero'),
        ('O', 'Otro')
        
    )

    username = models.CharField('Nombre de Usuario', max_length=50, unique=True)
    name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    age = models.IntegerField('Edad')
    email = models.EmailField('Correo', unique=True)
    image_profile = models.ImageField('Imagen de perfil', upload_to = 'image_profile', blank=True)
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES, blank=True)
    height = models.DecimalField('Altura',decimal_places=2, max_digits=3, blank=True, null=True)
    weight = models.DecimalField('Peso', max_digits=3, decimal_places=2, blank=True, null=True)
    chest = models.DecimalField('Pecho', max_digits=3, decimal_places=2, blank=True, null=True)
    arms = models.DecimalField('Brazos', max_digits=3, decimal_places=2, blank=True, null=True)
    waist = models.DecimalField('cintura', max_digits=3, decimal_places=2, blank=True, null=True)
    legs = models.DecimalField('Piernas', max_digits=3, decimal_places=2, blank=True, null=True)
    code_register = models.CharField('Codigo de Registro', max_length=6, blank=True)
    objects = UserManager()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS =['name','last_name', 'age','email']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.username
    