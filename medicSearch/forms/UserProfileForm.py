from django.forms import ModelForm      
from django import forms
from medicSearch.models.profile import Profile
from django.contrib.auth.models import User


class UserProfileForm(ModelForm):
    def __int__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.role != 1:
            del self.fields['role']

    # classe Meta dentro de um formulário                                     
    # (geralmente definido em um arquivo chamado forms.py)
    # é usada para fornecer metadados e configurações adicionais 
    # relacionadas ao formulário.
    class Meta:                           
        model = Profile                   
        fields = ['user', 'role', 'birthday', 'image']   

        widgets = {

            'user': forms.HiddenInput(),
            'role': forms.Select(attrs={'class': "form-control"}),
            'birthday': forms.DateInput(attrs={'class': "form-control", "type": "date"}),
            "image": forms.FileInput(attrs={'class': "form-control"})

        }


# MODELFORM: obj que a nossa class UserProfileForm herdou para que possamos criar um formulário
#            Do django que se baseie em uma model(Profile)

# FROM DJANGO IMPORT FORMS: módulo que posuí diversas classes que podem mudar a estrutura de um campo formulário

# FIELDS: atributo que pode receber uma lista com campos especificos da nossa class Profile 
#         ou podemos usar um método mágico para usarmos todos os campos da nossa classe

# EXCLUDE: Atributo que usamos para excluir campos específicos do sistema

# WIDGETS: Atributo como um dict, que podemos passar o nome do campo que desejamos modificar
#          podemos mudar o tipo do campo, input text para e-mail.

# HIDDENINPUT: Uma das muitas classes do módulo forms, que usamos para modificar um campo do formulário
#              para se comportar como um hidden.          



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.EmailInput(attrs={'class': "form-control"}),
            'first_name': forms.TextInput(attrs={'class': "form-control"}),
            'last_name': forms.TextInput(attrs={'class': "form-control"})
        }