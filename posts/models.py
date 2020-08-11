""" django """
from django.db import models

""" utilities """
  
class User(models.Model):
    """ User Model """
    email       = models.EmailField(unique=True, default="email@domain.com")
    password    = models.CharField(max_length=25)
    
    first_name  = models.CharField(max_length=25)
    last_name   = models.CharField(max_length=25)

    city        = models.CharField(max_length=25, blank=True)
    country     = models.CharField(max_length=25, blank=True)

    is_admin    = models.BooleanField(default=False)

    bio         = models.TextField(blank=True)

    birthday    = models.DateField(blank=True, null=True)
    created     = models.DateTimeField(auto_now_add=True)         
    modified    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


""" Poblating BD 
data = [
{
"email" : "cadasmeq@gmail.com",
"password" : "somepassword",
"first_name" : "cristopher",
"last_name": "adasme",
"city": "santiago",
"country" : "chile",
"bio" : "Aficionado a la python",
"birthday" : datetime.date(1993, 5, 4),
},
{
"email" : "boot@fake.cl",
"password" : "topsecret_2",
"first_name" : "Don",
"last_name" : "Bot",
"city" : "valparaiso",
"country" : "chile",
"bio" : "Im a Bot",
"birthday" : datetime.date(2000, 1, 1),
},
{
"email" : "test@platzi.cl",
"password" : "topsecret_1",
"first_name" : "juanito",
"last_name" : "test",
"city" : "santiago",
"country" : "chile",
"bio" : "Im a tester",
"is_admin" : True,
},
{
"email" : "anonymous@gmail.com",
"password" : "topsecret_3",
"first_name" : "anony",
"last_name" : "mous",
"city" : "fake",
"country" : "chile",
"is_admin" : True,
}

]

for d in data:
    user = User.objects.create(**d)

1. Convert anonymous and fake emails into @fake.cl
2. Convert test and cadasmeq into admins.

fake = User.objects.filter(email="boot@fake.cl").update(email="fake_account@fake.cl", is_admin=0)
anonymous = User.objects.filter(email="anonymous@gmail.com").update(email="fake_account2@fake.cl", is_admin=0)

platzi = User.objects.filter(email__endswith="@platzi.cl").update(is_admin=1)
admin = User.objects.filter(email="cadasmeq@gmail.com").update(is_admin=1)

"""