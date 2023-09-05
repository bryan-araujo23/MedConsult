from django.test import TestCase, Client          # classe Client, realizar requisições HTTPS dentro de nossos testes
from django.contrib.auth.models import User       # Importa o modelo de usuário do Django
from medicSearch.models.profile import Profile    # Importa o modelo de perfil do aplicativo "medicSearch"
from django.db import transaction, IntegrityError # usados para gerenciar transações de banco de dados e capturar erros de integridade do banco de dados.

class MedicViewTestClass(TestCase):
    def setUp(self): # função especial, que executada antes de cada teste individual.usado para configurar o ambiente de teste, criar objetos ou executar qualquer preparação necessária para os testes.
        try: # tente
            with transaction.atomic(): # Inicia uma transação de banco de dados
                user = User.objects.create(username='teste.unitario', password='123456') # Cria um novo usuário com nome de usuário 'teste.unitario' e senha '123456'
                profile = Profile.objects.get(user=user) # Obtém o perfil associado ao usuário recém-criado
                profile.role = 2 # Define o campo 'role' do perfil como 2(médico)
                profile.save()   # Salva as alterações no perfil

        except IntegrityError as e: # Captura a exceção de integridade de banco de dados e a associa à variável 'e'
            print("Erro ao criar usuário. Descrição: %s" % e)  # Imprime uma mensagem de erro com a descrição da exceção

        self.client = Client() # Cria uma instância do cliente de teste do Django e a associa a 'self.client'

        def test_medics_list(self):
            response = self.client.get('/medic/') # # Faz uma solicitação GET à URL '/medic/'
            self.assertEqual(response.status_code, 200) # Verifica se o código de status da resposta é 200 (OK)
            self.assertContains(response, 'Foram encontrados: 1 medico(s)') # Verifica se a resposta contém o texto especificado