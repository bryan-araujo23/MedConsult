from medicSearch.models import *


# Tabela onde serão adicionadas as pontuações dos médicos
class Rating(models.Model):
    user = models.ForeignKey(User, related_name='avaliou', on_delete=models.CASCADE)
    # avaliado pelo usuário
    user_rated = models.ForeignKey(User, related_name='Avaliado', on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    opinion = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Avaliador: {self.user.first_name} | Avaliado: {self.user_rated}'