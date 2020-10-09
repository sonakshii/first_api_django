from django.shortcuts import render
from rest_framework import viewsets

from .serializers import blogSerializer
from .models import blog


class blogViewSet(viewsets.ModelViewSet):
    queryset = blog.objects.all().order_by('id')
    serializer_class = blogSerializer
