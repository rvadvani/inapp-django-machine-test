from django.urls import path
from .views import LoginView, CurrentUserView, MovieSearchAPIView, PersonSearchAPIView

urlpatterns = [
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('user/', CurrentUserView.as_view(), name='current_user'),
    path('movies/search/', MovieSearchAPIView.as_view(), name='movie-search'),
    path('persons/search/', PersonSearchAPIView.as_view(), name='person-search'),
]
