from cProfile import label
from django.db import models
from django.urls import reverse

class Enseignant(models.Model):
    CodeE=models.CharField(primary_key=True,max_length=50)
    NomE=models.CharField(max_length=50)
    PrenomE=models.CharField(max_length=50)
    GradeE=models.CharField(max_length=50)
    TelE1=models.CharField(max_length=10,null=True)
    TelE2=models.CharField(max_length=10,null=True,blank=True)
    EmailE=models.EmailField(max_length=254,null=True)
    #Jury=models.ForeignKey("Jury" , on_delete=models.SET_NULL,null=True, blank=True)
    def __str__(self):
     
        return  self.NomE+' ' +self.PrenomE


class Entreprise(models.Model):
    E_name=models.CharField(max_length=50)
    E_domaine=models.CharField(max_length=50)
    email_E=models.EmailField(max_length=254,null=True)
    address= models.CharField(max_length=50,null=True)
    NTel1 =models.CharField(max_length=10,null=True)
    NTel2 =models.CharField(max_length=10,null=True,blank=True)
    def __str__(self):
        return self.E_name

class Membre_Entreprise(models.Model):
    CodeM=models.CharField(primary_key=True,max_length=50)
    NomP=models.CharField(max_length=50)
    PrenomP=models.CharField(max_length=50)
    GradeP=models.CharField(max_length=50)
    TelP1=models.CharField(max_length=10,null=True)
    TelP2=models.CharField(max_length=10,null=True,blank=True)
    EmailP=models.EmailField(max_length=254,null=True)
    #Jury=models.ForeignKey("Jury" , on_delete=models.SET_NULL,null=True, blank=True)
    entreprise=models.ForeignKey(Entreprise,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.NomP + ' '+ self.PrenomP

class Stagiaire(models.Model):
    matricule= models.CharField(primary_key=True,max_length=12)
    last_name=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    birthday=models.DateField()
    spceciality=models.CharField(max_length=50)
    level=models.IntegerField()
    Tel1=models.CharField(max_length=10,null=True)
    Tel2=models.CharField(max_length=10,null=True,blank=True)
    Email=models.EmailField(max_length=254,null=True)
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Jury(models.Model):
    J_name=models.CharField(max_length=50)
    date=models.DateField()
    Enseignants=models.ManyToManyField(Enseignant)
    Membre_Entreprises=models.ManyToManyField(Membre_Entreprise)
    def __str__(self):
        return self.J_name

stage_type=(
    ("Ouvrier", "1- Stage Ouvrier"),
    ("Court","2- Stage Court durée"),
    ("PFE","3- Stage fin d'étude (PFE)"),
)
class Stage(models.Model):
    
    Theme=models.CharField(max_length=50)
    Period=models.CharField(max_length=50)
    Date_Deb=models.DateField()
    Date_Fin=models.DateField()
    domaine=models.CharField(max_length=50)
    type=models.CharField(max_length=100,choices=stage_type)
    Rapport=models.FileField(blank=True, null= True, upload_to="file/%Y/%m/%D")

    stagiaires=models.ManyToManyField(Stagiaire,related_name="stages" )
    mmbr_entreprise=models.ForeignKey(Membre_Entreprise, on_delete=models.CASCADE)
    enseignant=models.ForeignKey(Enseignant, on_delete=models.SET_NULL,null=True, blank=True )
    soutenire=models.ForeignKey(Jury , on_delete=models.SET_NULL,null=True, blank=True)

    def __str__(self):
        return self.Theme   
    