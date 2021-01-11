from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Post
from .serializers import BlogSerializer

class PostListView(ListAPIView):
    queryset  = Post.objects.order_by('-date_created')
    serializer_class = BlogSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class PostDetailView(RetrieveAPIView):
    queryset  = Post.objects.order_by('-date_created')
    serializer_class = BlogSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class PostFeaturedView(ListAPIView):
    queryset  = Post.objects.all().filter(featured=True)
    serializer_class = BlogSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )
    
class PostCategoryView(APIView):
    serializer_class = BlogSerializer
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request, format=None):
        data = self.request.data
        category = data['category']
        queryset = Post.objects.all().order_by('-date_created').filter(category_iexact=category)

        serializer = BlogSerializer(queryset, many=True)
        
        return Response(serializer.data)
    