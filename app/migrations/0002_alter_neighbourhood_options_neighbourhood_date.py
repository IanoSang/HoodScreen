# Generated by Django 4.0.5 on 2022-06-20 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='neighbourhood',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
