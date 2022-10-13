from rest_framework import serializers
from blog.models import blog, tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tag
        fields = ('id', 'tag_title',)


class CreateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = ('user','blog_title', 'desc', 'blogTag', 'history', 'category')

class BlogListSerializer(serializers.ModelSerializer):
    blogTag = TagSerializer(many = True)
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        return f"Username = {obj.user.username}"
    class Meta:
        model = blog
        fields = ('user','blog_title', 'desc', 'blogTag',  'category')