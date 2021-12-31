import datetime
from actividad.models import actividad 
from encuesta.models import encuesta

def validar_fecha(property,date):
    exist=False
    date = date.replace(minute=00, second=00)
    print('date',date)
    total=actividad.objects.filter(
        schedule__gte=date,
        schedule__lte=date + datetime.timedelta(hours=1),
        property=property
    ).exclude(status='cancelada').count()
    if total >0:
        exist=True
    return exist

def validar_status(actividad):
    condicion=''
    fecha=datetime.datetime.now()


    if actividad.status== 'Activo' and actividad.schedule >=fecha:
        condicion='Pendiente de realizar'
    elif actividad.status == 'Activo' and actividad.schedule < fecha:
        condicion = 'Atrasada'
    elif actividad.status == ' Realizado':
        condicion= 'Terminada'
    elif actividad.status == 'Desactivada':
        condicion = 'Desactivada'
    elif actividad.status == ' Cancelado':
        condicion== 'Cancelado'
    return condicion

def obtener_id_encuesta(id):
    try:
        en=encuesta.objects.get(actividad=id)
    except Exception as e:
        print(f'error{str(e)}')
        en=None
    return en