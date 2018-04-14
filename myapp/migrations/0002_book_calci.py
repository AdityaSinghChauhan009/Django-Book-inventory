# Generated by Django 2.0.3 on 2018-04-04 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=300)),
                ('text', models.CharField(max_length=300)),
                ('created_date', models.CharField(max_length=300)),
                ('published_date', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='calci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n1', models.IntegerField(max_length=5)),
                ('n2', models.IntegerField(max_length=5)),
            ],
        ),
    ]