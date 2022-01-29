from email import message
from celery import shared_task
from datetime import *
from django.core.mail import send_mail


from django.conf import settings
@shared_task
def email():
    print('hello print now')
    subject = 'this is celery time task email '
    message = 'Hi thank you for using celery'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['bhavesh.sharma@datenwissen.com',]
    send_mail(subject , message , email_from , recipient_list)
    # return 'email has been send it'


