from django.urls import path
from blog.views import home, article


urlpatterns = [
    path('', home, name='index'),
    path('single/<int:art>', article, name='article'),
]