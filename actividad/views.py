from django.db import transaction
from django.db.models.query import QuerySet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets,status
from actividad.serializer import actividad_serializer,reagendar,cancelar
from actividad.models import actividad
from datetime import datetime, time,timedelta
from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView
from prueba.validadores_globales import validar_fecha



class Actividad_view(viewsets.ModelViewSet):
    serializer_class=actividad_serializer
    queryset=actividad.objects.all()
    authentication_classes = []
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializerz=self.serializer_class(data=request.data)
        if serializerz.is_valid():
            data = serializerz.validated_data
            print('data',data)
            print('data',data['title'])
            if  data['property'].status=='Desactivada':
                mensaje='Ya se encuentra desactivada'
                return Response({'mensaje':mensaje},status=status.HTTP_404_NOT_FOUND)
            exist=validar_fecha(data['property'],data['schedule'])
            if exist:
                mensaje='La fecha y hora ya estan en uso'
                return Response({'mensaje':mensaje},status=status.HTTP_406_NOT_ACCEPTABLE)

            with transaction.atomic():
    
                nueva_actividad=actividad.objects.create(
                    property=data['property'],
                    title=data['title'],
                    status=data['status'],
                    schedule=data['schedule']
                )
                nueva_actividad.updated_at =datetime.now()
                nueva_actividad.save()
                serializerz=self.serializer_class(
                    nueva_actividad, context={'request': request}
                )
                return Response(data=serializerz.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializerz.errors,status=status.HTTP_400_BAD_REQUEST)

    def lista(self,request):
        init_date = request.query_params.get('init_date', None)
        end_date = request.query_params.get('end_date', None)
        activity_status = request.query_params.get('status', None)

        if init_date and  end_date and status:
            lista_actividades=self.queryset.filter(
                schedule__gte=init_date,
                schedule__lte=end_date,
                status=activity_status
            ).order_by('schudele')
        else:
            init_date=datetime.now().replace(hour=0,minute=0,second=0) - datetime.timedelta(days=3)
            end_date= init_date.replace(hour=23, minute=59, second=59) + datetime.timedelta(days=14)
            activities_list = self.queryset.filter(
                schedule__gte=init_date,
                schedule__lte=end_date
            ).order_by('schedule')
            serialiserz=self.serializer_class(activities_list, many=True, context={'request': request})
            return Response(data=serialiserz.data, status=status.HTTP_200_OK)

   

class reagendar(GenericAPIView):
        serializer_class=reagendar
        querry=actividad.objects.all()

        def post(self,request):
            serialiserz=self.serializer_class(data=request.data)
            if serialiserz.is_valid():
                data=serialiserz.validated_data
                print('data',data)
                actividades=get_object_or_404(self.querry,pk=data['id'])
                if actividades.status == 'Cancelado':
                    mensaje='Ya esta cancelada'
                    return Response({'mensaje':mensaje},status=status.HTTP_401_UNAUTHORIZED)
                #schedule = data['schedule']
                print('hola2')
                with transaction.atomic():
                    actividades.schedule=datetime.now()
                    actividades.updated_at=datetime.now()
                    actividades.save()
                    serializerz=actividad_serializer(actividades, context={'request': request})
                    return Response(data=serialiserz.data,status=status.HTTP_202_ACCEPTED)
            else:
                return Response(data=serialiserz.errors,status=status.HTTP_400_BAD_REQUEST)
    
class cancelar(GenericAPIView):
        serializer_class=cancelar
        query=actividad.objects.all()
        def post(self,request):
            serialiserz=self.serializer_class(data=request.data)
            if serialiserz.is_valid():
                data=serialiserz.validated_data
                actividades=get_object_or_404(self.query,pk=data['id'])
                if actividades.status == 'Cancelado':
                    mensaje= 'Cancelado previamente'
                    return Response({'mensaje':mensaje},status=status.HTTP_400_BAD_REQUEST)
                with transaction.atomic():
                    actividades.status='Cancelado'
                    actividades.updated_at=datetime.now()
                    actividades.save()
                    serializerz=actividad_serializer(actividades,context={'request': request})
                    return Response(data=serialiserz.data,status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serialiserz.errors,status=status.HTTP_404_NOT_FOUND)

                

