from asyncio.windows_events import NULL
from datetime import datetime,timedelta

from django.shortcuts import  redirect, render
from .forms import stageform,Enseignantform,Entrepriseform,Membre_Entrepriseform,Stagiaireform,Juryform
from .models import Enseignant, Stagiaire,Entreprise ,Membre_Entreprise, Stage,Jury
from django.db.models import Count


def go_home(request):
    return render(request,"views\home.html")

def afficheEnseignants (request):
    engs=Enseignant.objects.all()
    return render(request,"Enseignant.html",{"ensg":engs})
def affiche_Entreprises (request):
    entreprise= Entreprise.objects.all()
    return render( request, "entreprise.html",{"Entreprise":entreprise})
def affiche_Membre_Entreprises (request):
    membre_Entreprise= Membre_Entreprise.objects.all()
    return render( request, "mmbr.html",{"Membre_Entreprise":membre_Entreprise})
def affiche_Stages (request):
    stage= Stage.objects.all()
    return render( request, "index.html",{"Stage":stage})
def affiche_Stagiaires (request):
    stagiaire= Stagiaire.objects.all()
    return render( request, "stagiaire.html",{"Stagiaire":stagiaire})
def affiche_Jurys (request):
    jury= Jury.objects.all()
    return render( request, "soutenance.html",{"Jury":jury})


def ajouter_stage (request):
    #durée de stage
    if request.method=="POST":
        form =stageform(request.POST, request.FILES)
        debut=request.POST.get('Date_Deb')
        fin=request.POST.get('Date_Fin')
        #ISO_format c YYYY-mm-dd
        duree= datetime.fromisoformat(fin)-datetime.fromisoformat(debut)
         #------------------- a revoir
        if(fin>debut):
            typestage=request.POST.get('type') 
            if(typestage=="Ouvrier"):
                list_stagiares=request.POST.getlist('stagiaires') 
                if len(list_stagiares)>=1 and len(list_stagiares)<=2:
                    if (duree==timedelta(days=15)):
                        if form.is_valid():
                            form.save()  
                            form=stageform()
                            return redirect("affiche_Stages") # .... redirection vers une autre page
                    else:
                            mssg="veuillez selectionner entre une date qui ne dure pas plus de 15jours ( 2 semaines precise)!"
                            return render(request,"stgform.html",{"form":form,"message":mssg})  
                else:
                    mssg="veuillez selectionner entre 1 et 2 stagiaires!" 
                return render(request,"stgform.html",{"form":form,"message":mssg}) 
            elif(typestage=="Court"):
                    list_stagiares=request.POST.getlist('stagiaires') 
                    if len(list_stagiares)>=1 and len(list_stagiares)<=4 :
                        if(duree>timedelta(days=42) and duree<timedelta(days=56)): 
                            if form.is_valid():
                                form.save()
                                form=stageform()
                                return redirect("affiche_Stages") # .... redirection vers une autre page
                        else:
                            mssg="veuillez selectionner entre une date qui ne dure pas plus de 56 jours et moins de 42 jours ( 6 semaines à 8 semaines max)!"
                            return render(request,"stgform.html",{"form":form,"message":mssg})  
                    else:
                        mssg="veuillez selectionner entre 1 et 4 stagiaires!"
                        return render(request,"stgform.html",{"form":form,"message":mssg})  
            elif(typestage=="PFE"):
                eng=request.POST.get('Enseigant')
                if (eng!=NULL and eng!=''):
                    list_stagiares=request.POST.getlist('stagiaires') 
                    if len(list_stagiares)>=1 and len(list_stagiares)<=2 :
                        if (duree <= timedelta(days=367) and duree >= timedelta(days=183)): # duree max une année et min 6 mois 
                            if form.is_valid():
                                form.save()  
                                form=stageform() 
                                return redirect("affiche_Stages") # .... redirection vers une autre page
                        else:
                            mssg="veuillez selectionner entre une date qui ne dure pas plus de 183 jours et moins de 367 jours ( 6 mois à 1 ans max)!"
                            return render(request,"stgform.html",{"form":form,"message":mssg}) 
                    else:
                        mssg="veuillez selectionner entre 1 et 2 stagiaires!" 
                else:
                        mssg="veuillez selectionner un Enseigant !" 
                return render(request,"stgform.html",{"form":form,"message":mssg})  
                
            else:
                    mssg="Stage n'existe pas !" 
                    return render(request,"stgform.html",{"form":form,"message":mssg}) 
        else:
                mssg="Date debut inferieur a date fin !" 
                return render(request,"stgform.html",{"form":form,"message":mssg}) 

    else :
        form = stageform(request.GET)
        form=stageform()
    return render(request,'stgform.html', {"form":form})
