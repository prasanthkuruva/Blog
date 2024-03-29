# Generated by Django 3.2.8 on 2021-10-31 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('post', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Blog',
                'ordering': ['-date_added'],
            },
        ),
    ]
