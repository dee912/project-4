# Generated by Django 3.2.4 on 2021-06-21 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0011_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.RemoveField(
            model_name='store',
            name='category',
        ),
        migrations.AddField(
            model_name='store',
            name='category',
            field=models.CharField(blank=True, max_length=50, verbose_name='category'),
        ),
    ]