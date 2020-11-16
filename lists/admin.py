from django.contrib import admin

# Register your models here.
@admin.register(models.Lists)
class ListsAdmin(admin.ModelAdmin):
    pass