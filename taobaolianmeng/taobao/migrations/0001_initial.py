# Generated by Django 2.1.5 on 2019-07-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='商品名称')),
                ('price', models.IntegerField(verbose_name='商品价格')),
            ],
        ),
    ]
