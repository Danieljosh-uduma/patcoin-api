from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.db.models.signals import post_save, pre_save
from .models import User, Profile
import uuid



@receiver(post_save, sender=User)
# Signal to create a referral token for a new user upon saving
def create_user_refferal_token(sender, instance, created, *args, **kwargs):
    """
    Signal handler to create a referral token for a new user upon creation.
    Args:
        sender (Model): The model class that sent the signal.
        instance (User): The actual instance being saved.
        created (bool): A boolean indicating whether a new record was created.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.
    Returns:
        None
    """
    
    user = instance
    try:
        ref = user.referral_code
        obj = Profile.objects.get(code__iexact=ref)
        obj = User.objects.get(username=obj)
    except:
        obj = None

    if created:
        num = str(uuid.uuid4())
        token = f'{user.username}-{num}-patcoin.token-referral'
        Profile.objects.create(
            user=user, 
            code=token,
            recommended_by=obj
        )