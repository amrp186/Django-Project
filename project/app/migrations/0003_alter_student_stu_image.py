# Generated by Django 5.1.4 on 2024-12-21 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_my_contact_student_stu_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stu_image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
