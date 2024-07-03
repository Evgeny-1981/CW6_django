from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Client(models.Model):
    """Модель для блога"""
    email = models.EmailField(unique=True, verbose_name='почта')
    fio = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)
    owner = models.ForeignKey(User, verbose_name="Чей клиент", related_name="clients", on_delete=models.SET_NULL,
                              **NULLABLE,)

    class Meta:
        db_table = "client"
        verbose_name = "Клиент"
        verbose_name_plural = "Клиента"
        ordering = ("email",)

    def __str__(self):
        return f"Клиент: {self.fio}, {self.email}"


class Mailing(models.Model):
    """Модель для блога"""
    title = models.CharField(max_length=120, verbose_name="заголовок", unique=True)
    slug = models.CharField(max_length=120, verbose_name="слаг", unique=True)
    content = models.TextField(verbose_name="содержимое")
    preview = models.ImageField(upload_to="blog/images", verbose_name="превью(изображение)", **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name="дата публикации")
    published = models.BooleanField(verbose_name="признак публикации", default=False)
    count_views = models.PositiveIntegerField(verbose_name="счетчик просмотров", default=0, **NULLABLE)

    class Meta:
        db_table = "blog"
        verbose_name = "блог"
        verbose_name_plural = "блоги"
        ordering = ("count_views",)

    def __str__(self):
        return f"{self.title}, {self.content}"


class Message(models.Model):
    """Модель для блога"""
    subject = models.CharField(max_length=120, verbose_name="Тема письма",)
    message = models.TextField(verbose_name="Сообщение",)
    owner = models.ForeignKey(User, verbose_name="Автор сообщения", **NULLABLE, on_delete=models.SET_NULL,)


    class Meta:
        db_table = "message"
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ("subject",)

    def __str__(self):
        return f"Тема сообщения: {self.subject}"


class MailingAttempt(models.Model):
    """Модель для блога"""
    title = models.CharField(max_length=120, verbose_name="заголовок", unique=True)
    slug = models.CharField(max_length=120, verbose_name="слаг", unique=True)
    content = models.TextField(verbose_name="содержимое")
    preview = models.ImageField(upload_to="blog/images", verbose_name="превью(изображение)", **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name="дата публикации")
    published = models.BooleanField(verbose_name="признак публикации", default=False)
    count_views = models.PositiveIntegerField(verbose_name="счетчик просмотров", default=0, **NULLABLE)

    class Meta:
        db_table = "blog"
        verbose_name = "блог"
        verbose_name_plural = "блоги"
        ordering = ("count_views",)

    def __str__(self):
        return f"{self.title}, {self.content}"
