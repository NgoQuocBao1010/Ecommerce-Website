from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import Profile

User = get_user_model()

def createAuthToken(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


def createProfile(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def sendConfirmationEmail(sender, instance=None, created=False, **kwargs):
    if created:
        adminEmail = settings.EMAIL_HOST_USER
        userEmail = instance.email

        htmlContent = render_to_string('welcome.html', {})
        textContent = strip_tags(htmlContent)

        subject = "Footco - Confirm account"
        msg = EmailMultiAlternatives(subject, textContent, adminEmail, to=[userEmail, ])
        msg.attach_alternative(htmlContent, "text/html")
        msg.send()


post_save.connect(createAuthToken, sender=User)
post_save.connect(createProfile, sender=User)
post_save.connect(sendConfirmationEmail, sender=User)