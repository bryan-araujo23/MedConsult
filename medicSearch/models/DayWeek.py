from medicSearch.models import *

# Dias da Semana em que abrirá
class DayWeek(models.Model): 
    name = models.CharField(null=False, max_length=20)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.name}'