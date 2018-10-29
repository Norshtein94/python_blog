import json

from django.db import models
from django.utils.translation import gettext as _


# Create your models here.


class UserInfo(models.Model):
    IS_SUPER_CHOICES = ((True, _('yes')), (False, _('no')))
    STATUS_CHOICES = ((0, _('normal')), (1, _('frozen')), (2, _('cancelled')))

    username = models.CharField(_('username'), max_length=20, unique=True)
    password = models.CharField(_('password'), max_length=64)
    is_super = models.BooleanField(_('is super'), choices=IS_SUPER_CHOICES)
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES)
    last_login_time = models.DateTimeField(_('last login time'), )
    create_time = models.DateTimeField(_('create time'), auto_now_add=True)
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    email = models.EmailField(_('email'), )
    mobile = models.CharField(_('mobile'), max_length=20)
    github_account = models.CharField(_('github account'), max_length=64)
    city = models.CharField(_('city'), max_length=20)
    creator_id = models.CharField(_('creator id'), max_length=20)
    update_time = models.DateTimeField(_('update time'), auto_now=True, )

    # def __str__(self):
    #     return self.username
