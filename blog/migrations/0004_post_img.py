# Generated by Django 3.0.1 on 2020-05-15 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default=0, upload_to='postimg'),
            preserve_default=False,
        ),
    ]