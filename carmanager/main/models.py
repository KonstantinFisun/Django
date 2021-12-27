from django.db import models
#
class Type_transport(models.Model):
    title = models.CharField('Название типа транспорта', max_length = 50)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/Type{self.id}'

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

class Firm(models.Model):
    title = models.CharField('Название фирмы', max_length = 50)
    country = models.CharField('Название страны', max_length=50)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/Firm/{self.id}'

    class Meta:
        verbose_name = 'Фирма'
        verbose_name_plural = 'Фирмы'

class Transport(models.Model):
    id_firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    id_type = models.ForeignKey(Type_transport, on_delete=models.CASCADE)
    model = models.CharField('Название модели', max_length=50)
    weight = models.CharField('Вес', max_length = 50)
    power = models.CharField('Мощность', max_length=50)

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return f'/Transport/{self.id}'

    class Meta:
        verbose_name = 'Транспорт'
        verbose_name_plural = 'Транспорта'

# class Task(models.Model):
#     title = models.CharField('Название', max_length = 50)
#     task = models.TextField('Описание')
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Задача'
#         verbose_name_plural = 'Задачи'
