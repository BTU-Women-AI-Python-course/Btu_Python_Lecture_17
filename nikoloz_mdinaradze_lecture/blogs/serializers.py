from rest_framework import serializers

from blogs.models import Blogs
from users.serializers import UserSerializer


class BlogsSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Blogs
        fields = ("id", "title", "context", "author")
    
    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user
        return super().create(validated_data)
            