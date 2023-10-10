from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class BaseModel(models.Model):
    is_published = models.BooleanField(verbose_name='Опубликовано',
                                       default=True,
                                       help_text='Снимите галочку, '
                                                 'чтобы скрыть публикацию.'
                                       )
    created_at = models.DateTimeField(verbose_name='Добавлено', auto_now_add=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    title = models.CharField('Заголовок', max_length=256)
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(verbose_name='Дата и время публикации',
                                    help_text='Если установить дату и '
                                              'время в будущем — '
                                              'можно делать отложенные публикации.'
                                    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts', verbose_name='Автор публикации'
    )
    location = models.ForeignKey(
        "Location", on_delete=models.SET_NULL, null=True, related_name='posts', verbose_name='Местоположение'
    )
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, related_name='posts', verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'


class Category(BaseModel):
    title = models.CharField(verbose_name='Заголовок', max_length=256)
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(verbose_name='Идентификатор', unique=True,
                            help_text='Идентификатор страницы для URL; '
                                      'разрешены символы латиницы, цифры, дефис и подчёркивание.'
                            )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Location(BaseModel):
    name = models.CharField(max_length=256, verbose_name='Название места')

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'
