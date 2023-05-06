from django.db import models

class Hache_vcego(models.Model): # карточка отдыха
    gl = models.CharField(max_length=50, verbose_name='Имя и 2-3 слова ')
    name = models.TextField(verbose_name='полное описаие тура')
    datas = models.CharField( max_length=50, verbose_name='Сколько дней и ночей')
    data = models.DateField( verbose_name='Дата опубликации поста')
    category = models.ForeignKey('Putis',on_delete=models.CASCADE, blank=True, null=True, verbose_name='Где отдыхать?')
    img = models.ImageField(verbose_name='Картинка на главну cтраницу')
    imgs = models.ImageField(verbose_name='Картинка вкладку')
    many = models.CharField( max_length=50, verbose_name='цена в рудлях')
    published = models.BooleanField( default=False, verbose_name='Опубликовать на главную страницу')
    faer_tur = models.BooleanField( default=False, verbose_name='Горящий тур')
    number_of_comments = models.IntegerField(default=0)


    def __str__(self):
        return self.name

class Putis(models.Model): # категории отдыха
    forinkeei = models.TextField(verbose_name='Направления')
    gr = models.BooleanField( default=False, verbose_name='Вывод кнопки на картинку с горящим туром')

    def __str__(self):
        return self.forinkeei


class Krasota(models.Model): #главная картинка при входе на сайт
    name1 = models.TextField(verbose_name='надпись 1')
    name2 = models.TextField(verbose_name='надпись 2')
    img_dva = models.ImageField(verbose_name='Картинка наглавную страницу')

    def __str__(self):
        return self.name1

class News(models.Model): #новости
    nows = models.CharField( max_length=19, verbose_name='Не много буквально до 19 слова')
    now = models.TextField( verbose_name='то + остальное')
    data = models.DateField( verbose_name='Дата опубликации новости')
    img = models.ImageField(verbose_name='Картинка новости')
    published = models.BooleanField(default=False, verbose_name='Опубликовать на главную страницу')

    def __str__(self):
        return self.nows

class Sovetiki(models.Model): #советы
    zagolovok = models.CharField(max_length=25, verbose_name='Заголовок')
    tema_cmoll = models.CharField(max_length=20, verbose_name='Немгого о теме')
    number_licK = models.IntegerField(default=0,verbose_name='количество лайков')
    data = models.DateField(verbose_name='Дата опубликации поста')
    tema_bug = models.TextField( verbose_name='Полное описание')
    published = models.BooleanField(default=False, verbose_name='Опубликовать на главную страницу')

    def __str__(self):
        return self.zagolovok

class Infa(models.Model): # О Але
    mane_situ = models.CharField(max_length=50, verbose_name='Название городе')
    tema_cmoll = models.CharField(max_length=30, verbose_name='2-3 слова о городе(для интриги)')
    img = models.ImageField(verbose_name='Картинка на главну cтраницу')
    #img_1 = models.ImageField(verbose_name='Картинка 1')
    #img_2 = models.ImageField(default=True,verbose_name='Картинка 2')
    #img_3 = models.ImageField(default=True,verbose_name='Картинка 3')
    #img_4 = models.ImageField(default=True,verbose_name='Картинка 4')
    #img_5 = models.ImageField(default=True,verbose_name='Картинка 5')
    #img_6 = models.ImageField(default=True,verbose_name='Картинка 6')
    #img_7 = models.ImageField(default=True,verbose_name='Картинка 7')
    #img_8 = models.ImageField(default=True,verbose_name='Картинка 8')
    #img_9 = models.ImageField(default=True,verbose_name='Картинка 9')
    #img_10 = models.ImageField(default=True,verbose_name='Картинка 10')
    published = models.BooleanField(default=False, verbose_name='Опубликовать на главную страницу к категории о себе')
    tema_bug = models.TextField( verbose_name='Полное описание, где была? Что видела?(потом сядем и напишем вопросы для этого пункта что бы легче было писать)')

    def __str__(self):
        return self.mane_situ

class Nomer(models.Model):         # заголовок c горящими турами
    zagol = models.CharField(max_length=50, verbose_name='заголовок')
    ksia = models.CharField(max_length=50, verbose_name='акция')
    data = models.TextField(verbose_name='Дата огда будут горящие туры(часы на убыване) надо так 2024/05/15(год,месяц,день)')
    faer_tur = models.BooleanField(default=False, verbose_name='опубликовать')

    def __str__(self):
        return self.zagol

class Otziv(models.Model): # отзыв
    name_otziv = models.CharField(max_length=70, verbose_name='имя')
    pothota_otziv = models.CharField(max_length=70, verbose_name='почта ')
    otziv_otziv = models.TextField(verbose_name='что хотят рассказать')
    published = models.BooleanField(default=False, verbose_name='Опубликовать на главную страницу к категории о себе')
    def __str__(self):
        return self.name_otziv

