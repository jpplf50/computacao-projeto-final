from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Automato, ExpressaoRegular, MaquinaTuring


class SequenciaForm(forms.Form):
    sequencia = forms.CharField(label='',
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'insira uma sequência',
                                    'size': '25'
                                }))


class AutomatoForm(ModelForm):
    class Meta:
        model = Automato
        fields = '__all__'   # pode-se especificar lista dos campos q queremos. podemos querer tudo excluindo alguns
        exclude = ['diagrama']

        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'AFD que aceita sequências ...'}),
            'alfabeto': forms.TextInput(attrs={'class': 'form-control'}),
            'estados': forms.TextInput(attrs={'class': 'form-control'}),
            'estadoInicial': forms.TextInput(attrs={'class': 'form-control'}),
            'estadosDeAceitacao': forms.TextInput(attrs={'class': 'form-control'}),
            'dicionarioTransicao': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'nome': 'Nome do autómato',
            'descricao': 'Descrição',
            'alfabeto': 'Alfabeto de símbolos',
            'estados': 'Estados',
            'estadoInicial': 'Estado inicial',
            'estadosDeAceitacao': 'Estado de aceitação',
            'dicionarioTransicao': 'Transições'
        }

        placeholders = {
            'nome': 'Nome do autómato',
            'descricao': 'Descrição',
            'alfabeto': 'Alfabeto de símbolos',
            'estados': 'Estados',
            'estadoInicial': 'Estado inicial',
            'estadosDeAceitacao': 'Estado de aceitação',
            'dicionarioTransicao': 'Transições'
        }

        help_texts = {
            'nome': 'Atribua um nome, com no máximo 3 palavras,  que identifique o AFD',
            'descricao': 'Descreva o tipo de sequências que o autómato reconhece',
            'alfabeto': 'Insira os simbolos do alfabeto separados por espaços (e.g. "0 1")',
            'estados': 'Insira os nomes dos estados separados por espaços (e.g. "A B")',
            'estadosDeAceitacao': 'Insira os estados separados por espaços (e.g. "A B")',
            'dicionarioTransicao': 'Insira as transicoes estadoInicial-simbolo-estadoSeguinte (e.g. "A-0-B A-1-A")'
        }

class TuringForm(ModelForm):
    class Meta:
        model = MaquinaTuring
        fields = '__all__'   # pode-se especificar lista dos campos q queremos. podemos querer tudo excluindo alguns
        exclude = ['diagrama']

        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'MT que aceita sequências ...'}),
            'alfabeto': forms.TextInput(attrs={'class': 'form-control'}),
            'estados': forms.TextInput(attrs={'class': 'form-control'}),
            'estadoInicial': forms.TextInput(attrs={'class': 'form-control'}),
            'estadosDeAceitacao': forms.TextInput(attrs={'class': 'form-control'}),
            'dicionarioTransicoes': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'nome': 'Nome da Máquina de Turing',
            'descricao': 'Descrição',
            'alfabeto': 'Alfabeto de símbolos',
            'estados': 'Estados',
            'estadoInicial': 'Estado inicial',
            'estadosDeAceitacao': 'Estado de aceitação',
            'dicionarioTransicoes': 'Transições'
        }

        placeholders = {
            'nome': 'Nome da Máquina de Turing',
            'descricao': 'Descrição',
            'alfabeto': 'Alfabeto de símbolos',
            'estados': 'Estados',
            'estadoInicial': 'Estado inicial',
            'estadosDeAceitacao': 'Estado de aceitação',
            'dicionarioTransicoes': 'Transições'
        }

        help_texts = {
            'nome': 'Atribua um nome, com no máximo 3 palavras,  que identifique a MT',
            'descricao': 'Descreva o tipo de sequências que a máquina reconhece',
            'alfabeto': 'Insira os simbolos do alfabeto separados por espaços (e.g. "0 1") e d',
            'estados': 'Insira os nomes dos estados separados por espaços (e.g. "A B")',
            'estadoInicial': 'Insira o estado inicial',
            'estadosDeAceitacao': 'Insira os estados separados por espaços (e.g. "A B")',
            'dicionarioTransicoes': 'Insira as transicoes estadoInicial char próximoEstado charEscrever direção (e.g. "A-01R-B A-01L-B")'
        }

class ExpressaoRegularForm(ModelForm):
    class Meta:
        model = ExpressaoRegular
        fields = '__all__'   # pode-se especificar lista dos campos q queremos. podemos querer tudo excluindo alguns

        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'expressão que aceita ...'}),
            'expressao': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'nome': 'Nome da Expressão Regular',
            'descricao': 'Descrição',
            'expressao': 'Expressão Regular'
        }

        placeholders = {
            'nome': 'Nome da Expressão Regular',
            'descricao': 'Descrição',
            'expressao' : 'Expressão Regular'
        }

        help_texts = {
            'nome': 'Atribua um nome, com no máximo 3 palavras,  que identifique a Expressão Regular',
            'descricao': 'Descreva o tipo de sequências que a expressão reconhece',
            'expressao' : 'Escreva a Expressão Regular na forma de, por exemplo, ^(?<=\@)(?<=\.).*$'
        }
