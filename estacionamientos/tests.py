from django.test import TestCase
from estacionamientos.models import Estacionamiento, Reserva, Pago
from estacionamientos.forms import ReservaForm, EstacionamientosForm
import sys
from datetime import datetime
from estacionamientos.views import crearEstacionamiento
import copy

# Create your tests here.

#DATOS PARA CREAR UN ESTACIONAMIENTO CUALQUIERA
DICT=    {'nombre_duenio' : 'Carlos',
        'nombre_est' : 'Melanie',
        'direccion' : 'por alla',
        'telefono1' : '1231231231',
        'email1'  : 'papirico@ho.com',
        'rif' :  '12232344',
        'capacidad' : '10',
        'tarifa' : '6',
        'horaI' : '06:00 AM',
        'reservaI' : '06:00 AM',
        'horaF' : '08:00 PM',
        'reservaF' : '08:00 PM',
        }

class EstacionamietoViewsTestCase(TestCase):
    
    def crear_estacionamiento(self):
        Est=Estacionamiento()
        Est.nombre_duenio = 'Carlos'
        Est.nombre_est = 'La chikungunya'
        Est.direccion = 'por alla'
        Est.telefono1 = 1231231231
        Est.email1 = 'papirico@ho.com'
        Est.rif = 12232344
        Est.capacidad = 10
        Est.tarifa = 6
        time = '06:00 AM'
        format = '%I:%M %p'
        Est.horaI = datetime.strptime(time,format)
        Est.reservaI = datetime.strptime(time,format)
        time = '08:00 PM'
        Est.horaF = datetime.strptime(time,format)
        Est.reservaF = datetime.strptime(time,format)      
        Est.save()
        return Est
    
    #1
    def test_view_indexSinEstacionaminto(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context['lista']),0)
   
    def test_view_indexConEstacionaminto(self):
        self.crear_estacionamiento()
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context['lista']),1)
  
    def test_view_indexVerEstacionamiento(self):
        Est = self.crear_estacionamiento()
        resp = self.client.get('/1/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(Est.nombre_est, resp.context['parametros'].nombre_est)
    
    def test_view_nuevo_estacionamiento(self):
        resp = self.client.get('/nuevo/')
        self.assertEqual(resp.status_code, 200)
    
    def test_view_nueva_reserva(self):
        resp = self.client.get('/nueva_reserva/')
        self.assertEqual(resp.status_code, 200)
            
    def test_view_editar_estacionamiento(self):
        Est = self.crear_estacionamiento()
        Est.save()
        resp = self.client.get('/1/editar/')
        self.assertEqual(resp.status_code, 200)       
        
    def test_integrar_view_crear_estacionamiento(self):
        resp = self.client.get('/nuevo/')
        self.assertTrue(type(resp.context['form']) is EstacionamientosForm)
        
    def test_integrar_view_nueva_reserva(self):
        resp = self.client.get('/nueva_reserva/')
        self.assertTrue(type(resp.context['form']) is ReservaForm)
        
    def test_integrar_view_editar_estacionamiento(self):
        Est = self.crear_estacionamiento()
        Est.save()
        resp = self.client.get('/1/editar/')    
        self.assertTrue(type(resp.context['form']) is EstacionamientosForm)                 
        
    def test_form_estacionamiento(self):
        DIC = DICT.copy()
        response = self.client.post('/nuevo/', DIC)
        est = Estacionamiento.objects.get(nombre_est='Melanie')
        self.assertEqual(est.nombre_est, DIC['nombre_est']) 
        self.assertEqual(est.nombre_duenio, DIC['nombre_duenio']) 
        self.assertEqual(est.direccion, DIC['direccion'])         
        self.assertEqual(est.telefono1, int(DIC['telefono1']))
        self.assertEqual(est.email1, DIC['email1'])              
        self.assertEqual(est.rif, int(DIC['rif']))
        self.assertEqual(est.capacidad, int(DIC['capacidad']))      
        self.assertEqual(est.tarifa, int(DIC['tarifa']))          
        self.assertEqual(est.horaI.hour, datetime.strptime(DIC['horaI'],'%I:%M %p').hour)
        self.assertEqual(est.horaI.minute, datetime.strptime(DIC['horaI'],'%I:%M %p').minute)            
        self.assertEqual(est.horaF.hour, datetime.strptime(DIC['horaF'],'%I:%M %p').hour)
        self.assertEqual(est.horaF.minute, datetime.strptime(DIC['horaF'],'%I:%M %p').minute)         
        self.assertEqual(est.reservaI.hour, datetime.strptime(DIC['reservaI'],'%I:%M %p').hour)
        self.assertEqual(est.reservaI.minute, datetime.strptime(DIC['reservaI'],'%I:%M %p').minute)
        self.assertEqual(est.reservaF.hour, datetime.strptime(DIC['reservaF'],'%I:%M %p').hour)
        self.assertEqual(est.reservaF.minute, datetime.strptime(DIC['reservaF'],'%I:%M %p').minute)   
        
                  
    def test_form_estacionamiento_nombre_repetido(self):
        DIC = DICT.copy()
        self.crear_estacionamiento().save()
        DIC['nombre_est'] = 'La chikungunya'
        response = self.client.post('/nuevo/', DIC)
        self.assertFalse(response.context['form'].is_valid())

    def test_form_estacionamiento_nombre_duenio_vacio(self):
        DIC = DICT.copy()
        DIC['nombre_duenio'] = ''
        response = self.client.post('/nuevo/', DIC)
        self.assertFalse(response.context['form'].is_valid())

                
    def test_form_estacionamiento_nombre_estacionamiento_vacio(self):
        DIC = DICT.copy()
        DIC['nombre_est'] = ''
        response = self.client.post('/nuevo/', DIC)
        self.assertFalse(response.context['form'].is_valid())

        
    def test_form_estacionamiento_dirreccion_vacio(self): 
        DIC = DICT.copy()  
        DIC['email1'] = ''
        response = self.client.post('/nuevo/', DIC)
        self.assertFalse(response.context['form'].is_valid())
  
     
    def test_form_estacionamiento_telefono_vacio(self):
        DIC = DICT.copy()
        DIC['telefono1'] = ''
        response = self.client.post('/nuevo/', DIC)
        self.assertFalse(response.context['form'].is_valid())

        
    def test_form_estacionamiento_email_vacio(self):
        DIC = DICT.copy()
        DIC['email1'] = ''
        response = self.client.post('/nuevo/', DIC)
        self.assertFalse(response.context['form'].is_valid())
 
        
    def test_form_estacionamiento_rif_vacio(self):
        DIC = DICT.copy()
        DIC['rif'] = ''
        response = self.client.post('/nuevo/', DIC)
        self.assertFalse(response.context['form'].is_valid())

        
    def test_form_estacionamiento_capacidad_vacio(self):
        DIC = DICT.copy()
        DIC['capacidad'] = ''
        response = self.client.post('/nuevo/', DIC)
        self.assertFalse(response.context['form'].is_valid())

        
    def test_form_estacionamiento_tarifa_vacio(self):
        DIC = DICT.copy()
        DIC['tarifa'] = ''
        response = self.client.post('/nuevo/', DIC)
        self.assertFalse(response.context['form'].is_valid())
    
        
    def test_form_estacionamiento_horarioI_vacio(self):
        DIC = DICT.copy()
        DIC['horaI'] = ''
        response = self.client.post('/nuevo/', DIC)
        self.assertFalse(response.context['form'].is_valid())

    def test_form_estacionamiento_horarioF_vacio(self):
        DIC = DICT.copy()
        DIC['horaF'] = ''
        response = self.client.post('/nuevo/', DIC)
        self.assertFalse(response.context['form'].is_valid())
        DIC['horaI'] = '08:00 PM'
    
    def test_form_estacionamiento_nombre_invalido(self):
        DIC = DICT.copy()
        print(DIC)  
        response = self.client.post('/nuevo/', DIC)
        self.assertFalse(response.context['form'].is_valid())
    
        
    def test_form_estacionamiento_campo_hora_invalido(self):
        DIC = DICT.copy()
        DIC['horaI'] = '06:00:00'
        response = self.client.post('/nuevo/', DIC)
        self.assertFalse(response.context['form'].is_valid())
        
    def test_form_estacionamiento_email_invalido1(self):
        DIC = DICT.copy()
        DIC['email1'] = 'aaahotmail.com'
        response = self.client.post('/nuevo/', DIC)
        self.assertFalse(response.context['form'].is_valid())     
        
    def test_form_estacionamiento_email_invalido2(self):
        DIC = DICT.copy()
        DIC['email1'] = 'aaa@hotmailcom'
        response = self.client.post('/nuevo/', DIC)
        self.assertFalse(response.context['form'].is_valid())
        
    def test_form_estacionamiento_email_invalido3(self):
        DIC = DICT.copy()
        DIC['email1'] = '@hotmailcom'
        response = self.client.post('/nuevo/', DIC)
        self.assertFalse(response.context['form'].is_valid())
        
    def test_form_estacionamiento_email_invalido4(self):
        DIC = DICT.copy()
        DIC['email1'] = '@hotmail.com'
        response = self.client.post('/nuevo/', DIC)
        self.assertFalse(response.context['form'].is_valid())
        
    def test_valid_form(self):
        data = DICT.copy() 
        form = EstacionamientosForm(data=data)
        self.assertTrue(form.is_valid())
        
        
    def test_invalid_nd_form(self):
        DI = DICT.copy()
        DI['nombre_duenio']= ""
        form = EstacionamientosForm(data=DI)
        self.assertFalse(form.is_valid())
               
    def test_invalid_ne_form(self):
        DI = DICT.copy()
        DI['nombre_est']= ""
        form = EstacionamientosForm(data=DI)
        self.assertFalse(form.is_valid())
        
    
    def test_invalid_dir_form(self):
        DI = DICT.copy()
        DI['direccion']= ""
        form = EstacionamientosForm(data=DI)
        self.assertFalse(form.is_valid())
    
    
    def test_invalid_t1_form(self):
        DI = DICT.copy()
        DI['telefono1'] = ""
        form = EstacionamientosForm(data=DI)
        self.assertFalse(form.is_valid())
        
        
    def test_invalid_e1_form(self):
        DI = DICT.copy()
        DI['email1']= ""
        form = EstacionamientosForm(data=DI)
        self.assertFalse(form.is_valid())
        
        
    def test_invalid_r_form(self):
        DI = DICT.copy()
        DI['rif']= ""
        form = EstacionamientosForm(data=DI)
        self.assertFalse(form.is_valid())
        
        
    def test_invalid_tm_form(self):
        DI = DICT.copy()
        DI['telefono1']= 212444335555
        form = EstacionamientosForm(data=DI)
        self.assertFalse(form.is_valid())
        
        
    def test_invalid_tme_form(self):
        DI = DICT.copy()
        DI['telefono1']= 0
        form = EstacionamientosForm(data=DI)
        self.assertFalse(form.is_valid())
       
        
    def test_invalid_gm_form(self):
        DI = DICT.copy()
        DI['email1']= "a@com"
        form = EstacionamientosForm(data=DI)
        self.assertFalse(form.is_valid())
        
        
    def test_invalid_gme_form(self):
        DI = DICT.copy()
        DI['email1']= "acom"
        form = EstacionamientosForm(data=DI)
        self.assertFalse(form.is_valid())
        
            
    def test_invalid_trn_form(self):
        DI = DICT.copy()
        DI['rif']= -111
        form = EstacionamientosForm(data=DI)
        self.assertFalse(form.is_valid())
        
        
    def test_invalid_ndn_form(self):
        DI = DICT.copy()
        DI['nombre_duenio']= None
        form = EstacionamientosForm(data=DI)
        self.assertFalse(form.is_valid())
        
            
    def test_invalidnen_form(self):
        DI = DICT.copy()
        DI['nombre_est']= None
        form = EstacionamientosForm(data=DI)
        self.assertFalse(form.is_valid())
        
        
    def test_invalid_ndin_form(self):
        DI = DICT.copy()
        DI['direccion']= None
        form = EstacionamientosForm(data=DI)
        self.assertFalse(form.is_valid())
        
            
    def test_invalid_ntn_form(self):
        DI = DICT.copy()
        DI['telefono1']= None
        form = EstacionamientosForm(data=DI)
        self.assertFalse(form.is_valid())
        
        
    def test_invalid_nemn_form(self):
        DI = DICT.copy()
        DI['email1']= None
        form = EstacionamientosForm(data=DI)
        self.assertFalse(form.is_valid())
            
        
    def test_invalid_nrin_form(self):
        DI = DICT.copy()
        DI['rif']= None
        form = EstacionamientosForm(data=DI)
        self.assertFalse(form.is_valid())   
