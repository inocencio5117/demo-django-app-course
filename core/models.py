from django.db import models
from stdimage.models import StdImageField

# Signals
from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    created_at = models.DateField('Creation date', auto_now_add=True)
    updated_at = models.DateField('Updated date', auto_now=True)
    active = models.BooleanField('Active?', default=True)

    class Meta:
        abstract = True
    

class Product(Base):
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('Price', max_digits=8, decimal_places=2)
    qty = models.IntegerField('Quantity')
    image = StdImageField('Image', upload_to='products', variations={'thumb': (124, 124)}) # type: ignore
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.name

def product_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)

signals.pre_save.connect(product_pre_save, sender=Product)
