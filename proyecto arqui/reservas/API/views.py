from django.shortcuts import render
from .models import Estudiante, Profesor, Espacio, Reserva
from .serializers import EstudianteSerializer, ProfesorSerializer, EspacioSerializer, ReservaSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
# Create your views here.

class ListaEstudiante(APIView):
  def get(self, request):
      estudiantes = Estudiante.objects.all()
      serializer = EstudianteSerializer(estudiantes,many=True)
      return Response(serializer.data)

  def post(self, request):
      serializer = EstudianteSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
class DetalleEstudiante(APIView):
  def get_object(self, id):
    try:
      return Estudiante.objects.get(id=id)
    except:
      return Http404

  def get(self,request, id):
    estudiante = Estudiante.objects.get(id=id)
    serializer = EstudianteSerializer(estudiante)
    return Response(serializer.data)

  def put(self,request, id):
    estudiante = Estudiante.objects.get(id=id)
    serializer = EstudianteSerializer(estudiante,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, id):
    estudiante = Estudiante.objects.get(id=id)
    estudiante.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class ListaProfesor(APIView):
  def get(self, request):
      profesores = Profesor.objects.all()
      serializer = ProfesorSerializer(profesores,many=True)
      return Response(serializer.data)

  def post(self, request):
      serializer = ProfesorSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DetalleProfesor(APIView):
  def get_object(self, id):
    try:
      return Profesor.objects.get(id=id)
    except:
      return Http404

  def get(self,request, id):
    profesor = Profesor.objects.get(id=id)
    serializer = ProfesorSerializer(profesor)
    return Response(serializer.data)

  def put(self,request, id):
    profesor = Profesor.objects.get(id=id)
    serializer = ProfesorSerializer(profesor,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class ListaEspacio(APIView):
  def get(self, request):
      espacios = Espacio.objects.all()
      serializer = EspacioSerializer(espacios,many=True)
      return Response(serializer.data)

  def post(self, request):
      serializer = EspacioSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DetalleEspacio(APIView):
  def get_object(self, id):
    try:
      return Espacio.objects.get(id=id)
    except:
      return Http404

  def get(self,request, id):
    espacio = Espacio.objects.get(id=id)
    serializer = EspacioSerializer(espacio)
    return Response(serializer.data)

  def put(self,request, id):
    espacio = Espacio.objects.get(id=id)
    serializer = EspacioSerializer(espacio,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, id):
    espacio = Espacio.objects.get(id=id)
    espacio.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class ListaReserva(APIView):
  def get(self, request):
      reservas = Reserva.objects.all()
      serializer = ReservaSerializer(reservas,many=True)
      return Response(serializer.data)

  def post(self, request):
      serializer = ReservaSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DetalleReserva(APIView):
  def get_object(self, id):
    try:
      return Reserva.objects.get(id=id)
    except:
      return Http404

  def get(self,request, id):
    reserva = Reserva.objects.get(id=id)
    serializer = ReservaSerializer(reserva)
    return Response(serializer.data)

  def put(self,request, id):
    reserva = Reserva.objects.get(id=id)
    serializer = ReservaSerializer(reserva,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, id):
    reserva = Reserva.objects.get(id=id)
    reserva.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


