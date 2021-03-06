from django.urls import path
from .views import agenda, delagenda, index, reservarhora, registrar, iniciarsesion, contacto, medicos, ubicaciones, anularhora, confirmarhora, delhora, cajeropagar, comprobantepago, secretaria, modificaragendamedico, medico, agregaragenda, modificarcita, modificarcitapaciente


urlpatterns = [
    path('', iniciarsesion, name="iniciarsesion"),
    path('index', index, name="index"),
    path('reservarhora', reservarhora, name="reservarhora"),
    path('registrar', registrar, name="registrar"),
    path('contacto', contacto, name="contacto"),
    path('medicos', medicos, name="medicos"),
    path('ubicaciones', ubicaciones, name="ubicaciones"),
    path('confirmarhora', confirmarhora, name="confirmarhora"),
    path('anularhora', anularhora, name="anularhora"),
    path('anularhora/<id>', anularhora, name="anularhora"),
    path('delhora/<id>', delhora, name="delhora"),
    path('cajeropagar', cajeropagar, name="cajeropagar"),
    path('comprobantepago', comprobantepago, name="comprobantepago"),
    path('secretaria', secretaria, name="secretaria"),
    path('medico', medico, name="medico"),
    path('modificaragendamedico<id>', modificaragendamedico,name="modificaragendamedico"),
    path('agregaragenda', agregaragenda, name="agregaragenda"),
    path('delagenda<id>', delagenda, name="delagenda"),
    path('agenda', agenda, name="agenda"),
    path('modificarcita', modificarcita, name="modificarcita"),
    path('modificarcitapaciente<id>', modificarcitapaciente, name="modificarcitapaciente"),  

]
