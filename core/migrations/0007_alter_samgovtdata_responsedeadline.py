# Generated by Django 4.1.5 on 2023-01-13 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_samgovtdata_active_alter_samgovtdata_award_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samgovtdata',
            name='responseDeadLine',
            field=models.CharField(max_length=255, null=True),
        ),
    ]