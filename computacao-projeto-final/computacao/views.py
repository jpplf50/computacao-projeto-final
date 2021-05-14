import re
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Automato, ExpressaoRegular, MaquinaTuring
from .forms import SequenciaForm, AutomatoForm, TuringForm, ExpressaoRegularForm


def index(request):
    return render(request, 'computacao/index.html')

def turing(request):
    context = {'maquinas': MaquinaTuring.objects.all()}
    return render(request, 'computacao/turing.html', context)

def nova_turing(request):
    form = TuringForm(request.POST or None)
    if form.is_valid():
        new_mt = form.save()
        new_mt.desenha_diagrama()
        new_mt.save()
        return HttpResponseRedirect(reverse('computacao:turing'))

    context = {'form': form}

    return render(request, 'computacao/nova_turing.html', context)

def maquina(request, maquina_id):
    sequencia = None
    resultado = None

    form = SequenciaForm(request.POST or None)
    if form.is_valid():
        sequencia = form.cleaned_data['sequencia']
        resultado = MaquinaTuring.objects.get(id=maquina_id).valida_sequencia(sequencia)
    
    context = {
        'maquina': MaquinaTuring.objects.get(id=maquina_id),
        'sequencia': sequencia,
        'resultado': resultado,
        'form': form
    }

    return render(request, 'computacao/maquina.html', context)

def edita_maquina(request, maquina_id):
    instance = MaquinaTuring.objects.get(id=maquina_id)
    form = TuringForm(request.POST or None, instance=instance)
    if form.is_valid():
        a = form.save()
        a.desenha_diagrama()
        a.save()
        return HttpResponseRedirect(reverse('computacao:turing'))

    context = {'form': form, 'maquina_id':maquina_id}
    return render(request, 'computacao/edita_maquina.html', context)

def apaga_maquina(request, maquina_id):
    MaquinaTuring.objects.filter(id=maquina_id).delete()
    context = {'maquinas': MaquinaTuring.objects.all()}
    return render(request, 'computacao/turing.html', context)


def automato(request, automato_id):

    sequencia = None
    resultado = None

    form = SequenciaForm(request.POST or None)
    if form.is_valid():
        sequencia = form.cleaned_data['sequencia']
        resultado = Automato.objects.get(id=automato_id).valida_sequencia(sequencia)

    context = {
        'automato': Automato.objects.get(id=automato_id),
        'sequencia': sequencia,
        'resultado': resultado,
        'form': form,
    }
    return render(request, 'computacao/automato.html', context)
    # """return render(request, 'computacao/test.html', {'automato_id':automato_id})"""

def automatos(request):

    context = {'automatos': Automato.objects.all()}
    return render(request, 'computacao/automatos.html', context)


def novo_automato(request):

    form = AutomatoForm(request.POST or None)
    if form.is_valid():
        new_automata = form.save()
        new_automata.desenha_diagrama()
        new_automata.save()
        return HttpResponseRedirect(reverse('computacao:automatos'))

    context = {'form': form}

    return render(request, 'computacao/novo_automato.html', context)


def edita_automato(request, automato_id):
    """if request.POST == 'POST':
        form = AutomatoForm(request.POST)
        form.save()"""

    instance = Automato.objects.get(id=automato_id)
    form = AutomatoForm(request.POST or None, instance=instance)
    if form.is_valid():
        a = form.save()
        a.desenha_diagrama()
        a.save()
        return HttpResponseRedirect(reverse('computacao:automatos'))

    """
    form = AutomatoForm(initial={
        'nome': automato_a_editar.nome,
        'descricao': automato_a_editar.descricao,
        'alfabeto': automato_a_editar.alfabeto,
        'estados': automato_a_editar.estados,
        'estadoInicial': automato_a_editar.estadoInicial,
        'estadosDeAceitacao': automato_a_editar.estadosDeAceitacao,
        'dicionarioTransicao': automato_a_editar.dicionarioTransicao,
    })"""
    context = {'form': form, 'automato_id':automato_id}
    return render(request, 'computacao/edita_automato.html', context)

def apaga_automato(request, automato_id):
    Automato.objects.filter(id=automato_id).delete()
    context = {'automatos': Automato.objects.all()}
    return render(request, 'computacao/automatos.html', context)

def expressoes(request):
    context = {'expressoes': ExpressaoRegular.objects.all()}
    return render(request, 'computacao/expressoes.html', context)

def nova_expressao(request):
    form = ExpressaoRegularForm(request.POST or None)
    if form.is_valid():
        new_mt = form.save()
        new_mt.save()
        return HttpResponseRedirect(reverse('computacao:expressoes'))

    context = {'form': form}

    return render(request, 'computacao/nova_expressao.html', context)

def expressao(request, expressao_id):
    sequencia = None
    resultado = None

    form = SequenciaForm(request.POST or None)
    if form.is_valid():
        sequencia = form.cleaned_data['sequencia']
        resultado = ExpressaoRegular.objects.get(id=expressao_id).valida_sequencia(sequencia)
    
    context = {
        'expressao': ExpressaoRegular.objects.get(id=expressao_id),
        'sequencia': sequencia,
        'resultado': resultado,
        'form': form
    }

    return render(request, 'computacao/expressao.html', context)

def edita_expressao(request, expressao_id):
    instance = ExpressaoRegular.objects.get(id=expressao_id)
    form = ExpressaoRegularForm(request.POST or None, instance=instance)
    if form.is_valid():
        a = form.save()
        a.save()
        return HttpResponseRedirect(reverse('computacao:expressoes'))

    context = {'form': form, 'expressao_id':expressao_id}
    return render(request, 'computacao/edita_expressao.html', context)

def apaga_expressao(request, expressao_id):
    ExpressaoRegular.objects.filter(id=expressao_id).delete()
    context = {'expressoes': ExpressaoRegular.objects.all()}
    return render(request, 'computacao/expressoes.html', context)