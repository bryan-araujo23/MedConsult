# Importando as classes HttpRequest, HttpResponse

from django.shortcuts import render

# home_view é método que vamos disparar através da url
# request é o parâmetro padrão da view, esse parâmetro recupera todos os dados do usuário logado

# para que a view funcione corretamente em nossa aplicação
# precisamos adicionar o arquivo local: HomeView.py dentro de __init__.py
# Por padrão o render procura os templates dentro da pasta de template, não precisando indicar a pasta
# templates ao renderizar uma página ficando home/home.html

def home_view(request):            
    return render(request, template_name='home/home.html', status=200)




