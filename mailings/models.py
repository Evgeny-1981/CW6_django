from django.db import models

from users.models import User
from django.utils import timezone

NULLABLE = {"blank": True, "null": True}
Frequency_of_mailing = [("Daily", "Ежедневно"), ("Weekly", "Еженедельно"), ("Monthly", "Ежемесячно")]
Mailing_status = [("Completed", "Завершена"), ("Created", "Создана"), ("Launched", "Запущена")]
Permissions = [('View_any_mailing_lists', 'Просматривать любые рассылки'),
               ('Disable_mailing_lists', 'Отключать рассылки'), ]
Attempt_status = [("Succses", "Успешно"), ("Fail", "Неуспешно"), ]


class Client(models.Model):
    """Модель для клиента"""
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    fio = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)
    owner_client = models.ForeignKey(User, verbose_name="Чей клиент", related_name="clients", on_delete=models.SET_NULL,
                                     **NULLABLE, )

    class Meta:
        db_table = "client"
        verbose_name = "Клиента"
        verbose_name_plural = "Клиенты"
        ordering = ("email", "owner_client",)

    def __str__(self):
        return f"Клиент: {self.fio}, {self.email}"


class Message(models.Model):
    """Модель для сообщений"""
    subject = models.CharField(max_length=120, verbose_name="Тема письма", )
    message = models.TextField(verbose_name="Сообщение", )
    owner_message = models.ForeignKey(User, verbose_name="Автор сообщения", related_name="messages",
                                      on_delete=models.SET_NULL, **NULLABLE, )

    class Meta:
        db_table = "message"
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ("subject", "owner_message",)

    def __str__(self):
        return f"{self.subject}"


class Mailing(models.Model):
    """Модель для рассылки"""
    start_mailing = models.DateTimeField(default=timezone.now, verbose_name="Дата и время первой отправки")
    owner_mailing = models.ForeignKey(User, related_name="mailings", verbose_name="Автор рассылки",
                                      on_delete=models.SET_NULL, **NULLABLE, )
    message = models.ForeignKey(Message, verbose_name="Сообщение для рассылки", on_delete=models.CASCADE)
    frequency = models.CharField(max_length=15, choices=Frequency_of_mailing, verbose_name="Периодичность рассылки")
    status = models.CharField(max_length=10, choices=Mailing_status, default="created",
                              verbose_name="Статус рассылки", )
    clients = models.ManyToManyField(Client, verbose_name="Получатели рассылки")
    is_active = models.BooleanField(default=True, verbose_name="Актуальность рассылки")

    class Meta:
        db_table = "mailing"
        verbose_name = "Рассылку"
        verbose_name_plural = "Рассылки"
        ordering = ("start_mailing", "status",)
        permissions = Permissions

    def __str__(self):
        return f"Рассылка: {self.pk}. Время: {self.start_mailing}. Статус: {self.status}"


class MailingAttempt(models.Model):
    """Модель для отчета о рассылках"""
    data_mailing = models.DateTimeField(auto_now=True, verbose_name="Дата и время рассылки", )
    status = models.CharField(max_length=120, choices=Attempt_status, verbose_name="Статус рассылки", )
    answer = models.TextField(verbose_name="Ответ сервера", **NULLABLE, )
    mailing = models.ForeignKey(Mailing, verbose_name="Рассылка", on_delete=models.CASCADE, )
    owner_mailing = models.ForeignKey(User, verbose_name="Владелец рассылки", on_delete=models.SET_NULL, **NULLABLE)

    class Meta:
        db_table = "MailingAttempt"
        verbose_name = "Отчет о рассылке"
        verbose_name_plural = "Отчеты о рассылках"
        ordering = ("status", "answer", "owner_mailing",)

    def __str__(self):
        return f"{self.data_mailing}, {self.status}, {self.answer}"
