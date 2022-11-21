
from rest_framework import serializers
from .models import Post
class PostSerializer(serializers.ModelSerializer):
    auth=serializers.ReadOnlyField(read_only=True)
    class Meta:
        model=Post
        fields=['image','video','title','content','auth']
    
    # def get_author(self,request):
    #     self.auth=request.user.username
    #     return self.auth
    
    def create(self, validated_data):
        validated_data["auth"]=self.context["user"]
        post=Post.objects.create(**validated_data,auth=self.context["user"])
        return post