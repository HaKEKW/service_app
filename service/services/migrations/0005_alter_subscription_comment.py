# Generated by Django 3.2.16 on 2023-03-20 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20230319_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='comment',
            field=models.CharField(db_index=True, default='', max_length=50),
        ),
    ]