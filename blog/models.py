from django.db import models
from django.utils.text import slugify
from users.models import User

NULLABLE = {"blank": True, "null": True}


class Blog(models.Model):
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
