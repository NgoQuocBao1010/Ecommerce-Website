from django.db.models.signals import post_save
from .models import Order

# from django.conf import settings
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags

# def orderSuccessEmail(sender, instance=None, created=False, **kwargs):
#     if created and instance.user:
#         adminEmail = settings.EMAIL_HOST_USER
#         userEmail = instance.user.email

#         htmlContent = render_to_string('newOrder.html', {"order": instance})
#         textContent = strip_tags(htmlContent)

#         subject = "Footco - Order Successfully"
#         msg = EmailMultiAlternatives(subject, textContent, adminEmail, to=[userEmail, ])
#         msg.attach_alternative(htmlContent, "text/html")
#         msg.send()

# post_save.connect(orderSuccessEmail, sender=Order)