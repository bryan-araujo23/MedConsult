# Importando as classes HttpRequest, HttpResponse

from django.http import HttpResponse

# home_view é método que vamos disparar através da url
# request é o parâmetro padrão da view, esse parâmetro 
# recupera todos os dados do usuário logado

# para que a view funcione corretamente em nossa aplicação
# precisamos adicionar o arquivo local: HomeView.py dentro de __init__.py

def home_view(request):            
    return HttpResponse('<h1>Olá mundo!</h1>', status=200)


