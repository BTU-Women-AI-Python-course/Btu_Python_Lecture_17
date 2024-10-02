from rest_framework import serializers


class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "title", "context", "author")
