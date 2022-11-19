from django.contrib import admin
from .models import  Enseignant, Entreprise,Membre_Entreprise,Stagiaire,Stage ,Jury

admin.site.register(Enseignant)
admin.site.register(Entreprise)
admin.site.register(Membre_Entreprise)
admin.site.register(Stagiaire)
admin.site.register(Jury)
admin.site.register(Stage)