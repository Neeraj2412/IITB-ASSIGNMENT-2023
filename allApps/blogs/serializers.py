from rest_framework import serializers
from. models import *

# queryset to python native 
class blogSerializers(serializers.ModelSerializer):
    class Meta:
        model = blogs
        exclude = ['author']

