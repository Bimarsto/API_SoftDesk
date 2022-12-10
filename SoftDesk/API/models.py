from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    pass


class Project(models.Model):
    TYPE = [
        ('Front-end', 'front-end'),
        ('Back-end', 'back-end'),
        ('iOS', 'ios'),
        ('Android', 'android')
    ]

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1500)
    type = models.CharField(max_length=10,
                            choices=TYPE,
                            default='Front-end')
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                       on_delete=models.CASCADE)


class Contributor(models.Model):
    user_id = models.ManyToManyField(User)
    project_id = models.ManyToManyField(Project)
    permission = models.CharField(max_length=50)  # choice
    role = models.CharField(max_length=50)  # char field


class Issue(models.Model):
    TAG = [
        ('Bug', 'bug'),
        ('Improvement', 'improvement'),
        ('Task', 'task'),
    ]
    PRIORITY = [
        ('Low', 'low'),
        ('Medium', 'medium'),
        ('High', 'high'),
    ]
    STATUS = [
        ('To do', 'to_do'),
        ('In progress', 'in_progress'),
        ('Completed', 'completed'),
    ]

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1500)
    tag = models.CharField(max_length=15,
                           choices=TAG,
                           default='Bug')
    priority = models.CharField(max_length=10,
                                choices=PRIORITY,
                                default='Medium')
    project_id = models.ForeignKey(to=Project,
                                   on_delete=models.CASCADE)
    status = models.CharField(max_length=15,
                              choices=STATUS,
                              default='To do')
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                       on_delete=models.SET_NULL,
                                       null=True,
                                       related_name='author')
    assignee_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                         on_delete=models.SET_DEFAULT,
                                         default=author_user_id,
                                         related_name='assignee')
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    # comment_id ?
    description = models.CharField(max_length=1500)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                       on_delete=models.CASCADE)
    issue_id = models.ForeignKey(to=Issue,
                                 on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
