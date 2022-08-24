from django.forms import models
from import_export import resources
from app.models import Inerg

class InergResources(resources.ModelResource):
    class Meta:
        model=Inerg