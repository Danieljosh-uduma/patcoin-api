from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    recommended_by = models.CharField(max_length=150, null=True, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return str(self.username)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=150)
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='ref_by')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}'


# class ReferralRelationship(models.Model):
#     inviter = models.ForeignKey(User, related_name='inviter', on_delete=models.CASCADE)
#     invited = models.ForeignKey(User, related_name='invited', on_delete=models.CASCADE)
#     refer_token = models.ForeignKey(ReferralCode, verbose_name='Referral_code', on_delete=models.CASCADE)
