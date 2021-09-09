from celery import shared_task
from django.core.mail import send_mail
from celery.utils.log import get_task_logger


@shared_task
def send_reset_form(user, subject, plain_message):
    from_email = 'admin@ilvits.com'
    to = user.email
    logger = get_task_logger(__name__)
    mail_sent = send_mail(subject, plain_message, from_email, [to])
    logger.info("*** Sent reset form ***")
    return mail_sent
