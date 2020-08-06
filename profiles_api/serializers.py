from rest_framework import serializers

class HelloSerializer(serializers.Searializer):
    """ Searlizes a name field for testing our Apiview """
    name = serializers.CharField(max_length = 10)# allows you to input any text
