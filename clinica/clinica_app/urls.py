
from django.urls import path
from .views import Home, Sobre, Contato, Login, Logout_admin, Index, Ver_Medico, Deletar_Medico, Adicionar_Medico, Ver_Paciente, Deletar_Paciente, Adicionar_Paciente, Ver_Agenda, Adicionar_Agenda, Deletar_Agenda

urlpatterns = [
    path('', Home, name='home'),
    path('sobre/', Sobre, name='sobre'),
    path('contato/', Contato, name='contato'),
    path('admin_login/', Login, name='admin_login'),
    path('logout/', Logout_admin, name='logout_admin'),
    path('index/', Index, name='dashboard'),
    path('ver_paciente/', Ver_Paciente, name='ver_pacientes'),
    path('deletar_pacientes(?p<int:pid>)/', Deletar_Paciente, name='deletar_pacientes'),
    path('adicionar_pacientes/', Adicionar_Paciente, name='adicionar_pacientes'),
    path('ver_medicos/', Ver_Medico, name='ver_medicos'),
    path('adicionar_medicos/', Adicionar_Medico, name='adicionar_medico'),
    path('deletar_medicos(?p<int:pid>)/', Deletar_Medico, name='deletar_medicos'),
    path('ver_agenda/', Ver_Agenda, name='ver_agenda'),
    path('adicionar_agenda/', Adicionar_Agenda, name='adicionar_agenda'),
    path('deletar_agenda(?p<int:pid>)/', Deletar_Agenda, name='deletar_agenda'),
    path('adicionar_agenda/<int:pk>/', Adicionar_Agenda, name='editar_agendamento'),
    path('adicionar_medicos<int:pk>/', Adicionar_Medico, name='editar_medico'),
    path('adicionar_pacientes<int:pk>/', Adicionar_Paciente, name='editar_pacientes')
]