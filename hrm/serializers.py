from rest_framework import serializers
from hrm.models import Users

class Usersserializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields = '__all__'