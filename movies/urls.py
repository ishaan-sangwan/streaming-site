from django.urls import path
from .views import MoviesList, MoviePull, LoginStatus, MovieTile,EmailTest, Filter
urlpatterns = [
    path('list/', MoviesList.as_view()),
    path('pull/<name>/', MoviePull.as_view()),
    path('test/', LoginStatus.as_view()),
    path('poster/<name>', MovieTile.as_view()),
    path('email_test/', EmailTest.as_view()),
    path('filter/',Filter.as_view())
]