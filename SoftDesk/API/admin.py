from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Contributor, Project, Issue, Comment


class ProjectAdmin(admin.ModelAdmin):

    list_display = ('title', 'type', 'author_user_id')


class IssueAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'project_id',
        'priority',
        'tag',
        'status',
        'assignee_user_id',
        'author_user_id',
    )


class CommentAdmin(admin.ModelAdmin):

    list_display = ('author_user_id', 'issue_id', 'description')


admin.site.register(User, UserAdmin)
admin.site.register(Contributor)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)
