# Generated by Django 3.2.4 on 2021-07-27 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0007_alter_courses_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_content',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_price',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_title',
            field=models.CharField(max_length=50),
        ),
    ]
