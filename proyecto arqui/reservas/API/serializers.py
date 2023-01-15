from rest_framework import serializers 
from .models import Estudiante, Profesor, Espacio, Reserva  

class EstudianteSerializer(serializers.ModelSerializer):   
    class Meta:     
        model = Estudiante     
        fields = '__all__'

class ProfesorSerializer(serializers.ModelSerializer):   
    class Meta:     
        model = Profesor     
        fields = '__all__'

class EspacioSerializer(serializers.ModelSerializer):   
    class Meta:     
        model = Espacio     
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):   
    class Meta:     
        model = Reserva     
        fields = '__all__'