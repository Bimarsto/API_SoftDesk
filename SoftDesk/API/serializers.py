from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Project, Issue, Comment, User, Contributor


class UserSignupSerializer(ModelSerializer):

    tokens = SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'tokens']

    @staticmethod
    def validate_password(value):
        if value is not None:
            return make_password(value)
        raise ValidationError("Password is empty")

    @staticmethod
    def get_tokens(instance):
        tokens = RefreshToken.for_user(instance)
        data = {
            'refresh': str(tokens),
            'access': str(tokens.access_token)
        }
        return data


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


class ProjectListSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'type',
            'author_user_id',
        ]


class ProjectDetailSerializer(ModelSerializer):

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
        serializer = IssueListSerializer(queryset, many=True)
        return serializer.data


class IssueListSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = [
            'id',
            'title',
            'tag',
            'priority',
            'status',
            'assignee_user_id',
            'author_user_id'
        ]


class IssueDetailSerializer(ModelSerializer):

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
        serializer = CommentListSerializer(queryset, many=True)
        return serializer.data


class CommentListSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'id',
            'description',
            'issue_id'
        ]


class CommentDetailSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'id',
            'description',
            'author_user_id',
            'issue_id',
            'created_time',
        ]

