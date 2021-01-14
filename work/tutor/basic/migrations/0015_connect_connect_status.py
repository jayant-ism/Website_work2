# Generated by Django 3.1.4 on 2021-01-14 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0014_class_details_level_rating_user_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='connect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connect_id', models.IntegerField()),
                ('class_id', models.IntegerField()),
                ('student_id', models.IntegerField()),
                ('teacher_id', models.IntegerField()),
                ('connect_status', models.IntegerField()),
                ('connect_seek_rating', models.IntegerField()),
                ('connect_teach_rating', models.IntegerField()),
                ('connect_rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='connect_status',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('connect_status', models.CharField(max_length=15)),
            ],
        ),
    ]
