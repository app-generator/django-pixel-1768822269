# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Car(models.Model):

    #__Car_FIELDS__
    tyres = models.CharField(max_length=255, null=True, blank=True)
    colour = models.ForeignKey(Tyres, on_delete=models.CASCADE)

    #__Car_FIELDS__END

    class Meta:
        verbose_name        = _("Car")
        verbose_name_plural = _("Car")


class Tyres(models.Model):

    #__Tyres_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    type = models.TextField(max_length=255, null=True, blank=True)

    #__Tyres_FIELDS__END

    class Meta:
        verbose_name        = _("Tyres")
        verbose_name_plural = _("Tyres")



#__MODELS__END
