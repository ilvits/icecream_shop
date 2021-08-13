from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from celery.utils.log import get_task_logger
from django.conf import settings


@shared_task
def send_contact_form(user, email, message):
    subject = 'Сообщение с сайта'
    html_message = render_to_string('message_mail_template.html',
                                    {'user': user,
                                     'message': message
                                     })
    plain_message = strip_tags(html_message)
    from_email = 'Наклейки <admin@ilvits.com>'
    to = email
    logger = get_task_logger(__name__)
    mail_sent = send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    logger.info("Sent contact form e-mails ;)")
    return mail_sent
