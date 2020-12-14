from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
    )
from posts.models import Post
from comments.api.serializers import CommentSerializer
from comments.models import Comment

from accounts.api.serializers import UserDetailSerializer



class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            #'id',
            'title',
            #'slug',
            'content',
            'image',
            'publish'
        ]


class PostListSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    url = HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field='slug'
    )
    update_url = HyperlinkedIdentityField(
        view_name='posts-api:update',
        lookup_field='slug'
    )
    class Meta:
        model = Post
        fields = [
            'user',
            'url',
            'update_url',
            'title',
            'content',
            'publish'
        ]


class PostDetailSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    image = SerializerMethodField()
    html = SerializerMethodField()
    comments = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'user',
            'id',
            'title',
            'slug',
            'content',
            'html',
            'image',
            'publish',
            'comments',
        ]

    def get_html(self, obj):
        return obj.get_markdown()


    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

    def get_comments(self, obj):
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(c_qs, many=True).data
        return comments






"""
data = {
    "title": "Yeah buddy",
    "content": "New Content",
    "publish": "2016-2-12",
    "slug": "yeah-buddy",
}
obj = Post.objects.get(id=3)
new_item = PostDetailSerializer(obj, data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)
"""