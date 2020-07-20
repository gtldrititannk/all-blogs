from rest_framework import serializers
from rest_framework import status
from .models import Blogs


class BlogSerializer(serializers.ModelSerializer):
    # def validate(self, attrs):
    #     """
    #     This method will Validate the user data and serialize it.
    #     """
    #     if attrs['product_mrp'] <= 0:
    #         raise serializers.ValidationError("Price Cannot Be Zero or Negative.")
    #     return attrs

    class Meta:
        model = Blogs
        fields = ['author', 'title', 'blog_content',
                  'created_at', 'updated_at'
                  ]

    def update(self, instance, validated_data):
        """
            This method will update the record.
        """
        instance.blog_content = validated_data.get('blog_content', instance.blog_content)
        instance.title = validated_data.get('title', instance.title)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance
