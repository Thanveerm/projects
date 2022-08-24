from django.contrib import admin
from.models import Inerg
from import_export.admin import ImportExportModelAdmin




class InergAdmin(ImportExportModelAdmin):
    list_display=("API_WELL_NUMBER","PRODUCTION_YEAR","QUARTER","OWNER_NAME","COUNTRY","TOWNSHIP","WELL_NAME","WELL_NUMBER","GAS","BRINE")
    pass


admin.site.register(Inerg, InergAdmin)