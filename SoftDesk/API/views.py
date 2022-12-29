from rest_framework.exceptions import NotFound
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
        if self.action in ['retrieve', 'create', 'update']:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ContributorViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = ContributorSerializer

    def get_queryset(self, *args, **kwargs):
        project_id = self.kwargs.get('project_id_pk')
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            raise NotFound('A Project with that id does not exist')
        return Contributor.objects.filter(project_id=project)

    def destroy(self, request, *args, **kwargs):
        project_id = self.kwargs.get('project_id_pk')
        user_id = self.kwargs.get('pk')
        contributor = Contributor.objects.filter(project_id=project_id, user_id=user_id)
        if contributor:
            contributor.delete()
            return Response({'message': 'contributor has been deleted'})
        else:
            return Response({'message': 'This contributor does not exist'})


class IssueViewSet(ModelViewSet):

    permission_classes = [IssuePermission]
    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer

    def get_queryset(self, *args, **kwargs):
        project_id = self.kwargs.get('project_id_pk')
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            raise NotFound('A Project with that id does not exist')
        return Issue.objects.filter(project_id=project)

    def get_serializer_class(self):
        if self.action in ['retrieve', 'create', 'update']:
            return self.detail_serializer_class
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data['author_user_id'] = request.user.id
        if not request.data['assignee_user_id']:
            request.data["assignee_user_id"] = request.user.id
        project_id = self.kwargs.get('project_id_pk')
        project = Project.objects.get(id=project_id)
        request.data['project_id'] = project.id
        request.POST._mutable = False
        return super().create(request, *args, **kwargs)


class CommentViewSet(ModelViewSet):

    permission_classes = [CommentPermission]
    serializer_class = CommentListSerializer
    detail_serializer_class = CommentDetailSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def get_serializer_class(self):
        if self.action in ['retrieve', 'create', 'update']:
            return self.detail_serializer_class
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data['author_user_id'] = request.user.id
        issue_id = self.kwargs.get('issue_id_pk')
        issue = Issue.objects.get(id=issue_id)
        request.data['issue_id'] = issue.id
        request.POST._mutable = False
        return super().create(request, *args, **kwargs)
