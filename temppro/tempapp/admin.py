from django.contrib import admin
from .models import student,mointer
# Register your models here.
class studentAdmin(admin.ModelAdmin):
    pass
admin.site.register(student, studentAdmin)

class mointerAdmin(admin.ModelAdmin):
    pass
admin.site.register(mointer, mointerAdmin)