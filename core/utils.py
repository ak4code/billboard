from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .tokens import account_activation_token

def mail_confirm_new_user(site, user, email):
    mail_subject = 'Подтверждение адреса электронной почты.'
    message = render_to_string('confirm_email.html', {
        'user': user,
        'domain': site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    mail = EmailMessage(
        mail_subject, message, to=[email]
    )
    mail.send()