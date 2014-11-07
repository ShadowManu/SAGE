import re
from django import forms
from estacionamientos.models import Estacionamiento


class EstacionamientosForm(forms.ModelForm):
    
    class Meta:
        model = Estacionamiento
        #fields = ('nombre_duenio', 'nombre_est', 'direccion', 'telefono1', 'telefono2',
        #          'telefono3', 'email1', 'email2', 'email3', 'rif',)
        
        def clean_nombre_duenio(self):
            diccionario = self.cleaned_data
      
            dueno = diccionario.get('nombre_duenio')
            
            if not re.match('[^\W\d_]+$', dueno, re.UNICODE):
                raise forms.ValidationError("El dueno debe contener un nombre valido (Solo caracteres y espacios).")
         
            return dueno
        
        def clean_nombre_est(self):
            diccionario = self.cleaned_data
      
            est = diccionario.get('nombre_est')
            
            if not re.match('(\w)+$', est, re.UNICODE):
                raise forms.ValidationError("El estacionamiento debe contener un nombre valido.")
         
            return est
        def clean_dirreccion(self):
            diccionario = self.cleaned_data
      
            dir = diccionario.get('direccion')
            
            if not re.match('([^\W_]|\.|,)+$', dir, re.UNICODE):
                raise forms.ValidationError("El estacionamiento debe contener una direccion valida.")
         
            return dir
        
        def clean_telefono1(self):
            diccionario = self.cleaned_data
      
            tel = diccionario.get('telefono1')
            
            if not re.match('0\d{3}-\d{7}$', tel, re.UNICODE):
                raise forms.ValidationError("El telefono tiene que tener el formato correcto y ser solo numeros (0xxx-xxxxxxx).")
         
            return tel
        
        def clean_telefono2(self):
            diccionario = self.cleaned_data
      
            tel = diccionario.get('telefono2')
            
            if not re.match('0\d{3}-\d{7}$', tel, re.UNICODE):
                raise forms.ValidationError("El telefono tiene que tener el formato correcto y ser solo numeros (0xxx-xxxxxxx).")
         
            return tel
        
        def clean_telefono3(self):
            diccionario = self.cleaned_data
      
            tel = diccionario.get('telefono3')
            
            if not re.match('0\d{3}-\d{7}$', tel, re.UNICODE):
                raise forms.ValidationError("El telefono tiene que tener el formato correcto y ser solo numeros (0xxx-xxxxxxx).")
         
            return tel
        
        def clean_email1(self):
            diccionario = self.cleaned_data
      
            email = diccionario.get('email1')
            
            if not re.match('[a-zA-Z0-9|-|_]+@([a-zA-Z0-9|-|_]+\.)+[a-zA-Z0-9]+$', email, re.UNICODE):
                raise forms.ValidationError("El email tiene que tener el formato correcto.")
         
            return email
        
        def clean_email2(self):
            diccionario = self.cleaned_data
      
            email = diccionario.get('email2')
            
            if not re.match('[a-zA-Z0-9|-|_]+@([a-zA-Z0-9|-|_]+\.)+[a-zA-Z0-9]+$', email, re.UNICODE):
                raise forms.ValidationError("El email tiene que tener el formato correcto.")
         
            return email
        
        def clean_email3(self):
            diccionario = self.cleaned_data
      
            email = diccionario.get('email3')
            
            if not re.match('[a-zA-Z0-9|-|_]+@([a-zA-Z0-9|-|_]+\.)+[a-zA-Z0-9]+$', email, re.UNICODE):
                raise forms.ValidationError("El email tiene que tener el formato correcto.")
         
            return email
        
        def clean_rif(self):
            diccionario = self.cleaned_data
      
            rif = diccionario.get('email1')
            
            if not re.match('(J|j|v|V)[0-9]{10}$', rif, re.UNICODE):
                raise forms.ValidationError("El rif tiene que tener el formato correcto.")
         
            return rif