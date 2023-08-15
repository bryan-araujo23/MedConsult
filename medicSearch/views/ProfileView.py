from django.shortcuts import render, redirect
from medicSearch.models import Profile
from django.core.paginator import Paginator

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