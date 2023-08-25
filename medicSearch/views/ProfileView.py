from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from medicSearch.models import Profile
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from medicSearch.forms.UserProfileForm import UserProfileForm, UserForm

# Dentro do site logado(interno)
def list_profile_view(request, id=None):
    profile = None

    if id is None and request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()

    elif id is not None:
        profile = Profile.objects.filter(user__id=id).first()
    elif not request.user.is_authenticated:
        return redirect(to='/')
    
    favorites = profile.show_favorites()
    if len(favorites) > 0:
        paginator = Paginator(favorites, 8)
        page = request.GET.get('page')
        favorites = paginator.get_page(page)

    ratings = profile.show_ratings()
    if len(ratings) > 0:
        paginator = Paginator(ratings, 8)
        page = request.GET.get('page')
        ratings = paginator.get_page(page)


    context = {
        'profile': profile,
        'favorites': favorites,
        'ratings': ratings,
    }

    return render(request, template_name='profile/profile.html', context=context, status=200)

# request.user -> requisita algo objeto autenticado

# Para Acessarmos qql dado padrão do usuário(obj) logado, é só acessar request.user

# request.user.username -> Nome do usuário
# request.user.email -> e-mail do usuário
# request.user.first_name -> primeiro nome
# request.user.last_name -> último nome
# request.user.date_joined -> data de cadastro
# request.user.is_active -> se está ativo
# request.user.is_staff -> se usuário pode acessar site adm
# request.user.is_superuser -> se é um usuário com acesso ao painel adm
# request.user.last_login -> data e hora do último login do usuário
# request.user.is_authenticated -> atributo que informa se usuário estálogado ou não


@login_required
def edit_profile(request):   
    profile = get_object_or_404(Profile, user=request.user) # Profile class principal
    emailUnused = True
    message = None

    if request.method == 'POST':        
        profileForm = UserProfileForm(request.POST, request.FILES, instance=profile)
        userForm = UserForm(instance=request.user)

        # VERIFICA SE O E-MAIL QUE O USUÁRIO ESTÁ UTILIZAR EM SEU PERFIL JÁ EXISTE EM OUTRO PERFIL.
        # request.POST['email'] podemos acessar qql dado enviado pelo formulário

        # buscando objetos do modelo Perfil onde o campo email do campo relacionado usuario seja igual ao valor fornecido em request.POST['email'].
        verifyEmail = Profile.objects.filter(user__email=request.POST['email']).exclude(user__id=request.user.id).first()
        emailUnused = verifyEmail is None

    else:
        profileForm = UserProfileForm(instance=profile)
        userForm = UserForm(instance=request.user)

    if profileForm.is_valid() and  userForm.is_valid() and emailUnused:
        profileForm.save()
        userForm.save()
        message = {'type': 'success', 'text': 'Dados atualizados com sucesso'}
    else:
        # Aqui verificamos se é do tipo post, para que na primeira vez que a página carregar a mensagem não apareça
        if request.method == 'POST':
            if emailUnused:
                # Se o e-mail não está em uso mas o formulário tiver algum dado inválido.
                message = {'type': 'danger', 'text': 'Dados inválidos'}
            else:
                # Se o e-mail que o usuário  tentou usar já está em uso por outra pessoa
                message = {'type': 'warning', 'text': 'E-mail já usado por outro usuário'}


    context = {
        'profileForm': profileForm,
        'userForm': userForm,
        'message': message
    }

    return render(request, template_name='user/profile.html', context=context, status=200)


# get_object_or_404 = Método para fazermos uma consulta. Primeiro parâmetro, é model(Profile) que
# queremos consultar, e o segundo(user=request.user) é o campo da model que vamos consultar
# Caso retorne um resultado do banco de dados, teremos uma instância do da classe Profile
# Caso não exista um resultado, retornará um erro 404 em nossa página.

# UserProfileForm: Classe que criamos, que será a representação da nossa model
#                  Em formato de  formulário em nosso template HTml
# instance: Parâmetro da nossa classe form receberá a instância da classe que queromos editar