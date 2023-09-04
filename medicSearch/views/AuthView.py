from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# do   app       pasta  arquivo import  classe
from medicSearch.forms.AuthForm import LoginForm, RegisterForm
from  django.contrib.auth.models import User
from medicSearch.models.profile import Profile
from medicSearch.forms.AuthForm import LoginForm, RegisterForm, RecoveryForm, ChangePasswordForm
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import hashlib

# Vamos usar o atributo next da url para direcionar o
# usuário para página que ele queira após realizar o login



def login_view(request):
    loginForm = LoginForm()
    message = None
    
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST': 
        username = request.POST['username'] # acessando os dados enviados através do corpo de uma requisição POST:
        password = request.POST['password']  
        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                _next = request.GET.get('next')
                if _next is not None:
                    return redirect(_next)
                else:
                    return redirect("/")
            else:
                message =  {
                    'type': 'danger',
                    'text': 'Dados do usuário inválidos'
                }

    context = {
        'form': loginForm,
        'message': message,
        'title': 'Login',
        'button_text': 'Entrar',
        'link_text': 'Registrar',
        'link_href': '/register'

    }

    return  render(request, template_name='auth/auth.html', context=context, status=200)


def register_view(request):
    registerForm = RegisterForm()
    message = None

    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST['username']
        email =  request.POST['email']
        password = request.POST['password']
        registerForm = RegisterForm(request.POST)

        if registerForm.is_valid():
            # Verificando se existe usuário ou e-mail com esse cadastro
            verifyUsername = User.objects.filter(username = username).first()
            verifyEmail = User.objects.filter(email = email).first()

            if verifyUsername is not None:
                message = {'type': 'danger', 'text': 'Já existe um usuário com este username! '}

            elif verifyEmail is not None:
                message = {'type': 'danger', 'text': 'Já existe um usuário com este e-mail'}
            
            else:
                user = User.objects.create_user(username, email, password)

                if user is not None:
                    message = {'type': 'success', 'text': 'Conta criada com sucesso!'}
                
                else:
                    message = {'type': 'danger', 'text': 'Um erro ocorreu ao tentar criar o usuário.'}

    context = {
        'form': registerForm,
        'message': message,
        'title': 'Registrar',
        'button_text': 'Registrar',
        'link_text': 'Login',
        'link_href': '/login'
    }

    return render(request, template_name='auth/auth.html', context=context, status=200)


# get = solicita
# post = envia
# put = atualiza
# delete = excluí



def logout_view(request):
    logout(request)
    return redirect('/login') # redirecionando para url login



# View de recuperação de Senha
def recovery_view(request):
    recoveryForm = RecoveryForm()   # var = formulário - email type="input"
    message = None                  # message = valor nullo

    if request.method == 'POST':   # Se método de requisição == ' Enviar '
        recoveryForm = RecoveryForm(request.POST) # var = formulário(requisitando dados enviados)

        if recoveryForm.is_valid(): # Se recoveryForm(que recebeu os dados do form enviados) forem válidos
            email =  request.POST['email'] # var = requisição.Enviada['email'] pega o email
            profile = Profile.objects.filter(user__email=email).first()
            # var = Classe.objetos(instaciados).filtro(campo usuário, attr da classe).primeiro()

            if profile is not None:     # Se profile não é nullo
                try:                    # tente
                    send_email(profile) # função(obj profile)

                    message = {              # dict
                        'type': 'success',   # chave: valor
                        'text': 'Um e-mail foi enviado para sua caixa de entrada.'
                    }
                except:                      # exceto
                    message = {              # dict
                        'type': 'danger',    # chave: valor
                        'text': 'Erro no envio do e-mail'
                    }
            else:                           # Senão
                message = {                 # dict
                    'type': 'danger',       # chave: valor
                    'text': 'E-mail inexsistente.'
                }
        else:                              # Senão
            message = {                    # dict
                'type': 'danger',          # chave: valor
                'text': 'Formulário inválido'
            }

    context = {
        'form': recoveryForm,  # chave: variável que recebeu um formulário
        'message': message,    # chave: variável que recebeu um valor dependendo de uma estrutura condicional
        'button_text': 'Recuperar', # chave: valor que vai estar como string no botão
        'link_text': 'login',
        'link_href': '/login'
    }

    return render(request, template_name='auth/auth.html', context=context, status=200)


def send_email(profile):
    """
    funcão enviar e-mail(var profile)

    render_to_string: Esta função geralmente é usada em frameworks web
    como Django para renderizar um modelo HTML em uma string HTML completa. 

    """
    profile = hashlib.sha256().hexdigest() # var = módulo.cria objeto de hash SHA-256 vazio
    profile.save()                         # método save para nossa var

    # Possiveis erros(exceções)
    try: # tente
        html_message = render_to_string('auth/recovery.html', {'token': profile.token})
        # var                func           1º argumento,      2º argumento é um dict com os dados que serão passados para o modelo.

        message =  strip_tags(html_message)

        send_email(
            # Assunto
            subject = "Recuperação de senha", message=message, html_message=html_message,
            # remetente
            from_email=settings.EMAIL_HOST_USER, recipient_list=[profile.user.email], fail_silently=False,
        )
    
    except: # exceto
        raise Exception



def change_password(request, token):  
    """ 
    função (solicitação HTTP, chave eletrônica verificar autenticidade do usuário)
    profile = Classe.objetos.filtre(token: chave eletrônica)
    changePasswordForm = Formulário do tipo -> input:password
    message = valor Nulo
    link_href = /recovery: redirecionar para url recuperação
    
    """
    profile = Profile.objects.filter(token=token).first() 
    changePasswordForm = ChangePasswordForm()
    message = None
    link_text = 'Solicitar recuperação de senha'
    link_href = '/recovery'


    if profile is not None: # Se a variável que recebe uma instância da classe Profile não for nula
        if request.method == 'POST': # Se método da requisição igual POST(enviar)
            changePasswordForm = ChangePasswordForm(request.POST) # VAR = FORMULÁRIO(ENVIADO)
            if changePasswordForm.is_valid(): # var que recebeu o formulário enviado for válido
                profile.user.set_password(request.POST['password']) # var = usuário.configure_senha(requisição.ENVIADA['VARIÁVEL DO FORMULÁRIO'])
                profile.token = None # var.chave eletrônica = Nulo
                profile.user.save() # Salvar o usuário autenticado associado ao perfil
                profile.save()     #  Salvar o perfil

                message = {              # dict
                    'type': 'success',   # chave: valor
                    'text': 'Senha alterada com sucesso!'
                }

            else:
                message = {
                    'type': 'danger', 
                    'text': 'Formulário inválido'
                }
        
        else:
            message = {
                'type': 'danger',
                'text': 'Token inválido. Solicite novamente.'
            }
        

        context = { # dict
            # chave: valor
            'form': changePasswordForm,
            'message': message,
            'title': 'Alterar senha',
            'button_text': link_text,
            'link_href': link_href
        }

        return render(request, template_name='auth/auth.html', context=context, status=200)