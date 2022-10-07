from rest_framework import serializers
from blog.models import blog, tag

# Note: Meselen user: 1 bu formada data cixacaq ForeignKey, ManytoMany field olanlarda id-leri cixacaq. Amma istesek ki,
# "user: Gunay" cixsin bu zaman bunu 3 usulla yaza bilerik, ashagida bashliqlar yazmisham 3 usula da :
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tag
        fields = ('id', 'tag_title',)


class CreateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = ('user','blog_title', 'desc', 'blogTag', 'history', 'category')

class BlogListSerializer(serializers.ModelSerializer):
    # Birinci usul:
    blogTag = TagSerializer(many = True)
    # ------------------------------------

    # Ikinci usul:
    # user = serializers.CharField(source = 'user.username')
    # --------------------------------------
    
    # Ucuncu usul: (bu usulda get_user-functionu mutleq get ile bashlamalidir, user- ise serialize etdiyimiz fieldin adidir; obj ise blog modelimzin ozudur, hansi ki view-dan bize gelir (view-da yazdigimiz "blogs"-dur)):
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        return f"Username = {obj.user.username}"
    # --------------------------------------
    # Tagi methodla bele yaza bilerik:
    # blogTag = serializers.SerializerMethodField()
    # def get_blogTag(self, obj):
    #     return [{'name': blogTag.tag_title} for blogTag in obj.blogTag.all()]

    class Meta:
        model = blog
        fields = ('user','blog_title', 'desc', 'blogTag',  'category')