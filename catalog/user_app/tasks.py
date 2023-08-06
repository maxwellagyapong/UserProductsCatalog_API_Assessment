from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_password_reset_email(email, reset_url):
    subject = 'Password Reset'
    message = f'Click the following link to reset your password: {reset_url}. This email was sent to you because, you requested to reset your password, if this was not you, ignore.'
    from_email = 'maxwellamoakoagyapong@gmail.com'
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)