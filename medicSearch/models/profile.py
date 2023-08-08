from django.db import models
from django.dispatch import receiver # usado para tratar sinais (eventos) ocorrem durante o uso  do app
from medicSearch.models import *    # importando todas as classes que existem em models.py do nosso app

class Profile(models.Model):
    """
    user = models.OneToOneField Significa que cada perfil está associado a um único usuário.
    on_delete= models.CASCADE Quando um usuário é excluído, seu perfil também será excluído.
    role = função ou cargo do usuário. Escolha pré-definida de 3 opções para o papel do usuário.
    birthday = campo do tipo data(padrão=nada) permite que fique em braco no formulário e BD.
    create_at = novo registro é criado ou atualizado, data e hora atual são automaticamente preenchidos
    token = campo do tipo caractere, que armazena um token de autenticação.

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    role = models.IntegerField(choices=ROLE_CHOICE, default=3)
    birthday = models.DateField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=255, null=True, blank=True)

    image = models.ImageField(null=True, blank=True)

    favorites = models.ManyToManyField(User, blank=True, related_name='favorites')
    specialties = models.ManyToManyField(Speciality, blank=True, related_name='specialties')
    addresses = models.ManyToManyField(Address, blank=True, related_name='addresses')
    

    def __str__(self):
        return f'{self.user.username}'
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """
        Função decorada ela será acionada em resposta a um determinado sinal(evento), 
        no caso o sinal é: post_save que é acionado após salvar um objeto no banco de dados,
        remetente (sender) do sinal é o modelo User.
        Resumindo: quando um obj do modelo User é salvo(quando criamos um novo usuário, ou atualizamos)
        esta função é chamada.

        """
        try:
            if created:
                Profile.objects.create(user=instance)
        except:
            pass

    @receiver(post_save, sender=User)        
    def save_user_profile(sender, instance, **kwargs):
        """
        função também é decorada com @receiver que significa que ela responderá 
        ao sinal post_save emitido pelo modelo User quando um usuário é salvo.

        sender: O modelo que emitiu o sinal, ou seja, User.
        instance: A instância do objeto que foi salvo, que é um usuário neste caso.
        **kwargs: Parâmetros adicionais.

        """
        try:
            instance.profile.save()
        except:
            pass

