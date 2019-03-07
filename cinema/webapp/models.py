from django.db import models
from django.urls import reverse


class SoftDeleteManager(models.Manager):
    def active(self):
        return self.filter(is_deleted=False)

    def deleted(self):
        return self.filter(is_deleted=True)


class Category(models.Model):
    name = models.CharField(max_length=30,verbose_name="Название жанра")
    description = models.TextField(max_length=500, blank=True, null=True ,verbose_name="Описание")

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000, null=True, blank=True)
    poster = models.ImageField(upload_to='posters', null=True, blank=True)
    release_date = models.DateField()
    finish_date = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    category = models.ManyToManyField(Category,verbose_name="Жанр")
    objects = SoftDeleteManager()

    def get_absolute_url(self):
        return reverse('api_v1:movie-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

class Hall(models.Model):
    name = models.CharField(max_length=30,verbose_name="Зал")

class Seat(models.Model):
    hall = models.ManyToManyField(Hall,verbose_name="Зал")
    raw = models.IntegerField(verbose_name="Номер ряда")
    pos = models.IntegerField(verbose_name="Номер места")

class Show(models.Model):
    movie = models.ManyToManyField(Movie,verbose_name="Фильм")
    hall = models.ManyToManyField(Hall,verbose_name="Зал")
    begin = models.DateTimeField(verbose_name="Начало")
    end = models.DateTimeField(verbose_name="Окончание")
    price = models.DecimalField(decimal_places = 2, max_digits=5, verbose_name="Цена")
# Create your models here.
class Sale(models.Model):
    name = models.CharField(max_length=30,verbose_name="Название")
    amount = models.DecimalField(decimal_places=2,max_digits=5,verbose_name="скидка")
    begin = models.DateField(null=True,blank=True,verbose_name="Начало")
    end = models.DateField(null=True,blank=True,verbose_name="Окончание")
class Ticket(models.Model):
    show = models.ForeignKey(Show,on_delete=models.PROTECT,verbose_name="Сеанс")
    seat = models.ForeignKey(Seat,on_delete=models.PROTECT,verbose_name="Место")
    sale = models.ForeignKey(Sale,on_delete=models.PROTECT,verbose_name="Скидка")
    returned = models.BooleanField(verbose_name="Возврат")
class Reserve(models.Model):
    code = models.CharField(max_length=30,unique=True,verbose_name="Код")
    show = models.ForeignKey(Show,on_delete=models.PROTECT,verbose_name="Сеанс")
    seats = models.ManyToManyField(Seat,verbose_name="Места")
    status = models.CharField(max_length=20,choices=(("created","создано"),("bought","выкуплено"),("cancel","отмена")),verbose_name="Статус")
    created = models.DateTimeField(auto_now=True,verbose_name="Создано")
    updated = models.DateTimeField(auto_now_add=True,verbose_name="Обновлено")
