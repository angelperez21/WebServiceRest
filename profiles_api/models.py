from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin

class UserProfile (AbstractUser,PermissionsMixin):
    """ Modelo Base de Datos para usarios en el sistema """
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(sel):
        '''Obtener nombre completo del usuario'''
        return self.name
    
    def get_short_name(sel):
        '''Obtener el nombre corto del usuario'''
        return self.name

    def __str__ 