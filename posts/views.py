from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListAPIView): # wyswietla wszyskie posty
    queryset = Post.objects.all( )#queryset = to co chcemy wswietlac na koncu
    serializer_class = PostSerializer