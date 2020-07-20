from django.shortcuts import render
from requests import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from rest_framework import viewsets, serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .models import Blogs
from .serializers import BlogSerializer
from .forms import BlogForm


class BlogsView(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer
