from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManagerU(BaseUserManager):
    """ Manager para perfiles de usuario """

    #Con esta función permitiremos la creación de usuario desde linea de comandos
    def create_user(self, email, name, passwd=None):
        ''' Creación de nuevo user profile '''
        if not email:
            raise ValueError('El usuario debe tener un Email')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(passwd)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, name, passwd):
        user = self.create_user(email, name, passwd)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

        return user

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

    def __str__(self):
        ''' Regresamos una cadena de representación de nuestro usuario'''
        return self.email   