# Generated by Django 4.1.7 on 2023-04-13 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='banner',
            field=models.ImageField(upload_to='blog_posts'),
        ),
    ]
