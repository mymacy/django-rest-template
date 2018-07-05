# Models are for basic data validation, ordering and string representation

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

'''
##########################    User Profile with custom Fields
'''
class CustomUser(AbstractUser):
    '''
    extend or reduce the base user model here (eg make email required etc.)
    '''
    email = models.EmailField(max_length=255, unique=True, blank=False)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "my email: {} ist die mail vong {}".format(self.email, self.username)


class Profile(models.Model):
    '''
    This Class provides additional Fields for Users later on
    '''
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    customField1 = models.TextField(max_length=500, blank=True)
    customField2 = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return "Profile of {}".format(self.user)

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


'''
##########################    Main API Models
'''
class Rezept(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,)
    titel = models.CharField(max_length=100, blank=False)
    langerText = models.TextField(blank=True)
    booleanlol = models.BooleanField(default=False)

    def __str__(self):                                                                      # OPTIONAL toString.method
        return "{}".format(self.titel)







'''
##########################    Cheat Sheet:

DEMCHOICES = (
    ('daOne', 'ersteChoice'),
    ('daTwo', 'zweiteChoice')
)

owner = models.ForeignKey('auth.User', related_name='stocks', on_delete=models.CASCADE)
langerText = models.TextField()
booleanlol = models.BooleanField(default=False)
created = models.DateTimeField(auto_now_add=True)
updated = models.DateTimeField(auto_now=True)
publish=models.DateTimeField(default=timezone.now)
deName = models.CharField(max_length=10, blank=True, default='')
choiceslol = models.CharField(choices=DEMCHOICES, default="ersteChoice", max_length=100)
preis = models.FloatField()
volume = models.IntegerField()

def __str__(self):
    return "{}".format(self.langerText)

class Meta:
    ordering = ('created',) # , muss sein lol

'''
