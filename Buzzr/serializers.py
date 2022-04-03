from django.db.models.query import QuerySet
from rest_framework import serializers
from .models.user import User

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'display_name', 'role']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, data):
        password = data.pop('password', None)
        instance = self.Meta.model(**data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['state']