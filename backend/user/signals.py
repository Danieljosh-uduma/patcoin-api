from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import User, ReferralCode 
import uuid

@receiver(post_save, sender=User)
def create_user_refferal_token(sender, instance, created, *args, **kwargs):
    user = instance
    if created:
        num = uuid.uuid4().uuid[:14]
        token = f'{user.username}24/{num}-patcoin.token/referral'
        ReferralCode.objects.create(
            user=user, 
            token=token
        )