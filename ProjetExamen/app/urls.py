from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns=[
    path ('home', views.go_home,name="home"),
    #------------- creation des données dans la BD--------
    path('stage/add/',views.ajouter_stage,name='ajout_stage'),
    path('esng/add/',views.ajouter_enseignant,name='ajout_eng'),
    path('entp/add/',views.ajouter_Entreprise,name='ajout_ent'),
    path('mmbrentp/add/',views.ajouter_Membre_Entreprise,name='ajout_mmbr'),
    path('stagiaire/add/',views.ajouter_Stagiaire,name='ajout_stgr'),
    path('jry/add/',views.ajouter_Jury,name='ajout_sout'),

    #----------- affichages des données -----------------
    path('list_eng',views.afficheEnseignants,name='affiche_eng'),
    path('list_entp',views.affiche_Entreprises,name='affiche_ent'),
    path('list_mmbrentp',views.affiche_Membre_Entreprises,name='affiche_mmbr'),
    path('list_stg',views.affiche_Stages,name="affiche_Stages"),
    path('list_stagiaire',views.affiche_Stagiaires,name='affiche_stgr'),
    path('list_jry',views.affiche_Jurys,name='affiche_sout'),

    #----------- Update ---------------------------------
    path('stg/<int:id>',views.update_Stage,name="update_Stage"),
    path('esng/<int:id>/',views.update_enseignant,name="update_eng"),
    path('entp/<int:id>/',views.update_Entreprise,name="update_entr"),
    path('mmbrentp/<int:id>/',views.update_Membre_Entreprise,name="update_mmbrentr"),
    path('stagiaire/<int:id>/',views.update_Stagiaire,name="update_Stagiaire"),
    path('jry/<int:id>/',views.update_Jury,name="update_Jury"),
    #----------- recherche des données -----------------
    path('stage/search/',views.rechercher_stage,name='rechercher_stage'),
    path('esng/search/',views.rechercher_enseignant,name='rechercher_enseignant'),
    path('entp/search/',views.rechercher_Entreprise,name='rechercher_Entreprise'),
    path('mmbrentp/search/',views.rechercher_Membre_Entreprise,name='rechercher_Membre_Entreprise'),
    path('stagiaire/search/',views.rechercher_Stagiaire,name='rechercher_Stagiaire'),
    path('jry/search',views.rechercher_Jury,name='rechercher_Jury'),
    #----------- recherche avec id -------------------------
    path('search',views.rechercher,name='rechercher'),
    path('stage/id_search/',views.rechercher_stage_id,name='rechercher_stage_id'),
    path('esng/id_search/',views.rechercher_enseignant_id,name='rechercher_enseignant_id'),
    path('mmbrentp/id_search/',views.rechercher_Membre_Entreprise_id,name='rechercher_Membre_Entreprise_id'),
    path('stagiaire/id_search/',views.rechercher_Stagiaire_id,name='rechercher_Stagiaire_id'),
    #------------ Delete ----------------------------------------
    path('stg/delete/<int:id>',views.delete_stage,name='delete_stage'),
    path('esng/delete/<str:id>',views.delete_enseignant,name='delete_enseignant'),
    path('entp/delete/<int:id>',views.delete_Entreprise,name='delete_Entreprise'),
    path('mmbrentp/delete/<str:id>',views.delete_Membre_Entreprise,name='delete_Membre_Entreprise'),
    path('stagiaire/delete/<str:id>',views.delete_Stagiaire,name='delete_Stagiaire'),
    path('jry/delete/<int:id>',views.delete_Jury,name='delete_Jury'),
     #---------statistics-----------------------------------------
    path('graphePage',views.graphePage,name='graphePage'),
] + static (settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()