from django.shortcuts import render

from django.views import View

from django.core.paginator import Paginator

from core import models
import logging
from django.db.models import Q

logger = logging.getLogger(__name__)

# Create your views here.


class MainView(View):

    def get(self, request):

        current_pet_type = request.GET.get('pet', 'Собаки')

        news = models.News.objects.all()

        pet_types = models.PetType.objects.filter(~Q(title=current_pet_type))

        news = Paginator(news, 2)

        pets = models.Pet.objects.filter(pet_type__title=current_pet_type)
        pets = pets[:3]

        return render(request, 'core/index.html',
        {
            'news': news.page(1),
            'pets': pets,
            'pet_types': pet_types,
            'current_pet_type': current_pet_type
        })


class ContactView(View):

    def get(self, request):

        return render(request, 'core/contacts.html')


class AboutView(View):

    def get(self, request):

        return render(request, 'core/about.html')


class NewsView(View):

    def get(self, request):

        news = models.News.objects.all()

        news = Paginator(news, 5)

        try:
            recent = news.page(2)
        except Exception as e:
            recent = news.page(1)

        return render(request, 'core/news.html',
        {
            'news': news.page(1),
            'recent': recent
        })


class ArticleView(View):

    def get(self, request, id):

        article = models.News.objects.get(id=id)

        news = models.News.objects.all()

        news = Paginator(news, 5)

        try:
            recent = news.page(2)
        except Exception as e:
            recent = news.page(1)

        return render(request, 'core/article.html',
        {
            'article': article,
            'recent': recent

        })

        