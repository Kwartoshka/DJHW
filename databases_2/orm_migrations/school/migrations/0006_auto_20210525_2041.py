# Generated by Django 3.2 on 2021-05-25 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_auto_20210525_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, to='school.teacher'),
        ),
    ]