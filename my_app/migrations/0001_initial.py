# Generated by Django 3.0.7 on 2020-06-12 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=200)),
                ('deadline', models.DateTimeField(verbose_name='Time')),
                ('is_done', models.BooleanField(verbose_name='Completed')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.Categories')),
            ],
        ),
    ]
