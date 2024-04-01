from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data): #data pega todas as variáveis dos campos
        if not cpf_valido(data['cpf']): # data['nome_do_campo'] especifica qual campo quer pegar
            raise serializers.ValidationError({ 'cpf':"O CPF é inválido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "Não inclua números neste campo"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "O RG deve ter 9 dígitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O número de celular é inválido. Ele deve seguir o modelo (XX) 9XXXX-XXXX"})
        return data #deve ser apenas no final de todas as validações... a funcao retorna apenas no final dela

    # def validate_cpf(self, cpf):
    #     if len(cpf) != 11:
    #         raise serializers.ValidationError("O CPF deve ter 11 dígitos")
    #     return cpf
    # def validate_nome(self, nome):
    #     if not nome.isalpha():
    #         raise serializers.ValidationError("Não inclua números neste campo")
    #     return nome
    # def validate_rg(self, rg):
    #     if len(rg) != 9:
    #         raise serializers.ValidationError("O RG deve ter 9 dígitos")
    #     return rg
    # def validate_celular(self, celular):
    #     if len(celular)  < 11:
    #         raise serializers.ValidationError("O número de celular deve ter no mínimo 11 dígitos")
    #     return celular
