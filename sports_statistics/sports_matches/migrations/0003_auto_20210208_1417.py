# Generated by Django 3.1.5 on 2021-02-08 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports_matches', '0002_auto_20210208_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchresults',
            name='team_one',
            field=models.CharField(max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='matchresults',
            name='team_two',
            field=models.CharField(max_length=350, null=True),
        ),
    ]