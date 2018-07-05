# Serializers are for serialization into Python objects and advanced validations

from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import *


'''
##########################    User Profile and Auth Serializers
'''
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'groups', 'last_login']


class ProfileSerializer(serializers.ModelSerializer):
    userprofile = serializers.StringRelatedField(many=False)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'groups', 'userprofile']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


'''
##########################    Main API Serializers
'''
class RezeptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rezept                                                  # model name
        fields = ['id', 'titel', 'langerText', 'booleanlol']            # fields u want
        read_only_fields = ['id']                                       # optional can be used for everything

    def validate_langerText(self, value):                               # OPTIONAL
        print(value)                                                    # validatort bestimmte fields die man will (automatisch)
        print(self.initial_data['langerText'])                          # -> geht auch aber dann lieber einfach validate
        if 1 > 2:
            raise serializers.ValidationError("Mathe ist kaputt!")
        return value

    def validate(self, data):                                           # OPTIONAL
        print(data['titel'])                                            # Validiert gleich mehrere Fields
        return data

    def validate_titel(self, value):                                    # BEISPIEL mit DB
        daTitle = Rezept.objects.filter(titel__iexact=value)            #
        if self.instance:                                               # die instance muss sich selber ausschliessen
            daTitle = daTitle.exclude(pk=self.instance.pk)
        if daTitle.exists():
            raise serializers.ValidationError("Da title must be unique like a unicorn!")
        return value


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rezept
        fields = ['id', 'titel', 'langerText', 'booleanlol']
        read_only_fields = ['booleanlol']
