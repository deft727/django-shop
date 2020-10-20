from django.contrib import admin
from .models import *
from django.forms import ModelChoiceField
# ,ModelForm,ValidationError
# from PIL import Image
# from django.utils.safestring import mark_safe
# from django import forms


# class ParfumeAdminForm(ModelForm):

#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         self.fields['image'].help_text= mark_safe(
#             """'<span style="color:red;font-size:14px;">изображение будет обрезано до  {}x{}</span>'"""
#             .format(
#             * Product.MAX_RESOLUTION
#             ))
# func check image
    # def clean_image(self):
    #     image=self.cleaned_data['image']
    #     img=Image.open(image)
    #     # print(img.width)
    #     max_width,max_height= Product.MAX_RESOLUTION
    #     min_width,min_height= Product.VALID_RESOLUTION
    #     if img.height < min_height or img.width < min_width:
    #         raise ValidationError('высота или ширина меньше минимального разрешения')
    #     if img.height > max_height or img.width > max_width:
    #         img = img.resize(Product.MAX_RESOLUTION)
    #     return image


class ParfumeAdmin(admin.ModelAdmin):
    # form=ParfumeAdminForm
    change_form_template='admin.html'
    def formfield_for_foreignkey(self,db_field,request,**kwargs):
        if db_field.name=='category':
            return ModelChoiceField(Category.objects.filter(slug='parfumes'))
        return super().formfield_for_foreignkey(db_field,request,**kwargs)
        


class ProbesAdmin(admin.ModelAdmin):
    change_form_template='admin.html'
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
