from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Project, Issue, Comment, Contributor
from .serializers import ProjectListSerializer, ProjectDetailSerializer,\
    IssueListSerializer, IssueDetailSerializer, \
    CommentListSerializer, CommentDetailSerializer, \
    ContributorSerializer, UserSignupSerializer
from .permissions import ProjectPermission, IssuePermission, CommentPermission


class SignupViewSet(APIView):

    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ProjectViewSet(ModelViewSet):

    permission_classes = [ProjectPermission]
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class ContributorViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.all()


class IssueViewSet(ModelViewSet):

    permission_classes = [IssuePermission]
    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer

    def get_queryset(self):
        return Issue.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class CommentViewSet(ModelViewSet):

    permission_classes = [CommentPermission]
    serializer_class = CommentListSerializer
    detail_serializer_class = CommentDetailSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()
