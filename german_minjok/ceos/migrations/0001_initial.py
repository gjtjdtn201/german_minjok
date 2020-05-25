# Generated by Django 2.1.15 on 2020-05-25 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_condition', models.IntegerField(choices=[(0, '신청'), (1, '준비'), (2, '완료')], default=0)),
                ('order_location', models.CharField(max_length=100)),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('order_name', models.CharField(max_length=50)),
                ('order_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PlusMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plus_name', models.CharField(max_length=50)),
                ('plus_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=50)),
                ('store_phone', models.CharField(max_length=20)),
                ('store_number', models.CharField(max_length=20)),
                ('store_location', models.CharField(max_length=100)),
                ('store_cartegory', models.IntegerField(choices=[(0, '한식'), (1, '중국집'), (2, '일식'), (3, '피자'), (4, '치킨')], default=0)),
                ('store_image', models.ImageField(blank=True, upload_to='store/%Y/%m/%d')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('orderlists', models.ManyToManyField(related_name='restaurant', through='ceos.OrderList', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StoreMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=50)),
                ('menu_info', models.CharField(blank=True, max_length=50)),
                ('menu_price', models.IntegerField()),
                ('menu_image', models.ImageField(blank=True, upload_to='menu/%Y/%m/%d')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ceos.Store')),
            ],
        ),
    ]
