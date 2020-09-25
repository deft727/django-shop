from django.contrib import admin
from . models import *
from django import forms
from django.forms import ModelChoiceField



class ParfumeAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self,db_field,request,**kwargs):
        if db_field.name=='category':
            return ModelChoiceField(Category.objects.filter(slug='parfumes'))
        return super().formfield_for_foreignkey(db_field,request,**kwargs)
        


class ProbesAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self,db_field,request,**kwargs):
        if db_field.name=='category':
            return ModelChoiceField(Category.objects.filter(slug='probes'))
        return super().formfield_for_foreignkey(db_field,request,**kwargs)



admin.site.register(Category)
admin.site.register(Pafume,ParfumeAdmin)
admin.site.register(Probes,ProbesAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
