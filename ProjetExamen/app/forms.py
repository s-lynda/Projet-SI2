from django.forms import ModelForm

from .models import Stage,Enseignant,Entreprise,Membre_Entreprise,Stagiaire,Jury

class stageform (ModelForm):
    class Meta:
        model = Stage
        fields="__all__"
class Enseignantform (ModelForm):
    class Meta:
        model = Enseignant
        fields="__all__"
class Entrepriseform (ModelForm):
    class Meta:
        model = Entreprise
        fields="__all__"
class Membre_Entrepriseform (ModelForm):
    class Meta:
        model = Membre_Entreprise
        fields="__all__"
class Stagiaireform (ModelForm):
    class Meta:
        model = Stagiaire
        fields="__all__"
class Juryform (ModelForm):
    class Meta:
        model = Jury
        fields="__all__"

