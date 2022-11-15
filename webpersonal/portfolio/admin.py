from django.contrib import admin
from .models import Project


# Vamos a crear una clase
# para extender las configuraciones del admin
# podemos colocar cualquier nombre, peor esta en la nomenclatura
class ProjectAdmin(admin.ModelAdmin):
    # Es una tupla que vamos a redefinir
    readonly_fields = ('created', 'updated')


# hay que pasarle la configuracion extendida
admin.site.register(Project, ProjectAdmin)
