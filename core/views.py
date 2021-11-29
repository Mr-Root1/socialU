from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class HomeView(View):
    def get(self, request, *args, **kwargs):
        
        contexto={

        }
        return render(request, 'pages/index.html', contexto)