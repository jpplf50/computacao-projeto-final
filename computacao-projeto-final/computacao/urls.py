from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'computacao'

urlpatterns = [
                  path('', views.index, name='index'),
                  path('index/', views.index, name='index'),
                  path('automatos/', views.automatos, name='automatos'),
                  path('turing/', views.turing, name='turing'),
                  path('expressoes/', views.expressoes, name='expressoes'),
                  path('nova_turing/', views.nova_turing, name='nova_turing'),
                  path('novo_automato/', views.novo_automato, name='novo_automato'),
                  path('nova_expressao/', views.nova_expressao, name='nova_expressao'),
                  path('edita_automato/<int:automato_id>/', views.edita_automato, name='edita_automato'),
                  path('apaga_automato/<int:automato_id>/', views.apaga_automato, name='apaga_automato'),
                  path('edita_maquina/<int:maquina_id>/', views.edita_maquina, name='edita_maquina'),
                  path('apaga_maquina/<int:maquina_id>/', views.apaga_maquina, name='apaga_maquina'),
                  path('edita_expressao/<int:expressao_id>/', views.edita_expressao, name='edita_expressao'),
                  path('apaga_expressao/<int:expressao_id>/', views.apaga_expressao, name='apaga_expressao'),
                  path('<int:automato_id>/automato/', views.automato, name='automato'),
                  path('<int:maquina_id>/maquina/', views.maquina, name='maquina'),
                  path('<int:expressao_id>/expressao/', views.expressao, name='expressao'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)