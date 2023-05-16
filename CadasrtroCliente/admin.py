from django.contrib import admin
from CadasrtroCliente.models import Cliente, Profissao, Telefone, Interesse
# Register your models here.
#Classe para exibir Telefone no cadastro de Clientes
class Telefones(admin.StackedInline):
    model = Telefone
    extra = 0

class ClientAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "cidade"]
    list_display_links = ["id", "nome"]
    list_filter = ['bairro', "cidade", "Ativo"]
    inlines = [Telefones]

admin.site.register(Cliente, ClientAdmin)
admin.site.register(Profissao)
admin.site.register(Telefone)
admin.site.register(Interesse)