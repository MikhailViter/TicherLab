from django.shortcuts import render,redirect
from .models import Artiсles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView,DeleteView

def news_home(request):
    news = Artiсles.objects.order_by('-date')
    return render(request,'news/news_home.html',{'news': news})


class NewsDetailView(DetailView):
    model = Artiсles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
        model = Artiсles
        template_name = 'news/create.html'

        fields = ['title', 'anons', 'full_text', 'date']

class NewsDeleteView(DeleteView):
        model = Artiсles
        success_url = '/news/'
        template_name = 'news/news_delete.html'

        fields = ['title', 'anons', 'full_text', 'date']


def create (request):
    error = ""
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "Форма не верна"

    form = ArticlesForm()
    date = {
        'form': form,
        'error': error

    }
    return render(request, 'news/create.html', date)
# указывем словарь после путя