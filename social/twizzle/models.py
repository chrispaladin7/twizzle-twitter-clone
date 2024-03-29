from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create Profile Model.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    follows = models.ManyToManyField("self",
        related_name="followed_by",
        symmetrical=False,
        blank=True)


    def __str__(self) -> str:
        return self.user.username
    
#Create Profile when New User Signs Up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user = instance)
        user_profile.save()
        #Have user Follow themselves
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

post_save.connect(create_profile,sender=User)