def ajouter_enseignant (request):
    
    if request.method=="POST":
        form = Enseignantform(request.POST)
        num1=request.POST.get('TelE1')
        num2=request.POST.get('TelE2')
        if(len(num1)==10 and (len(num2)==10 or len(num2)==0)):
            if form.is_valid():
                form.save()  
                form=stageform()
                return redirect("affiche_eng")
        else :
            mssg="Numero de telephone erronée !" 
            return render(request,'stgform.html', {"form":form,"message":mssg})
    else:       
     form = Enseignantform(request.GET)
     return render(request,'stgform.html', {"form":form})

def ajouter_Entreprise (request):
    if request.method =='POST':
        form =  Entrepriseform(request.POST)
        num1=request.POST.get('NTel1')
        num2=request.POST.get('NTel2')
        if(len(num1)==10 and (len(num2)==10 or len(num2)==0)):
            if form.is_valid():
                form.save()
                form = Entrepriseform()
                return redirect("affiche_ent")
        else :
            mssg="Numero de telephone erronée !" 
            return render(request,'stgform.html', {"form":form,"message":mssg})
    else:
        form=Entrepriseform(request.GET)
    return render(request,'stgform.html',{"form":form})

def ajouter_Membre_Entreprise (request):
    if request.method =='POST':
        form =  Membre_Entrepriseform(request.POST)
        num1=request.POST.get('TelP1')
        num2=request.POST.get('TelP2')
        if(len(num1)==10 and (len(num2)==10 or len(num2)==0)):
            if form.is_valid():
                form.save()
                form = Membre_Entrepriseform()
                return redirect("affiche_mmbr")
        else :
            mssg="Numero de telephone erronée !" 
            return render(request,'stgform.html', {"form":form,"message":mssg})
    else:
        form=Membre_Entrepriseform(request.GET)
    return render(request,'stgform.html',{"form":form})
def ajouter_Stagiaire (request):
    if request.method =='POST':
        form =  Stagiaireform(request.POST)
        num1=request.POST.get('Tel1')
        num2=request.POST.get('Tel2')
        if(len(num1)==10 and (len(num2)==10 or len(num2)==0)):
            if form.is_valid():
                form.save()
                form = Stagiaireform()
                return redirect("affiche_stgr")
        else :
            mssg="Numero de telephone erronée !" 
            return render(request,'stgform.html', {"form":form,"message":mssg})
    else:
        form=Stagiaireform(request.GET)
    return render(request,'stgform.html',{"form":form})
def ajouter_Jury (request):

    if request.method =='POST':
        form = Juryform (request.POST)
        if form.is_valid():
            form.save()
            form = Juryform()
            return redirect("affiche_sout")
    else:
        form=Juryform(request.GET)
    return render(request,'stgform.html',{"form":form})

