from django.db import models

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name="Название")
    model = models.CharField(max_length=300, verbose_name="Модель")
    created_date = models.DateField(verbose_name="Дата выхода продукта на рынок")

    def __str__(self):
        return f"{self.title} {self.model}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class NetworkLink(models.Model):

    LEVEL = [
        (0, 'Завод'),
        (1, 'Магазин'),
        (2, 'Индивидуальный предприниматель')]

    level = models.PositiveIntegerField(choices=LEVEL, verbose_name='Структура уровней')
    email = models.EmailField(unique=True, verbose_name='Почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    street = models.CharField(max_length=50, verbose_name='Улица', **NULLABLE)
    number_house = models.CharField(max_length=100, verbose_name='Номер дома', **NULLABLE)
    provider = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Поставщик', **NULLABLE)
    indebtedness = models.FloatField(default=0.00, verbose_name='Задолженность')
    products = models.ManyToManyField(Product, default=None, verbose_name='Продукты')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    def __str__(self):
        return f'{self.level}, {self.email}'

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'
