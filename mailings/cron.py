import datetime
import smtplib
import pytz
from django.core.mail import send_mail
from config import settings
from mailings.models import Mailing, MailingAttempt


def send_message(mailing):
    """
    Отправляет сообщение клиентам,
    содержащимся в списке рассылки и фиксирует ответ сервера,
    устанавливая дату следующей рассылки в зависимости от выбранной периодичности
    """

    try:
        response = send_mail(
            subject=mailing.message.subject,
            message=mailing.message.message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[client.email for client in mailing.clients.all()],
            fail_silently=False,
        )
        if response == 1:
            # При успешной отправке сохраняем информацию о попытке в базу данных
            mailing.status = 'Launched'
            answer = 'Успешно отправлено'
            MailingAttempt.objects.create(status='Отправлено', answer=answer, mailing=mailing)

            # Устанавливаем дату следующей отправки письма
            if mailing.frequency == 'Daily':
                mailing.start_mailing += datetime.timedelta(days=1)
            elif mailing.frequency == 'Weekly':
                mailing.start_mailing += datetime.timedelta(days=7)
            elif mailing.frequency == 'Monthly':
                mailing.start_mailing += datetime.timedelta(days=30)
            mailing.save()


    except smtplib.SMTPException as error:
        # При ошибке отправки записываем полученный ответ сервера
        MailingAttempt.objects.create(status='Ошибка отправки', answer=error, mailing=mailing)

    # else:
    #     mailing.status = 'Launched'
    #     answer = 'Не отправлено'
    #     MailingAttempt.objects.create(status='Ошибка', answer=answer, mailing=mailing)


def send_mailings():
    """
    Проверяет, какие рассылки необходимо отправить в данный момент времени,
    и осуществляет их отправку
    """
    current_datetime = datetime.datetime.now(pytz.timezone(settings.TIME_ZONE))

    # Проверяем, какие рассылки должны быть отправлены в этот момент времени и производим отправку
    mailings = Mailing.objects.filter(status__in=['Created', 'Launched'], is_active=True)

    for mailing in mailings:
        if mailing.start_mailing <= current_datetime:
            mailing.status = 'Launched'
            mailing.save()
            send_message(mailing)
