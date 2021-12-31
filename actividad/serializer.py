from rest_framework import serializers

from actividad.models import actividad
from encuesta.serializer import encuesta_serializers
from propiedad.serializer import Propiedad_serializers
from prueba.validadores_globales import validar_status,obtener_id_encuesta



class actividad_serializer(serializers.ModelSerializer):
    class Meta:
      model= actividad
      fields="__all__" 

    def obtener_encuestas(self,instancias):
        pre=super(actividad_serializer,self).to_representation(instancias)
        condicion= validar_status(instancias)
        enc=obtener_id_encuesta(instancias.id)
        enc_data=encuesta_serializers(enc,contex=self.context).data
        if enc:
            enc_data['url']=self.context['request']._current_scheme_host + f'/enc/enc-preview/{enc.id}'
        else:
            enc_data['data']=None
        pre['property']=actividad_serializer(instancias.property).data
        pre['condition']=condicion
        pre['survey']=enc_data
        return pre

class reagendar(serializers.Serializer):
    id=serializers.IntegerField()
    fecha=serializers.DateTimeField()

class cancelar(serializers.Serializer):
    id=serializers.IntegerField()
        
