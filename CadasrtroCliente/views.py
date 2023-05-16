

from django.shortcuts import render

from CadasrtroCliente.models import Cliente, Profissao, Telefone

# Create your views here.
def index(request):
    meu_nome = "Washington Junior"
    lista_frutas = ["Laranja", "Manga", "Banana"]
    context = {
    "nome": meu_nome,
    "frutas": lista_frutas
    }
    return render(request, "index.html", context)

def lista_clientes(request):
    lista_clientes = Cliente.objects.all()
    lista_profissoes = Profissao.objects.all()
    context = {
        "clientes": lista_clientes,
         "profissoes": lista_profissoes,
    }
    return render(request, "lista_clientes.html", context)

def lista_profissoes(request):
    lista_profissoes = Profissao.objects.all()
    context={
        "profissoes": lista_profissoes
    }
    return render(request, "lista_profissoes.html", context)

def detalhar_cliente(request, id):
    #Buscando no banco de dados o cliente pelo ID
    cliente = Cliente.objects.get(id = id)
    telefones = Telefone.objects.filter(cliente_id = id)
    
    context = {
        "cliente": cliente,
        "telefones": telefones
    }
    return render(request, "cliente_detalhes.html", context)

