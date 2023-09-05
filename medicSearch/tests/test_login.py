from django.test import TestCase, Client
from django.contrib.auth.models import User

class LoginTestClass(TestCase):
    def setUp(self):
        # Cria um usuário de teste no banco de dados
        User.objects.create(username='teste.unitario', password='123456')
        # Cria uma instância do cliente de teste do Django
        self.client = Client()

    def test_login(self):
        # Faz uma solicitação POST para '/login' com dados de usuário
        response = self.client.post('/login', {       # endpoint seria a URL /login
            'username': 'teste.unitario',
            'password': '123456'
        }, **{'Content-Type': 'application/x-www-form-urlencoded'})
        
        # Verifica se o código de status da resposta é 200 (OK)
        self.assertEqual(response.status_code, 200)