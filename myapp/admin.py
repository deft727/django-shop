from django.contrib import admin
from . models import *
from django import forms
from django.forms import ModelChoiceField,ModelForm,ValidationError
from PIL import Image

class ParfumeAdminForm(ModelForm):
    VALID_RESOLUTION=(400,400)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['image'].help_text= 'Загружайте изображения с минимальны разрешением {}x{}'.format(
            *self.VALID_RESOLUTION
            )

    def clean_image(self):
        image=self.cleaned_data['image']
        img=Image.open(image)
        # print(img.width)
        min_width,min_height=self.VALID_RESOLUTION
        if img.height < min_height or img.width < min_width:
            raise ValidationError('высота или ширина меньше минимального разрешения')
        return image


class ParfumeAdmin(admin.ModelAdmin):
    form=ParfumeAdminForm
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
