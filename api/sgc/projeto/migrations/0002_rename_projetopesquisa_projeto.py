# Generated by Django 3.2.3 on 2021-06-02 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('projeto', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProjetoPesquisa',
            new_name='Projeto',
        ),
    ]
