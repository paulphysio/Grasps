# Generated by Django 3.2.12 on 2022-04-17 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grasps', '0005_alter_sign_up_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(default='', max_length=200)),
                ('subject', models.CharField(default='', max_length=200)),
                ('message', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Sign_Up',
        ),
    ]
