# Generated by Django 4.0.3 on 2022-04-06 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0002_member_firstname_member_surname_alter_member_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': 'Member', 'verbose_name_plural': 'Members'},
        ),
        migrations.AlterModelManagers(
            name='member',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='username',
        ),
    ]