def update_Stage(request,id):
    stage = Stage.objects.get(id=id)
    form =stageform(instance=stage)
    if request.method=="POST":
        form =stageform(request.POST, request.FILES, instance= stage)
        debut=request.POST.get('Date_Deb')
        fin=request.POST.get('Date_Fin')
        duree= datetime.fromisoformat(fin)-datetime.fromisoformat(debut)
         #------------------- a revoir
        if(fin>debut):
            typestage=request.POST.get('type') 
            if(typestage=="Ouvrier"):
                list_stagiares=request.POST.getlist('stagiaires') 
                if len(list_stagiares)>=1 and len(list_stagiares)<=2:
                    if (duree==timedelta(days=15)):
                        if form.is_valid():
                            form.save()  
                            form=stageform()
                            return redirect("affiche_Stages") # .... redirection vers une autre page
                    else:
                            mssg="veuillez selectionner entre une date qui ne dure pas plus de 15jours ( 2 semaines precise)!"
                            return render(request,"stgform.html",{"form":form,"message":mssg})  
                else:
                    mssg="veuillez selectionner entre 1 et 2 stagiaires!" 
                return render(request,"stgform.html",{"form":form,"message":mssg}) 
            elif(typestage=="Court"):
                    list_stagiares=request.POST.getlist('stagiaires') 
                    if len(list_stagiares)>=1 and len(list_stagiares)<=4 :
                        if(duree>timedelta(days=42) and duree<timedelta(days=56)): 
                            if form.is_valid():
                                form.save()
                                form=stageform()
                                return redirect("affiche_Stages") # .... redirection vers une autre page
                        else:
                            mssg="veuillez selectionner entre une date qui ne dure pas plus de 56 jours et moins de 42 jours ( 6 semaines à 8 semaines max)!"
                            return render(request,"stgform.html",{"form":form,"message":mssg})  
                    else:
                        mssg="veuillez selectionner entre 1 et 4 stagiaires!"
                        return render(request,"stgform.html",{"form":form,"message":mssg})  
            elif(typestage=="PFE"):
                eng=request.POST.get('Enseigant')
                if (eng!=NULL and eng!=''):
                    list_stagiares=request.POST.getlist('stagiaires') 
                    if len(list_stagiares)>=1 and len(list_stagiares)<=2 :
                        if (duree < timedelta(days=367) and duree > timedelta(days=183)): # duree max une année et min 6 mois 
                            if form.is_valid():
                                form.save()  
                                form=stageform() 
                                return redirect("affiche_Stages") # .... redirection vers une autre page
                        else:
                            mssg="veuillez selectionner entre une date qui ne dure pas plus de 367 jours et moins de 183 jours ( 6 mois à 1 ans max)!"
                            return render(request,"stgform.html",{"form":form,"message":mssg}) 
                    else:
                        mssg="veuillez selectionner entre 1 et 2 stagiaires!" 
                else:
                        mssg="veuillez selectionner un Enseigant !" 
                return render(request,"stgform.html",{"form":form,"message":mssg})  
                
            else:
                    mssg="Stage n'existe pas !" 
                    return render(request,"stgform.html",{"form":form,"message":mssg}) 
        else:
                mssg="Date debut inferieur a date fin !" 
                return render(request,"stgform.html",{"form":form,"message":mssg}) 

    else :
        form = stageform(instance=stage)
        form=stageform()

    return render(request,'stgform.html', {"form":form})

def update_enseignant(request,id):
    ensg= Enseignant.objects.get(CodeE=id)
    form = Enseignantform( instance=ensg)
    if request.method=="POST":
        form = Enseignantform(request.POST, instance=ensg)
        num1=request.POST.get('TelE1')
        num2=request.POST.get('TelE2')
        if(len(num1)==10 and (len(num2)==10 or len(num2)==0)):
            if form.is_valid():
                form.save()  
                form=stageform()
                return redirect("affiche_eng")
        else :
            mssg="Numero de telephone erronée !" 
            return render(request,'stgform.html', {"form":form,"message":mssg})
    else :
        form = Enseignantform( instance=ensg)
    return render(request,'stgform.html', {"form":form})

def update_Entreprise( request,id):
    ent= Entreprise.objects.get(id =id)
    form = Entrepriseform(instance=ent)
    if request.method =='POST':
        form =  Entrepriseform(request.POST,instance=ent)
        num1=request.POST.get('NTel1')
        num2=request.POST.get('NTel2')
        if(len(num1)==10 and (len(num2)==10 or len(num2)==0)):
            if form.is_valid():
                form.save()
                form = Entrepriseform()
                return redirect("affiche_ent") 
        else :
            mssg="Numero de telephone erronée !" 
            return render(request,'stgform.html', {"form":form,"message":mssg}) 
    else:
        form=Entrepriseform(instance=ent)
    return render(request,'stgform.html',{"form":form})

