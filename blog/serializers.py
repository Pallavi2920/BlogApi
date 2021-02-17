from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import Blog

class BlogSerializer(DocumentSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
