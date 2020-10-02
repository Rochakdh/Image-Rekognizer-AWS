from django.shortcuts import render
from django.views.generic import TemplateView,View,CreateView
from .forms import ImageForm
from .models import Image
from django.urls import reverse_lazy
# Create your views here.


# class Index(TemplateView):
#     template_name = 'rekon/index.html'
#     form_class = ImageForm
#     # extra_context = Image.objects.latest('image')
#
    # def get_context_data(self, **kwargs):
    #     print("---------------->>>>>>>>>>")
    #     context = super(Index, self).get_context_data(**kwargs)
    #     context['pic'] = Image.objects.latest('image')
    #     return context



class GetImage(CreateView):
    model = Image
    template_name = 'rekon/index.html'
    success_url = reverse_lazy('rekon:index')
    form_class = ImageForm

    def get_context_data(self, **kwargs):
        print("---------------->>>>>>>>>>")
        context = super(GetImage, self).get_context_data(**kwargs)
        context['pic'] = Image.objects.latest('id')
        return context
