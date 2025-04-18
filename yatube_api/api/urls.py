from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as views_authtoken

from . import views

router = routers.DefaultRouter()
router.register('posts', views.PostViewSet)
router.register(r'^posts/(?P<post_id>\d+)/comments',
                views.CommentViewSet, basename='comments')
router.register('groups', views.GroupViewSet)
router.register('follow', views.FollowingViewSet, basename='follower')


urlpatterns = [
    path('v1/api-token-auth/', views_authtoken.obtain_auth_token),
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
