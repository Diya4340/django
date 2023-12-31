# Generated by Django 4.2.4 on 2023-09-15 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_leave_apply_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_id', models.IntegerField()),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Leave_status',
        ),
    ]
