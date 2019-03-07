# Generated by Django 2.1.5 on 2019-03-07 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_sale_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, unique=True, verbose_name='Код')),
                ('status', models.CharField(choices=[('created', 'создано'), ('bought', 'выкуплено'), ('cancel', 'отмена')], max_length=20, verbose_name='Статус')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Обновлено')),
                ('seats', models.ManyToManyField(to='webapp.Seat', verbose_name='Места')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.Show', verbose_name='Сеанс')),
            ],
        ),
    ]