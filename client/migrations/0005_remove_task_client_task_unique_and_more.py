# Generated by Django 4.2.6 on 2023-10-11 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_alter_task_complete_date_alter_task_create_date_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='task',
            name='client_task_unique',
        ),
        migrations.RemoveConstraint(
            model_name='ticket',
            name='client_ticket_unique',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='user_id',
            new_name='userid',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='user_id',
            new_name='userid',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='user_id',
            new_name='userid',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_id',
            new_name='userid',
        ),
        migrations.AddConstraint(
            model_name='task',
            constraint=models.UniqueConstraint(fields=('userid', 'tkt_num', 'task_num'), name='client_task_unique'),
        ),
        migrations.AddConstraint(
            model_name='ticket',
            constraint=models.UniqueConstraint(fields=('userid', 'tkt_num'), name='client_ticket_unique'),
        ),
    ]