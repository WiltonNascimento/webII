from django.shortcuts import render, redirect, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Medico, Paciente, Consulta
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def Sobre(request):
    return render(request, 'sobre.html')

def Home(request):
    return render(request, 'home.html')

def Contato(request):
    return render(request, 'contato.html')

def Index(request):
    if not request.user.is_staff:
        return redirect ('login')
    medicos = Medico.objects.all()
    pacientes = Paciente.objects.all()
    agenda = Consulta.objects.all()
    m=0
    p=0
    a=0
    for i in medicos:
        m+=1
    for i in pacientes:
        p+=1
    for i in agenda:
        a+=1
    m1 = {'m':m, 'p':p, 'a':a}
    return render(request, 'index.html', m1)

def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['nome']
        p = request.POST['senha']
        user = authenticate(username= u, password = p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"

            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'login.html', d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    
    logout(request)
    return redirect('admin_login')

def Adicionar_Medico(request, pk=None):
    if pk:  # Modo de edição
        medico = get_object_or_404(Medico, pk=pk)
        titulo = "Editar Médico"
        acao = "editar"
    else:  # Modo de criação
        medico = None
        titulo = "Adicionar Médico"
        acao = "adicionar"

    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        crm = request.POST.get("crm")
        celular = request.POST.get("telefone")
        especialidade = request.POST.get("especialidade")
        
        try:
            if medico:  # Atualizar médico existente
                medico.nome_medico = nome
                medico.email = email
                medico.crm = crm
                medico.celular = celular
                medico.especialidade = especialidade
                medico.save()
                mensagem = "editado"
            else:  # Criar novo médico
                Medico.objects.create(
                    nome_medico=nome,
                    email=email,
                    crm=crm,
                    celular=celular,
                    especialidade=especialidade
                )
                mensagem = "adicionado"
            return render(request, 'adicionar_medico.html', {'error': 'no', 'mensagem': mensagem})
        except Exception as e:
            print(f"Erro: {e}")  # Para depuração
            return render(request, 'adicionar_medico.html', {'error': 'yes', 'acao': acao})

    return render(request, 'adicionar_medico.html', {'medico': medico, 'titulo': titulo, 'acao': acao})


def Ver_Medico(request):
    if not request.user.is_staff:
        return redirect('login')
    medicos = Medico.objects.all()  
    return render(request, 'ver_medicos.html', {'medicos': medicos})

def Deletar_Medico(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    medico1 = Medico.objects.get(id=pid)
    medico1.delete()
    return redirect('ver_medicos')

from django.shortcuts import render, redirect
from .models import Paciente

from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente

def Adicionar_Paciente(request, pk=None):
    if not request.user.is_staff:
        return redirect('login')

    if pk:  # Modo de edição
        paciente = get_object_or_404(Paciente, pk=pk)
        titulo = "Editar Paciente"
        acao = "editar"
    else:  # Modo de criação
        paciente = None
        titulo = "Adicionar Paciente"
        acao = "adicionar"

    error = ""
    mensagem = ""

    if request.method == "POST":
        n = request.POST.get('nome')
        g = request.POST.get('genero')
        m = request.POST.get('telefone')
        ed = request.POST.get('endereco')
        dc = request.POST.get('documento')
        ns = request.POST.get('nascimento')

        try:
            if paciente:  # Atualizar paciente existente
                paciente.nome_paciente = n
                paciente.genero = g
                paciente.celular = m
                paciente.endereco = ed
                paciente.documento = dc
                paciente.data_nascimento = ns
                paciente.save()
                mensagem = "editado"
            else:  # Criar novo paciente
                Paciente.objects.create(
                    nome_paciente=n,
                    genero=g,
                    celular=m,
                    endereco=ed,
                    documento=dc,
                    data_nascimento=ns
                )
                mensagem = "adicionado"

            error = "no"
        except Exception as e:
            print(f"Erro: {e}")  # Log para depuração
            error = "yes"

    return render(request, 'adicionar_pacientes.html', {
        'titulo': titulo,
        'error': error,
        'mensagem': mensagem,
        'paciente': paciente,
        'acao': acao
    })

def Ver_Paciente(request):
    if not request.user.is_staff:
        return redirect('login')
    pacientes = Paciente.objects.all()  
    return render(request, 'ver_pacientes.html', {'pacientes': pacientes})

def Deletar_Paciente(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    paciente1 = Paciente.objects.get(id=pid)
    paciente1.delete()
    return redirect('ver_pacientes')

def Adicionar_Agenda(request, pk=None):
    error = ""
    if pk:  # Se `pk` for fornecido, é uma edição
        agendamento = get_object_or_404(Consulta, pk=pk)
        titulo = "Editar Agendamento"
        mensagem = "editada"
        acao = "editar"
    else:  # Caso contrário, é uma criação
        agendamento = None
        titulo = "Agendar Consulta"
        mensagem = "adicionada"
        acao = "adicionar"
    
    if request.method == "POST":
        medico = request.POST.get("medico")
        paciente = request.POST.get("paciente")
        data = request.POST.get("data")
        hora = request.POST.get("hora")
        observacoes = request.POST.get("observacoes")
        
        try:

            medico = Medico.objects.get(id=medico)
            paciente = Paciente.objects.get(id=paciente)

            if agendamento:  # Atualizar agendamento existente
                agendamento.medico = medico
                agendamento.paciente = paciente
                agendamento.data = data
                agendamento.hora = hora
                agendamento.observacoes = observacoes
                agendamento.save()
            else:  # Criar novo agendamento
                Consulta.objects.create(
                    medico=medico,
                    paciente=paciente,
                    data=data,
                    hora=hora,
                    observacoes=observacoes,
                )
            return render(request, 'adicionar_agenda.html', {'error': 'no', 'mensagem': mensagem})
        except Exception:
            return render(request, 'adicionar_agenda.html', {'error': 'yes', 'acao': acao})

    # Obter médicos e pacientes para o formulário
    medicos = Medico.objects.all()
    pacientes = Paciente.objects.all()

    return render(request, 'adicionar_agenda.html', {
        'medico': medicos,
        'paciente': pacientes,
        'agendamento': agendamento,
        'titulo': titulo,
        'mensagem': mensagem,
        'acao': acao,
    })

def Ver_Agenda(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Consulta.objects.all()
    d = {'doc': doc}
    return render(request, 'ver_agenda.html', d)

def Deletar_Agenda(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    agenda = Consulta.objects.get(id=pid)
    agenda.delete()
    return redirect('ver_agenda')