from django.db import models

# Tuple of 2-tuples
# Canvas Options
SIZES = (
  ('S', 'Small'),
  ('M', 'Medium'),
  ('L', 'Large')
)

MATERIALS = (
  ('Cl', 'Cloth'),
  ('Li', 'Linen')
)

FORMS = (
  ('P', 'Panel'),
  ('R', 'Roll')
)

# Brushes Options
TYPES = (
  ('Ro', 'Round'),
  ('Fl', 'Flat'),
  ('Br', 'Bright'),
  ('Fi', 'Filbert'),
  ('Fa', 'Fan'),
  ('An', 'Angle'),
  ('Mo', 'Mop'),
  ('Ri', 'Rigger')
)

# Create your models here.
class Paintbrush(models.Model):
  type = models.CharField(
    max_length=2,
    choices=TYPES,
    default=TYPES[0][0]
  )
  size = models.IntegerField() 

  def __str__(self):
    return f"{self.get_type_display()}"

class Student(models.Model):
  name= models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  age = models.IntegerField()
  bio = models.TextField(max_length=250)

  # M:M relationship
  paintbrushes = models.ManyToManyField(Paintbrush)

  def __str__(self):
    return self.name
  
  def got_all_sizes(self):
    array_of_sizes = []
    got_small=self.canvas_set.filter(size="S")
    got_medium =self.canvas_set.filter(size="M") 
    got_large =self.canvas_set.filter(size="L") 
    if got_small:
        array_of_sizes.append("Small")
    if got_medium:
        array_of_sizes.append("Medium")
    if got_large:
        array_of_sizes.append("Large")
    print("In the got_all_sizes - printing array_of sizes >>>>", array_of_sizes)
    if len(array_of_sizes) == 3:
        return True
    else:
        return False 

class Canvas(models.Model):
  size = models.CharField(
    max_length=1,
    choices=SIZES,
    default=SIZES[0][0]  
  )
  material = models.CharField(
    max_length=2,
    choices=MATERIALS,
    default=MATERIALS[0][0] 
  )
  form = models.CharField(
    max_length=1,
    choices=FORMS,
    default=FORMS[0][0] 
  )

  student = models.ForeignKey(Student, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_size_display()} {self.get_material_display()} {self.get_form_display()}" 
  
  # changing the default sort
  class Meta:
    ordering = ['-size']





  