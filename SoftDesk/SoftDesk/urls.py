from django.contrib import admin
from django.urls import include, path
from rest_framework_nested import routers

from API.views import ProjectViewSet, IssueViewSet, CommentViewSet,\
    ContributorViewSet, SignupViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

project_router = routers.SimpleRouter()
project_router.register('projects', ProjectViewSet, basename='projects')

issue_router = routers.NestedSimpleRouter(project_router, 'projects', lookup='project_id')
issue_router.register('issues', IssueViewSet, basename='issues')

comment_router = routers.NestedSimpleRouter(issue_router, 'issues', lookup='issue_id')
comment_router.register('comments', CommentViewSet, basename='comments')

contributor_router = routers.NestedSimpleRouter(project_router, 'projects', lookup='project_id')
contributor_router.register('users', ContributorViewSet, basename='users')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/signup/', SignupViewSet.as_view(), name='signup'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(project_router.urls)),
    path('api/', include(issue_router.urls)),
    path('api/', include(comment_router.urls)),
    path('api/', include(contributor_router.urls)),
]
