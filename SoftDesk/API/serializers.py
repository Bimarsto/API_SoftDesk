from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Project, Issue, Comment, User, Contributor


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
        ]


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = [
            'id',
            'user_id',
            'project_id',
            'permission',
            'role',
        ]


class ProjectSerializer(ModelSerializer):

    issues = SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'description',
            'type',
            'author_user_id',
            'issues',
        ]

    def get_issues(self, instance):
        queryset = Issue.objects.filter(project_id=instance.id)
        serializer = IssueSerializer(queryset, many=True)
        return serializer.data


class IssueSerializer(ModelSerializer):

    comments = SerializerMethodField()

    class Meta:
        model = Issue
        fields = [
            'id',
            'title',
            'description',
            'project_id',
            'tag',
            'priority',
            'status',
            'author_user_id',
            'assignee_user_id',
            'created_time',
            'comments',
        ]

    def get_comments(self, instance):
        queryset = Comment.objects.filter(issue_id=instance.id)
        serializer = CommentSerializer(queryset, many=True)
        return serializer.data


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'id',
            'description',
            'author_user_id',
            'issue_id',
            'created_time',
        ]
