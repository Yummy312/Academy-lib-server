from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='', null=True, blank=True, verbose_name="Изображение")
    view_count = models.PositiveIntegerField(default=0)  # Поле для счетчика просмотров
    publisher = models.CharField(max_length=100, null=True, blank=True, verbose_name="Издательство")
    publication_type = (models.CharField
                        (max_length=100,
                         null=True,
                         blank=True,
                         default="Электронные учебники",
                         verbose_name="Тип издания",
                         ))
    publication_year = models.PositiveIntegerField(null=True, blank=True, verbose_name="Год издания")
    authors = models.CharField(max_length=100, null=True, blank=True, verbose_name="Авторы")

    def __str__(self):
        return self.title

    @property
    def category_name(self):
        return str(self.category)

    @property
    def category_id(self):
        return str(self.category.id)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
