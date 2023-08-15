from django.shortcuts import render
from medicSearch.models import Profile
from django.core.paginator import Paginator

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




