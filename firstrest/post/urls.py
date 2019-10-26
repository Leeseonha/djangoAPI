from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

#django rest framework는 router라고 하는 개념을 통해 url을 결정함

router = DefaultRouter()
router.register('Post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('post/', views.PostList.as_view()),
    # path('post/<int:pk>/', views.PostDetail.as_view()),

]

# urlpatterns = format_suffix_patterns(urlpatterns)