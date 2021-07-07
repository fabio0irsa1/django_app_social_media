from django.db import models
from django.contrib.auth.models import User

    # Create your models here.
class UserProfileInfo(models.Model):

        # Create relationship (don't inherit from User!)
        user = models.OneToOneField(User, on_delete=models.CASCADE)

        # Add any additional attributes you want
        first_name = models.CharField(max_length=150, blank=True)
        last_name = models.CharField(max_length=150, blank=True)
        bio = models.TextField(max_length=500, blank=True)
        location = models.TextField(max_length=250, blank=True)
        birth_date = models.DateField(null=True, blank=True)
        profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
        website_link = models.URLField(blank=True)

        # pip install pillow to use this!
        # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
        profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

        def __str__(self):
            # string representation of user
            # user comes with a username attribute
            return "@{}".format(self.user.username)
