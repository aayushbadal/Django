from django.urls import path

from .views import (
    HomePage,
    BlogPage,
    BlogDetailPage,
)

# Create your tests here.

urlpatterns = [
    # path(),
    path("", HomePage.as_view(), name="index"),
    path("blogs/", BlogPage.as_view(), name="blogs"),
    path("blog/<int:pk>/", BlogDetailPage.as_view(), name="blog_detail"),
]
