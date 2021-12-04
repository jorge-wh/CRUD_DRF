# Django-Rest-Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from .models import Libro

class BookSerializer(serializers.ModelSerializer):
    titulo = serializers.CharField(max_length=13, 
    validators=[UniqueValidator(queryset=Libro.objects.all())])

    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'paginas', 'desc_corta', 'categoria']

    def validate(self, data):
        if not data.get('categoria') or data.get('categoria') == "":
            raise serializers.ValidationError('La categoria no puede ir vacia.')
        
        return data

class BookFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'paginas', 'desc_corta', 'categoria']