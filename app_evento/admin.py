from django.contrib import admin
from .models import PessoaFisica,Pessoa,evento,Ingresso,Iscricao


@admin.register(PessoaFisica)
class PessoaFisicaAdmin(admin.ModelAdmin):
	pass


@admin.register(Pessoa)
class Pessoa(admin.ModelAdmin):
	pass

@admin.register(evento)
class evento(admin.ModelAdmin):
	pass

@admin.register(Ingresso)
class Ingresso(admin.ModelAdmin):
	pass


@admin.register(Iscricao)
class Iscricao(admin.ModelAdmin):
	pass