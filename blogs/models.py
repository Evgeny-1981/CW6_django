from django.db import models
from django.utils.text import slugify
from users.models import User

NULLABLE = {"blank": True, "null": True}
Permissions = [('View_any_entries', 'Просматривать любые записи'),
               ('Edit_entries', 'Редактировать запись'), ]

class Blog(models.Model):
    """Модель для блога"""
    title = models.CharField(max_length=120, verbose_name="заголовок", unique=True)
    slug = models.CharField(max_length=120, verbose_name="слаг", unique=True)
    content = models.TextField(verbose_name="содержимое")
    preview = models.ImageField(upload_to="blogs/images", verbose_name="превью(изображение)", **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name="дата публикации")
    published = models.BooleanField(verbose_name="признак публикации", default=False)
    count_views = models.PositiveIntegerField(verbose_name="счетчик просмотров", default=0, **NULLABLE)
    owner_blog = models.ForeignKey(User, related_name='blogs', verbose_name='Автор статьи', on_delete=models.SET_NULL,
                                   **NULLABLE)

    class Meta:
        db_table = "blog"
        verbose_name = "блог"
        verbose_name_plural = "блоги"
        ordering = ("count_views",)
        permissions = Permissions

    def __str__(self):
        return f"{self.title}, {self.content}"
