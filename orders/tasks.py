from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    """
    Задача для отправки уведомления по эл. почте при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Заказ номер {}'.format(order_id)
    message = 'Дорогой {}, \n\nВы успешно разместили заказ.\
                Номер Вашего заказа: {}.'.format(order.first_name, order_id)
    mail_sent = send_mail(subject, message, 'admin@ilvits.com', [order.email])
    return mail_sent
