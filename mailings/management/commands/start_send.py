import smtplib
from django.core.mail import send_mail
from django.core.management import BaseCommand
from config import settings
from mailings.models import Mailing, MailingAttempt


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        mailings = Mailing.objects.filter(status__in=['Created', 'Launched'], is_active=True)
        for mailing in mailings:
            mailing.status = 'Launched'
            mailing.save()

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

            except smtplib.SMTPException as error:
                # При ошибке отправки записываем полученный ответ сервера
                MailingAttempt.objects.create(status='Ошибка отправки', answer=error, mailing=mailing)
