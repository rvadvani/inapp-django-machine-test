from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


from rest_framework import status
from django.db.models import Q
from .models import Movie, Person
from .serializers import MovieSerializer, PersonSerializer


class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer  

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'detail': 'Invalid credentials'}, status=401)

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)



class MovieSearchAPIView(APIView):
    """
    API View to search movies based on filters.
    """
    def get(self, request):
        movies = Movie.objects.all()

        year = request.GET.get('year')
        if year:
            movies = movies.filter(start_year=year)

        genre = request.GET.get('genre')
        if genre:
            movies = movies.filter(genres__icontains=genre)

        person_name = request.GET.get('person_name')
        if person_name:
            movies = movies.filter(Q(person__primary_name__icontains=person_name))

        title_type = request.GET.get('type')
        if title_type:
            movies = movies.filter(title_type__iexact=title_type)

        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PersonSearchAPIView(APIView):
    """
    API View to search persons based on filters.
    """
    def get(self, request):
        persons = Person.objects.all()

        movie_title = request.GET.get('movie_title')
        if movie_title:
            persons = persons.filter(Q(known_for_titles__icontains=movie_title))

        name = request.GET.get('name')
        if name:
            persons = persons.filter(primary_name__icontains=name)

        profession = request.GET.get('profession')
        if profession:
            persons = persons.filter(primary_profession__icontains=profession)

        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
