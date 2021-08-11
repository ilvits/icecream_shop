# import hashlib
# import urllib
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# def gravatar_url(email, size=40):
#     default = "https://example.com/static/images/defaultavatar.jpg"
#     return "https://www.gravatar.com/avatar/%s?%s" % (
#         hashlib.md5(email.lower()).hexdigest(), urllib.urlencode({'d': default, 's': str(size)}))
#

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='images/profile_pictures',
        default='images/profile_pictures/default_picture.jpg',
        blank=True
    )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
