# Generated by Django 3.0.2 on 2020-01-27 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=30)),
                ('Option_1', models.CharField(max_length=30)),
                ('Option_2', models.CharField(max_length=30)),
                ('Option_3', models.CharField(max_length=30)),
                ('Option_4', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Quesiton',
                'verbose_name_plural': 'Quesiton',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ans', models.CharField(max_length=30)),
                ('Question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Questions.Question')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
