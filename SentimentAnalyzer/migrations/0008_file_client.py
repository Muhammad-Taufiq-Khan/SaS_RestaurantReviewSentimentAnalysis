# Generated by Django 3.2.4 on 2021-07-10 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SentimentAnalyzer', '0007_rename_username_client_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SentimentAnalyzer.client'),
        ),
    ]