from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.db.models.signals import post_save, pre_save
from .models import User, Profile
import uuid

@receiver(pre_save, sender=User)
def check_valid_recommendation_code(sender, instance, *args, **kwargs):
    user = instance

    try:
        ref = user.recommended_by
        obj = Profile.objects.get(code__iexact=ref)
        obj = User.objects.get(username=obj)
    except:
        obj = None

    user.recommended_by = obj

@receiver(post_save, sender=User)
def create_user_refferal_token(sender, instance, created, *args, **kwargs):
    user = instance

    if created:
        num = str(uuid.uuid4())
        token = f'{user.username}-{num}-patcoin.token-referral'
        Profile.objects.create(
            user=user, 
            code=token,
            recommended_by=user.recommended_by
        )