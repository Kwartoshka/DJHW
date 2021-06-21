# Generated by Django 3.2 on 2021-05-24 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_tag_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='main',
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='articles', to='articles.Tag'),
        ),
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(verbose_name='Основной')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.tag')),
            ],
        ),
    ]
