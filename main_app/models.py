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

        
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)


class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        # this will help us make a select menu when a form is created from this model
        choices=MEALS,
        default=MEALS[0][0])

    # create a cat_id FK (Cat is our model)
    # <- If you delete cat, delete all the feeding associated with the cat as well
    goodboiz = models.ForeignKey(Goodboiz, on_delete=models.CASCADE)

    def __str__(self):
        # get_meal_display() is a method django creates for  Charfields that have choices (Select menu)
        # get_<property name>_display() -> automatically shows the humnan readable value, so if meal's value is "B", the method
        # will return Breakfast, (look at the tuple!)
        return f"{self.get_meal_display()} on {self.date}"