def update_Membre_Entreprise( request,id):
    mmbr = Membre_Entreprise.objects.get(CodeM=id)
    form = Enseignantform( instance=mmbr)
    if request.method =='POST':
        form =  Membre_Entrepriseform(request.POST,instance=mmbr)
        num1=request.POST.get('TelP1')
        num2=request.POST.get('TelP2')
        if(len(num1)==10 and (len(num2)==10 or len(num2)==0)):
            if form.is_valid():
                form.save()
                form = Membre_Entrepriseform()
                return redirect("affiche_mmbr")
        else :
            mssg="Numero de telephone erronée !" 
            return render(request,'stgform.html', {"form":form,"message":mssg})
    else:
        form=Membre_Entrepriseform(instance=mmbr)
    return render(request,'stgform.html',{"form":form})

def update_Stagiaire( request,id):
    stg= Stagiaire.objects.get(matricule=id)
    form = Enseignantform( instance=stg)
    if request.method =='POST':
        form =  Stagiaireform(request.POST, instance=stg)
        num1=request.POST.get('Tel1')
        num2=request.POST.get('Tel2')
        if(len(num1)==10 and (len(num2)==10 or len(num2)==0)):
            if form.is_valid():
                form.save()
                form = Stagiaireform()
                return redirect("affiche_stgr")
        else :
            mssg="Numero de telephone erronée !" 
            return render(request,'stgform.html', {"form":form,"message":mssg})
    else:
        form=Stagiaireform(instance=stg)
    return render(request,'stgform.html',{"form":form})

def update_Jury ( request,id):
    j=Jury.objects.get(id=id)
    form = Enseignantform( instance=j)
    if request.method =='POST':
        form = Juryform (request.POST,instance=j)
        if form.is_valid():
            form.save()
            form = Juryform()
            return redirect("affiche_sout")
    else:
        form=Juryform(instance=j)
    return render(request,'stgform.html',{"form":form})

def delete_stage(request,id):
    stage = Stage.objects.get(id=id)
    if request.method=='POST' :
        stage.delete()
        return redirect('/list_stg')
    context= {'item':stage}
    return render (request, 'delete.html',context)
def delete_enseignant (request, id):
    ensg= Enseignant.objects.get(CodeE=id)
    if request.method=='POST' :
        ensg.delete()
        return redirect('/list_eng')
    context = {'item': ensg}
    return render (request, 'delete.html',context)
def delete_Entreprise (request, id):
    ent= Entreprise.objects.get(id=id)
    if request.method=='POST' :
        ent.delete()
        return redirect('/list_entp')
    context = {'item':ent}
    return render (request, 'delete.html',context)
def delete_Membre_Entreprise (request, id):
    mmbr = Membre_Entreprise.objects.get(CodeM=id)
    if request.method=='POST' :
        mmbr.delete()
        return redirect('/list_mmbrentp')
    context = {'item':mmbr}
    return render (request, 'delete.html',context)
def delete_Stagiaire (request, id):
    stg= Stagiaire.objects.get(matricule=id)
    if request.method=='POST' :
        stg.delete()
        return redirect('/list_stagiaire')
    context = {'item': stg}
    return render (request, 'delete.html',context)
def delete_Jury (request, id):
    j=Jury.objects.get(id=id)
    if request.method=='POST' :
        j.delete()
        return redirect('/list_jry')
    context = {'item':j}
    return render (request, 'delete.html',context)

def rechercher(request):
    return render(request,"recherche.html")
def rechercher_stage(request):
    stages=''
    if request.method =='GET':
        query =request.GET.get('recherche')
        if query:
            stages=Stage.objects.filter(Theme__startswith=query)
    return render(request,"views/chercherStage.html",{"stage": stages})
def rechercher_stage_id(request):
    stages=''
    if request.method =='GET':
        query =request.GET.get('recherche')
        if query:
            stages=Stage.objects.filter(id=query)
    return render(request,"views/chercherStage.html",{"stage": stages})
