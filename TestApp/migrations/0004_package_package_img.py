# Generated by Django 5.1.7 on 2025-04-09 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0003_rename_reviwer_name_review_reviewer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='package_img',
            field=models.ImageField(default='package_pic/default.jpg', upload_to='package_pic'),
        ),
    ]
