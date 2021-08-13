from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from celery.utils.log import get_task_logger
from django.conf import settings
from .models import Order


@shared_task
def order_created(order_id, user_email):
    """
    Задача для отправки уведомления по эл. почте при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    order_items = Order.get_order_items
    subject = 'Наклейки. Заказ номер {}'.format(order_id)
    html_message = render_to_string('mail_template.html', {'order': order, 'order_items': order_items})
    plain_message = strip_tags(html_message)
    from_email = 'Наклейки <admin@ilvits.com>'
    to = [user_email, 'ilvits@yandex.ru']
    logger = get_task_logger(__name__)
    mail_sent = send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    logger.info("Sent e-mails ;)")
    return mail_sent
