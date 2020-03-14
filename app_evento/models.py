from django.contrib.auth.models import User
from django.db import models

class Pessoa(models.Model):
	nome= models.CharField('Nome',max_length=128)
	email= models.EmailField('E-mail', null=True, blank=True)

	def _str_(self):
		return self.nome


class PessoaFisica(models.Model):
	pessoa=models.ForeignKey(Pessoa, on_delete=models.CASCADE,blank=True,null=True)
	cpf=models.CharField('CPF', max_length=15,
		help_text='Número do cpf no formato 1111111111',null=True,
		blank=True,)

	def _str_(self):
		return self.cpf

class evento(models.Model):
    nome = models.CharField('nome',max_length = 50)
    sigla = models.CharField('sigla',max_length = 50)
    data_icinio = models.DateField('Data de Inicio')
    realizador = models.CharField ('realizador', max_length = 50)
    descricao = models.TextField()


class Ingresso(models.Model):
	discricao=models.CharField('Nome',max_length=128)
	valor=models.FloatField()
	evento=models.ForeignKey(evento, on_delete=models.CASCADE,blank=True,null=True)

	def _str_(self):
		return self.discricao



class Iscricao(models.Model):
	pessoa=models.ForeignKey(Pessoa, on_delete=models.CASCADE,blank=True,null=True)
	evento=models.ForeignKey(evento, on_delete=models.CASCADE,blank=True,null=True)
	ingresso=models.ForeignKey(Ingresso,on_delete=models.CASCADE,blank=True,null=True)





