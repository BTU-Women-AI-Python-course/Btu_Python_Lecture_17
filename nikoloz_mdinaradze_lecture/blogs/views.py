from rest_framework import viewsets

from blogs.models import Blogs
from blogs.serializers import BlogsSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer
