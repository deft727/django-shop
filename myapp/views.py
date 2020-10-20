from django.shortcuts import render
from django.views.generic import DetailView
from .models import Pafume,Probes,Category
# Create your views here.


def test_view(request):
    categories=Category.objects.get_categories_for_left_sidebar()
    return render(request,'index.html',{'categories':categories})

class ProductDetailView(DetailView):
    CT_MODEL_MODEL_CLASS={
        'parfume': Pafume,
        'probes': Probes
    }
    def dispatch(self,request,*args,**kwargs):
        self.model=self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset=self.model._base_manager.all()
        return super().dispatch(request,*args,**kwargs)

    # model=Model
    # queryset=Model.object.all()
    context_object_name='product'
    template_name='product_detail.html'
    slug_url_kwarg= 'slug'

class CategotyDetailView(DetailView):
    model= Category
    queryset= Category.objects.all()
    context_object_name='category'
    template_name= 'category_detail.html'
    slug_url_kwarg= 'slug'
