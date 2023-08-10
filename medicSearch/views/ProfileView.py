from django.http import HttpResponse

# Dentro do site logado(interno)
def list_profile_view(request, id=None):
    if id is None and request.user.is_authenticated: # Se id for none e usuário estiver autenticado
        id = request.user.id                         # id = id do usuário que logado(autenticado)
    elif not request.user.is_authenticated:
        id = 0
    return HttpResponse('<h1>Usuário de id %s!</h1>' %id)



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