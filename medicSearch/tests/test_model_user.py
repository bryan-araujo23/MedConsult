from django.test import TestCase
from django.contrib.auth.models import User


# Nosso primeiro teste de unidade que listará um usuáriodo django e, 
# caso retorne um valor, o teste estará correto.


class UserModelTestClass(TestCase): # classe(TestCase)
    def setUp(self):                # configurando ambiente de teste criando um objeto de usuário no DB
        User.objects.create(username='teste.unitário', password='123456') # Modelo user estamos criando um objeto

    def test_user_exist(self):       # função(UserModelTestClass)
        user = User.objects.first() # var = retorna o primeiro usuário encontrado no banco de dados
        self.assertIsNotNone(user) # verifica se esse usuário não é nulo.
        


# PRINCIPAIS MÉTODOS DO MÓDULO UNITTEST QUE PODEMOS UTILIZAR:

# assertFalse(expr, msg=None): Verifica se uma expressão é avaliada como False. Se a expressão for True, o teste falhará.
# assertTrue(expr, msg=None): Verifica se uma expressão é avaliada como True. Se a expressão for False, o teste falhará.