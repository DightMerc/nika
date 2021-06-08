from django.shortcuts import render

from django.views import View

from django.core.paginator import Paginator

from core import models

# Create your views here.


class MainView(View):

    def get(self, request):

        news = models.News.objects.all()

        news = Paginator(news, 2)

        pets = models.Pet.objects.all()
        pets = pets[:3]

        return render(request, 'core/index.html',
        {
            'news': news.page(1),
            'pets': pets
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

        