from rest_framework.permissions import BasePermission
from .models import Contributor


def is_author(user, obj):
    return user == obj.author_user_id


def is_contributor(user, project):
    for contributor in Contributor.objects.filter(project_id=project.id):
        if user == contributor.user.id:
            return True
    return False


class ProjectPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action in ['retrieve', 'list', 'create', 'update', 'partial_update', 'destroy']:
            return is_author(request.user, obj)
        if view.action in ['retrieve', 'list']:
            return is_contributor(request.user, obj)


class ContributorPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            if view.action in ['retrieve', 'list', 'create', 'update', 'partial_update', 'destroy']:
                return is_author(request.user, obj)
            if view.action in ['retrieve', 'list']:
                return is_contributor(request.user, obj)


class IssuePermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            if view.action in ['retrieve', 'list', 'create', 'update', 'partial_update', 'destroy']:
                return is_author(request.user, obj)
            if view.action in ['retrieve', 'list', 'create']:
                return is_contributor(request.user, obj.project_id)


class CommentPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            if view.action in ['retrieve', 'list', 'create', 'update', 'partial_update', 'destroy']:
                return is_author(request.user, obj)
            if view.action in ['retrieve', 'list', 'create']:
                return is_contributor(request.user, obj.issue_id.project_id)

