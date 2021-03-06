# Generated by Django 4.0 on 2021-12-30 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actividad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('activity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='actividad.actividad')),
            ],
        ),
    ]
