from django.contrib.auth.models import User
from django.db import models

from App.models import Role, Client, ServiceCompany


class User_Auth(models.Model):
    user_auth = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    role_auth = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
    client_auth = models.ForeignKey(Client, on_delete=models.DO_NOTHING, null=True, blank=True)
    serviceCompany_auth = models.ForeignKey(ServiceCompany, on_delete=models.DO_NOTHING, null=True, blank=True)
