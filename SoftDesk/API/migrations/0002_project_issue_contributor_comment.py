# Generated by Django 4.1.3 on 2022-12-10 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1500)),
                ('type', models.CharField(choices=[('Front-end', 'front-end'), ('Back-end', 'back-end'), ('iOS', 'ios'), ('Android', 'android')], default='Front-end', max_length=10)),
                ('author_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1500)),
                ('tag', models.CharField(choices=[('Bug', 'bug'), ('Improvement', 'improvement'), ('Task', 'task')], default='Bug', max_length=15)),
                ('priority', models.CharField(choices=[('Low', 'low'), ('Medium', 'medium'), ('High', 'high')], default='Medium', max_length=10)),
                ('status', models.CharField(choices=[('To do', 'to_do'), ('In progress', 'in_progress'), ('Completed', 'completed')], default='To do', max_length=15)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('assignee_user_id', models.ForeignKey(default=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to=settings.AUTH_USER_MODEL), on_delete=django.db.models.deletion.SET_DEFAULT, related_name='assignee', to=settings.AUTH_USER_MODEL)),
                ('author_user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.project')),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('project_id', models.ManyToManyField(to='API.project')),
                ('user_id', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1500)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('author_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('issue_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.issue')),
            ],
        ),
    ]