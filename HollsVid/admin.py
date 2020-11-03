from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Holl)
class coustomHoll(admin.ModelAdmin):
    pass

@admin.register(models.video)
class coustomVideo(admin.ModelAdmin):
    pass