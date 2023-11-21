from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'

v1_router = routers.DefaultRouter()
v1_router.register(r'posts/(?P<post_id>[1-9]\d*)/comments',
                   CommentViewSet,
                   basename='comments')
v1_router.register(r'posts', PostViewSet)
v1_router.register(r'groups', GroupViewSet)
v1_router.register(r'follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('', include(v1_router.urls)),
    path('', include('djoser.urls.jwt')),
]
