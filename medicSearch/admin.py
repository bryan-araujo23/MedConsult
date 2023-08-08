from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    # Componente que  cria um filtro de hierarquia com datas na tabela adm
    date_hierarchy =  'created_at'
    # Componente que informa Quais elementos serão exibidos na tabela adm
    list_display = ('user', 'role', 'birthday', 'specialtiesList', 'addressesList', )
    # Componente alterar apresentação dos campos vazios na tabela adm
    empty_value_display = '----'
    # Componente para criar link nos campos na tabela adm
    list_display_links = ('user', 'role',)
    # Componente cria uma filtro de dados baseados nos campos que foram adc
    list_filter = ('user__is_active', 'role')
    # Componente permite dizer quais campos serão exibidos no formulário ou não.
    # fields = ('user', ('role'), 'image', 'birthday', 'specialties', 'addresses')
    # Componentes oposto de fields. Ele removerá os campos citados
    exclude = ('favorites', 'created_at', 'updated_at')
    # Componente que deixa o campo apenas para leitura no formulário de edição e criação.
    readonly_fields = ('user', )
    # Componente que lista os campos que poderão ser pesquisados na tela de listagem do adm.
    search_fields = ('user__username', )

    # Customização Avançada
    # Similar ao field, porém aqui podemos agrupar os campos no formulário
    # para que  ele fique dividido de forma mais organizada na tela.

    fieldsets = (
    ('Usuário', {'fields': ('user', 'birthday', 'image')}),
    ('Função',  {'fields': ('role',)}),
    ('Extras',  {'fields': ('specialties', 'addresses')}),
    )
    
    # listando os campos ManyToManyFields(um para muitos)
    # Para fazer isso, precisamos apenas criar os campos customizados
    
    def specialtiesList(self, obj):
        return [i.name for i in obj.specialties.all()]
    def addressesList(self, obj):
        return [i.name for i in obj.addresses.all()]

    # Usaremos método: empty_value_display para customizar campo do
    # list_display(Componente insere elementos serão exibidos na tabela adm)
    # personalizar a exibição dos dados quando ov valor da data de anivesário estiver vazio.

    def birthday(self, obj):
        if obj.birthday:
            return obj.birthday.strftime("%d/%m/%Y")
    birthday.empty_value_display = '__/__/____'

    # Podemos adc arquivos:CSS e JS em nossa página adm

    class Media:
        css = {
            "all": ("css/custom.css", )
        }
        js = ("js/custom.js", )
    

# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)
