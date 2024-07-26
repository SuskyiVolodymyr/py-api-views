from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from cinema.models import (
    Actor,
    CinemaHall,
    Genre,
    Movie,
)


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(read_only=True, many=True)
    genres = GenreSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = "__all__"


class CinemaHallSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    rows = serializers.IntegerField()
    seats_in_row = serializers.IntegerField()

    def create(self, validated_data):
        return CinemaHall.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.rows = validated_data.get("rows", instance.rows)
        instance.seats_in_row = validated_data.get(
            "seats_in_row",
            instance.seats_in_row
        )
        instance.save()

        return instance
