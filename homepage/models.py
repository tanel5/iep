from django.db import models
from django.forms import ModelForm, Select
from django.forms import TextInput

# Create your models here.
from prompt_toolkit.widgets import TextArea


class Lead(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    code_postal = models.CharField(max_length=5)
    email = models.EmailField(max_length=254)
    tel = models.CharField(max_length=10)
    date_creation = models.DateField(auto_now_add=True)
    sold = models.BooleanField(default=False)
    a = 'entre 10h et 12h'
    b = 'entre 12h et 14h'
    c = 'entre 14h et 16h'
    d = 'entre 16h et 18h'
    e = 'entre 18h et 20h'
    TRANCHE_HORAIRES = [
        (a, 'entre 10h et 12h'),
        (b, 'entre 12h et 14h'),
        (c, 'entre 14h et 16h'),
        (d, 'entre 16h et 18h'),
        (e, 'entre 18h et 20h')
    ]
    tranche_horaire = models.CharField(max_length=200, choices=TRANCHE_HORAIRES, default=None)
    """g = 'garage'
    s = 'caves et sous-sol'
    c = 'combles'
    v = 'vide sanitaires'
    a = 'autre'
    TYPE_DE_SURFACE_CHOICES = [
        (g, 'garage annexe'),
        (s, 'cave et sous-sol'),
        (c, 'combles'),
        (v, 'vide sanitaire'),
        (a, 'autre')
    ]
    type_de_surface = models.CharField(max_length=200, choices=TYPE_DE_SURFACE_CHOICES, default=None)
    A = '0 à 50m2'
    B = '50 à 100m2'
    C = '100 à 150m2'
    D = '150 à 200m2'
    E = '200m2 et plus'
    SURFACES_APPROXIMATIVES_CHOICES = [
        (A, '0 à 50m2'),
        (B, '50 à 100m2'),
        (C, '100 à 150m2'),
        (D, '150 à 200m2'),
        (E, '200m2 et plus'),
    ]
    surface_approximative = models.CharField(max_length=200, choices=SURFACES_APPROXIMATIVES_CHOICES, default=None)
    El = 'electricité'
    Fi = 'fioul'
    Ga = 'gaz'
    Po = 'pompe à chaleur'
    Au = 'autre'
    CHAUFFAGE_CHOICES = [
        (El, 'electricité'),
        (Fi, 'Fioul'),
        (Ga, 'Gaz'),
        (Po, 'Pompe à chaleur'),
        (Au,'Autre'),
    ]
    chauffage = models.CharField(max_length=200, choices=CHAUFFAGE_CHOICES, default=None)"""

    def __str__(self):
        return self.nom + " " + self.prenom


class LeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = ['nom', 'prenom', 'code_postal', 'email', 'tel', 'tranche_horaire']
        widgets = {
            'nom': TextInput(attrs={'placeholder': 'Votre nom', 'size': 30}),
            'prenom': TextInput(attrs={'placeholder': 'Votre prénom', 'size': 30}),
            'code_postal': TextInput(attrs={'placeholder': 'Votre code postal', 'size': 30}),
            'email': TextInput(attrs={'placeholder': 'votre adresse email', 'size': 30}),
            'tel': TextInput(attrs={'placeholder': 'votre numéro de téléphone', 'size': 30}),
            'tranche_horaire': Select(attrs={'placeholder': 'à quel heure êtes vous disponible?', 'size': 1}),
        }
