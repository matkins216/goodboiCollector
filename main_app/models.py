from django.db import models
from django.urls import reverse

# Create your models here.


# Note that parens are optional if not inheriting from another class
class Goodboiz(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()


    def get_absolute_url(self):
    # first argument is a name of a url (looks at kwargs in urls.py)
    # self.id is referring to the id of the cat you just
    # created and or updated
        return reverse('detail', kwargs={'gb_id': self.id})
