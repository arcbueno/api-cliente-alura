from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
    def validate(self, data):
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf': "CPF inválido"})
        
        if (not validate_rg(data['rg'])):
            raise serializers.ValidationError({'rg': "RG deve conter 9 dígitos"})
            
        if(not validate_nome(data['nome'])):
            raise serializers.ValidationError({'nome': "Nome deve conter apenas letras"})
        if(not validate_celular(data['celular'])):
            raise serializers.ValidationError({'celular': "O celular deve seguir o padrão 99 99999-9999" })
        
        return data

    

   
    