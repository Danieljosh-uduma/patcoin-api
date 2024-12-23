from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100, null=False, unique=True)
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return str(self.username)
    

class ReferralCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=150)



class UserReferral(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    referral_link = models.URLField()

    def __str__(self):
        return f'{self.user} referral'


class ReferralRelationship(models.Model):
    inviter = models.ForeignKey(User, related_name='inviter', on_delete=models.CASCADE)
    invited = models.ForeignKey(User, related_name='invited', on_delete=models.CASCADE)
    refer_token = models.ForeignKey(ReferralCode, verbose_name='Referral_code', on_delete=models.CASCADE)
