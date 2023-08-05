from medicSearch.models import *

# Estado do país
class State(models.Model):
    name = models.CharField(null=False, max_length=30)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True) # Atualizar em
    update_at = models.DateTimeField(auto_now=True)      # Criado em

    def __str__(self):
        return f'{self.name}'