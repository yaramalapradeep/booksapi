# Generated by Django 4.0.6 on 2022-07-07 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=30)),
                ('esal', models.CharField(max_length=64)),
                ('eaddr', models.CharField(max_length=64)),
            ],
        ),
    ]
