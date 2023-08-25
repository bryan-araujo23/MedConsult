from django.shortcuts import render, redirect
from medicSearch.models import Profile, Rating
from django.core.paginator import Paginator
from medicSearch.forms.MedicForm import MedicRatingForm




# Fora do site(SERVIDOR)
def list_medics_views(request):
    name = request.GET.get("name")                    # estamos capturando o que vem da url com mét. GET
    speciality = request.GET.get("speciality")        # estamos capturando o que vem da url com mét. GET
    neighborhood = request.GET.get("neighborhood")    # estamos capturando o que vem da url com mét. GET
    city = request.GET.get("city")                    # estamos capturando o que vem da url com mét. GET
    state = request.GET.get("state")                  # estamos capturando o que vem da url com mét. GET

    medics = Profile.objects.filter(role=2)

    if name is not None and name != '':               
        medics = medics.filter(user__first_name__contains=name) 
    if speciality is not None:
        medics = medics.filter(specialties__id=speciality)

    if neighborhood is not None:
        medics = medics.filter(addresses__neighborhood=neighborhood)
    else:
        if city is not None:
            medics = medics.filter(addresses__neighborhood__city=city)
        elif state is not None:
            medics = medics.filter(addresses__neighborhood__city__state=state)
        
    if len(medics) > 0:
        paginator = Paginator(medics, 8) # objeto de consulta, e qntd que desejamo retornar nohtml
        page = request.GET.get('page')
        medics = paginator.get_page(page)

    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()


    context = {
        'medics': medics,
        'parameters': parameters
    }                             
    
    return render(request, template_name='medic/medics.html', context=context, status=200)

# REQUEST é o parâmetro PADRÃO de uma view(func, class), aqui parâmetro requisita todos os dados do usuário para um servidor VIA URL.

# GET, POST, PUT e DELETE: Esses são métodos usados para interagir com um SERVIDOR WEB. 
# quando quiser saber algo que foi escrito na caixinha da web (na URL), como quando alguém te dá um recadinho.

# request.GET ->  um objeto em Django que contém todos os parâmetros passados na URL

# request.GET.get("nome"): Retorna o valor do parâmetro chamado "nome" passado na URL.
# request.GET.items(): Retorna uma lista de tuplas com todos os pares chave-valor dos parâmetros na URL.
# request.GET.keys(): Retorna uma lista de todas as chaves (nomes dos parâmetros) na URL.
# request.GET.values(): Retorna uma lista de todos os valores dos parâmetros na URL.
# request.GET.getlist("nome"): Retorna uma lista de valores para o parâmetro "nome" na URL, caso ele apareça várias vezes.



def add_favorite_view(request):
    page = request.POST.get("page") # Usando método acessar os dados enviados através do corpo de uma requisição POST:
    name = request.POST.get("name")
    speciality = request.POST.get("speciality")
    neighborhood = request.POST.get("neighborhood")
    city = request.POST.get("city")
    state = request.POST.get("state")
    id = request.POST.get("id")

    try:
        profile = Profile.objects.filter(user=request.user).first() # Pegando o perfil do usuário logado
        medic = Profile.objects.filter(user__id=id).first()         # Pegando o perfil do médico pelo id
        profile.favorites.add(medic.user)                           # add, um método que usamos em um atributo de tipo many to many field
        profile.save()
        msg = "Favorito adicionado com sucesso"                     # msg e type são 2 var que serão usadas para exibir umamsg no template
        _type = "success"
    except Exception as e:
        print("Erro %s" % e)
        msg = "Um erro ocorreu ao salvar o médico nos favoritos"
        _type = "danger"
    if page:
        arguments = "?page=%s" % (page)
    else:
        arguments = "?page=1"
    if name:
        arguments += "&name=%s" % name
    if speciality:
        arguments += "&specinality=%s" % speciality
    if neighborhood:
        arguments += "&neighborhood=%s" % neighborhood
    if city:
        arguments += "&city=%s" % city
    if state:
        arguments += "&state=%s" % state

    arguments += "&msg=%s&type=%s" % (msg, _type)

    return redirect(to='/medic/%s' % arguments) # redirecionando o usuário para uma url específica



# request.POST.items(): Retorna uma lista de tuplas contendo todos os pares chave-valor dos campos enviados na requisição POST.

# request.POST.keys(): Retorna uma lista de todas as chaves (nomes dos campos) enviados na requisição POST.

# request.POST.values(): Retorna uma lista de todos os valores dos campos enviados na requisição POST.

# request.POST.getlist("nome"): Retorna uma lista de valores para o campo "nome" na requisição POST, caso ele apareça várias vezes.

# request.POST.dict(): Retorna um dicionário contendo todos os campos e seus valores da requisição POST.


def remove_favorite_view(request):
    page = request.POST.get("page")
    id = request.POST.get("id")

    try:
        profile = Profile.objects.filter(user=request.user).first()
        medic = Profile.objects.filter(user__id=id).first()
        profile.favorites.remove(medic.user)
        profile.save()
        msg = "Favorito removido com sucesso."
        _type = "success"
    except Exception as e:
        print("Erro %s" % e)
        msg = "Um erro ocorreu ao remover o médico nos favoritos."
        _type = "danger"


    if page:
        arguments = "?page=%s" % (page)
    else:
        arguments = "?page=1"

    arguments += "&msg=%s&type=%s" % (msg, _type)

    return redirect(to='/profile/%s' % arguments)




def rate_medic(request, medic_id=None):
    medic = Profile.objects.filter(user__id=medic_id).first()
    rating = Rating.objects.filter(user=request.user, user_rated=medic.user).first()
    message = None
    initial = {'user': request.user, 'user_rated': medic.user}

    # se já temos uma avaliação criada, ela será carregada no formulário, permitindo edição
    if request.method == 'POST':  # Envia dados do cliente (geralmente um navegador web) para o servidor. 
        ratingForm = MedicRatingForm(request.POST, instance=rating, initial=initial)

    # caso não haja, criaremos uma avaliação
    else:
        ratingForm = MedicRatingForm(instance=rating, initial=initial)
        ratingForm = MedicRatingForm(instance=rating, initial=initial)


    # se os dados foram preenchido corretamentes
    if ratingForm.is_valid():
        ratingForm.save()
        message = {'type': 'success', 'text': 'Avaliação salva com sucesso'}

    else:
        if request.method == 'POST':
            message = {'type': 'danger', 'text': 'Erro ao salvar avaliação'}

    context = {
        'ratingForm': ratingForm,
        'medic': medic,
        'message': message
    }

    return render(request, template_name='medic/rating.html', context=context, status=200)