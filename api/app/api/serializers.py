from rest_framework import serializers
from app.models import User, Record

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk',
            'created',
            'first_name',
            'last_name'
        ]

    def validate_first_name(self, value):
        qs = User.objects.filter(first_name__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("User exists")
        return value

    def create(self, validated_data):
        return User.objects.create(**validated_data)

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = [
            'pk',
            'created',
            'title',
            'artist',
            'genre',
            'year',
            'quanity_available'
        ]

    def create(self, validated_data):
        return Record.objects.create(**validated_data)