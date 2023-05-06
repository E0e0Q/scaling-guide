from django.shortcuts import render, redirect
from blog.models import Hache_vcego, Krasota, Putis, News, Sovetiki, Infa, Nomer,Otziv
from blog.forms import PostForm


def osnova(request):        # пустая основа с чего начинал
    return render(request, 'blog/index.html')

# индивидульно каждый пост открывался
def podrobno(request,i_pk):
    posts = Hache_vcego.objects.get(pk=i_pk)    # индивидульно каждый пост открывался
    pos = Hache_vcego.objects.all().filter(pk=i_pk)   # индивидульно каждый пост
    po = Hache_vcego.objects.all()
    return render(request, 'blog/podrobno.html', {'posts': posts,'pos': pos,'po':po})


# раблта с главной страницей

def baza(request):
    posts = Hache_vcego.objects.all().filter(published=True,faer_tur=False)        # только тру опубликовны
    gor_tur = Hache_vcego.objects.all().filter(published=True, faer_tur=True)        # только 2 тру опубликовны в горящие туры
    po = Krasota.objects.all()                        # красота на странице
    category = Putis.objects.all()                    # Вывод категорий на гл.стр
    categor = Putis.objects.filter(gr=True)         # Вывод категории на "горящиц тур"
    news = News.objects.all().filter(published=True)            # новости
    sovet = Sovetiki.objects.all().filter(published=True)          # cоветы
    o_sebe = Infa.objects.all().filter(published=True)             # О Але
    my = Nomer.objects.all().filter(faer_tur=True)         # Оформление горящих туров
    Otziv_Q = Otziv.objects.all().filter(published=True)
    return render(request, 'blog/baza.html',{'posts':posts,'po':po,'category':category,'news':news,'gor_tur':gor_tur,'sovet':sovet,'o_sebe':o_sebe,'categor':categor,'my':my,'Otziv_Q':Otziv_Q})

def categoryes(request,category_pk):
    posts = Hache_vcego.objects.all().filter(category=category_pk)
    category = Putis.objects.all()
    return render(request, 'blog/categoryes.html', {'posts': posts,
                                                   'category': category})

def all_tur(request):   #все туры
    po = Hache_vcego.objects.all()
    category = Putis.objects.all()
    gor_tur = Hache_vcego.objects.all().filter(published=True, faer_tur=True)
    return render(request, 'blog/all_tur.html',{'po':po,'category': category,'gor_tur':gor_tur})

def help(request):      # помощь/подсказки
    help_er = Sovetiki.objects.all().filter(published=True)
    help_e = Sovetiki.objects.all()
    return render(request, 'blog/help.html',{'help_er': help_er,'help_e':help_e})

def MY(request):        # о Але
    my = Infa.objects.all()
    return render(request, 'blog/MY.html',{'my': my})


def news_NEW(request):      # новости
    news_q = News.objects.all()
    return render(request, 'blog/news_NEW.html',{'news_q': news_q})

def сoment_new(request):      # коментарии
    if request.method == 'GET':
        form = PostForm
        return render(request, 'blog/сoment_new.html',{'form':form})
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('baza')

def сoment_n(request):      # новости
    Otziv_Q = Otziv.objects.all()
    return render(request, 'blog/сoment_new.html',{'Otziv_Q': Otziv_Q})


# 4) РАБОТАЛ ФИЛЬТР
# 5) верстка доп HTML
# 1) КАЕГОРИИ НОРМАЛЬНО ОТОБРАЖАЛИСЬ
# 1) нормальное отображения на телефонах
