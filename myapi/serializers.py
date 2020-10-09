#serializers

from rest_framework import serializers
from .models import blog

class blogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = blog
        fields = ('id','title', 'matter')