def rechercher_enseignant(request):
    enseignants=''
    if request.method =='GET':
        query =request.GET.get('recherche')
        if query:
            enseignants=Enseignant.objects.filter(NomE__startswith=query)
    return render(request,"views/chercherEncadreur.html",{"ensg": enseignants})
def rechercher_enseignant_id(request):
    enseignants=''
    if request.method =='GET':
        query =request.GET.get('recherche')
        if query:
            enseignants=Enseignant.objects.filter(CodeE=query)
    return render(request,"views/chercherEncadreur.html",{"ensg": enseignants})
def rechercher_Entreprise(request):
    Entreprises=''
    if request.method =='GET':
        query =request.GET.get('recherche')
        if query:
            Entreprises=Entreprise.objects.filter(E_name__startswith=query)
    return render(request,"views/chercherEntreprise.html",{"ent": Entreprises})
def rechercher_Membre_Entreprise(request):
    Membre_Entreprises=''
    if request.method =='GET':
        query =request.GET.get('recherche')
        if query:
            Membre_Entreprises=Membre_Entreprise.objects.filter(NomP__startswith=query)
    return render(request,"views/chercherPromoteur.html",{"mmbr": Membre_Entreprises})
def rechercher_Membre_Entreprise_id(request):
    Membre_Entreprises=''
    if request.method =='GET':
        query =request.GET.get('recherche')
        if query:
            Membre_Entreprises=Membre_Entreprise.objects.filter(CodeM=query)
    return render(request,"views/chercherPromoteur.html",{"mmbr": Membre_Entreprises})
def rechercher_Stagiaire(request):
    Stagiaires=''
    if request.method =='GET':
        query =request.GET.get('recherche')
        if query:
            Stagiaires=Stagiaire.objects.filter(last_name__startswith=query)
    return render(request,"views/chercherStagiaire.html",{"stgr": Stagiaires})
def rechercher_Stagiaire_id(request):
    Stagiaires=''
    if request.method =='GET':
        query =request.GET.get('recherche')
        if query:
            Stagiaires=Stagiaire.objects.filter(matricule=query)
    return render(request,"views/chercherStagiaire.html",{"stgr": Stagiaires})
def rechercher_Jury(request):
    Jurys=''
    if request.method =='GET':
        query =request.GET.get('recherche')
        if query:
            Jurys=Jury.objects.filter(J_name__startswith=query)
    return render(request,"views/chercherSoutenance.html",{"sout": Jurys})




def graphePage(request):
    
    annee = '2022'
    if request.method == "GET":
        data = Stage.objects.filter(Date_Deb__year=annee,type="PFE").values('mmbr_entreprise__entreprise').annotate(nbr_etudiant = Count('id')).order_by()
        classement = Stage.objects.filter(Date_Deb__year=annee).values('mmbr_entreprise__entreprise').annotate(nbr_stagiaires = Count('id')).order_by()
        classement = classement.order_by('-nbr_stagiaires')
        courbe = Stage.objects.filter(type="PFE").values('Date_Deb__year').annotate(nbr_entreprise = Count('mmbr_entreprise__entreprise')).order_by()
        print(courbe)
        context = {
            'data' : data,
            'annee' : annee,
            'classement' : classement,
            'courbe' : courbe
        }
    elif request.method == "POST":
        annee = request.POST['annee']
        data = Stage.objects.filter(Date_Deb__year=annee,type="PFE").values('mmbr_entreprise__entreprise').annotate(nbr_etudiant = Count('id')).order_by()
        classement = Stage.objects.filter(Date_Deb__year=annee).values('mmbr_entreprise__entreprise').annotate(nbr_stagiaires = Count('id')).order_by()
        classement = classement.order_by('-nbr_stagiaires')
        courbe = Stage.objects.filter(type="PFE").values('Date_Deb__year').annotate(nbr_entreprise = Count('mmbr_entreprise__entreprise')).order_by()
        print(courbe)
        
        context = {
            'data' : data,
            'annee' : annee,
            'classement' : classement,
            'courbe' : courbe
        }
    return render(request,"dashboard/ind.html",context)


