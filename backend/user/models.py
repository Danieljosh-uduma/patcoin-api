"""
User model that extends the AbstractUser model.
Attributes:
    username (CharField): The username of the user, must be unique and have a max length of 100 characters.
    email (EmailField): The email of the user, must be unique.
    referral_code (CharField): The referral code associated with the user, can be null or blank, with a default empty string.
    created (DateTimeField): The date and time when the user was created, automatically set on creation.
Methods:
    __str__(): Returns the string representation of the user, which is the username.
    set_referral_code(value): Sets the referral code for the user and saves the model instance.
"""
"""
Profile model that is linked to the User model.
Attributes:
    user (OneToOneField): A one-to-one relationship with the User model.
    code (CharField): The code associated with the profile, with a max length of 150 characters.
    recommended_by (ForeignKey): A foreign key to the User model, representing the user who recommended this profile, can be null or blank.
    created (DateTimeField): The date and time when the profile was created, automatically set on creation.
    updated (DateTimeField): The date and time when the profile was last updated, automatically set on update.
Methods:
    __str__(): Returns the string representation of the profile, which is the associated user.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    referral_code = models.CharField(max_length=150, null=True, blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return str(self.username)
    
    def set_referral_code(self, value):
        self.referral_code = value 
        self.save()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=150)
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='ref_by')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}'

