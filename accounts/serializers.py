from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "problems_solved",
            "total_points",
            "created_at",
            "authorDetails",
        ]
        read_only_fields = [
            "id",
            "problems_solved",
            "total_points",
            "created_at",
        ]
