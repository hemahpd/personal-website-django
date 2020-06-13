from blog import views
from django.urls import path

urlpatterns = [
    path('blog', views.PostList.as_view(), name='blog'),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]