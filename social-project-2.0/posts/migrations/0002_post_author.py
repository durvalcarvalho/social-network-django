# Generated by Django 4.0.4 on 2022-06-03 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_profile_avatar'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='profiles.profile'),
            preserve_default=False,
        ),
    ]
