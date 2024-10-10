from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie, Person

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['nconst', 'primary_name', 'birth_year', 'primary_profession']

class MovieSerializer(serializers.ModelSerializer):
    people_associated = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['primary_title', 'start_year', 'title_type', 'genres', 'people_associated']

    def get_people_associated(self, obj):
        people = Person.objects.filter(known_for_titles__contains=obj.tconst)
        return PersonSerializer(people, many=True).data
