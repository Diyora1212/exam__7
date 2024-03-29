# Generated by Django 5.0.2 on 2024-02-29 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productauthor',
            name='email',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='productauthor',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]
