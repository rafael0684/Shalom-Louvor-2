# Generated by Django 4.1 on 2022-08-25 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_artista', models.CharField(max_length=200)),
                ('artista_pic', models.ImageField(blank=True, upload_to='cover_pic')),
            ],
        ),
    ]