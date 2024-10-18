from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.contrib import messages




# Create your views here.
def article_list(request):
    category = request.GET.get('category')
    if category:
        articles = Article.objects.filter(category=category)
    else:
        articles = Article.objects.all()
    return render(request, 'tips/article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'tips/article_detail.html', {'article': article})



@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'tips/add_article.html', {'form': form})



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ArticleForm
from .models import Article

@login_required
def my_articles(request):
    articles = Article.objects.filter(author=request.user)
    return render(request, 'tips/my_articles.html', {'articles': articles})

@login_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id, author=request.user)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article updated successfully.')
            return redirect('my_articles')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'tips/edit_article.html', {'form': form})

@login_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id, author=request.user)
    if request.method == 'POST':
        article.delete()
        messages.success(request, 'Article deleted successfully.')
        return redirect('my_articles')
    return render(request, 'tips/delete_article_confirm.html', {'article': article})
