import logging
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from catalog.celery import app
@app.task
def send_password_reset_email(email):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.filter(email=email)
        if user.exists():
            send_mail(
                'Password Reset.',
                'Follow this link to reset your password: '
                    'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(user.verification_uuid)}),
                'from@catalogmanager.dev',
                [email],
                fail_silently=False,
            )
    except UserModel.DoesNotExist:
        logging.warning("Tried to send verification email to non-existing email '%s'" % email)