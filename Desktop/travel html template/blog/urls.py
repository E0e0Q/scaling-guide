from django.urls import path
from blog.views import baza,osnova,podrobno,categoryes,all_tur,MY,help,news_NEW,сoment_new

urlpatterns = [
    path('', baza, name='baza'),
    path('post/osnova', osnova, name='osnova'),
    path('post/MY', MY, name='MY'),
    path('post/news_NEW', news_NEW, name='news_NEW'),
    path('post/help', help, name='help'),
    path('post/сoment_new', сoment_new, name='сoment_new'),
    path('post/all_tur', all_tur, name='all_tur'),
    path('post/categoryes/<int:category_pk>', categoryes, name='categoryes'),
    path('post/podrobno/ <int:i_pk>', podrobno, name='podrobno'),
]