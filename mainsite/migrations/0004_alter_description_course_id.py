# Generated by Django 3.2.5 on 2021-09-11 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_rename_text_description_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.course'),
        ),
    ]
