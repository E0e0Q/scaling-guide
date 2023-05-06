# Generated by Django 4.1.7 on 2023-04-27 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Infa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mane_situ', models.CharField(max_length=50, verbose_name='Название городе')),
                ('tema_cmoll', models.CharField(max_length=30, verbose_name='2-3 слова о городе(для интриги)')),
                ('img', models.ImageField(upload_to='', verbose_name='Картинка на главну cтраницу')),
                ('published', models.BooleanField(default=False, verbose_name='Опубликовать на главную страницу к категории о себе')),
                ('tema_bug', models.TextField(verbose_name='Полное описание, где была? Что видела?(потом сядем и напишем вопросы для этого пункта что бы легче было писать)')),
            ],
        ),
        migrations.CreateModel(
            name='Kak_ehat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lokati', models.TextField(verbose_name='Направление')),
                ('img_lokati', models.ImageField(upload_to='', verbose_name='Картинка')),
            ],
        ),
        migrations.CreateModel(
            name='Krasota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.TextField(verbose_name='надпись 1 слайд 1')),
                ('nam1', models.TextField(verbose_name='надпись 2 слайд 1')),
                ('name2', models.TextField(verbose_name='надпись 1 слайд 2')),
                ('nam2', models.TextField(verbose_name='надпись 2 слайд 2')),
                ('img_one', models.ImageField(upload_to='', verbose_name='Картинка наглавную страницу 1')),
                ('img_dva', models.ImageField(upload_to='', verbose_name='Картинка наглавную страницу 2')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nows', models.CharField(max_length=19, verbose_name='Не много буквально до 10 слова')),
                ('now', models.TextField(verbose_name='то + остальное')),
                ('data', models.DateField(verbose_name='Дата опубликации новости')),
                ('img', models.ImageField(upload_to='', verbose_name='Картинка новости')),
                ('published', models.BooleanField(default=False, verbose_name='Опубликовать на главную страницу')),
            ],
        ),
        migrations.CreateModel(
            name='Nomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zagol', models.CharField(max_length=50, verbose_name='заголовок')),
                ('ksia', models.CharField(max_length=50, verbose_name='акция')),
                ('data', models.TextField(verbose_name='Дата огда будут горящие туры(часы на убыване) надо так 2024/05/15(год,месяц,день)')),
                ('img', models.ImageField(upload_to='', verbose_name='Картинка на фон горщих туров (желательно в хорошем качыестве и широкую)')),
                ('faer_tur', models.BooleanField(default=False, verbose_name='опубликовать')),
            ],
        ),
        migrations.CreateModel(
            name='Otziv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_otziv', models.CharField(max_length=70, verbose_name='имя')),
                ('pothota_otziv', models.CharField(max_length=70, verbose_name='почта ')),
                ('otziv_otziv', models.TextField(verbose_name='что хотят рассказать')),
                ('published', models.BooleanField(default=False, verbose_name='Опубликовать на главную страницу к категории о себе')),
            ],
        ),
        migrations.CreateModel(
            name='Putis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forinkeei', models.TextField(verbose_name='Направления')),
                ('gr', models.BooleanField(default=False, verbose_name='Вывод кнопки на картинку с горящим туром')),
            ],
        ),
        migrations.CreateModel(
            name='Sovetiki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zagolovok', models.CharField(max_length=25, verbose_name='Заголовок')),
                ('tema_cmoll', models.CharField(max_length=20, verbose_name='Немгого о теме')),
                ('number_licK', models.IntegerField(default=0, verbose_name='количество лайков')),
                ('data', models.DateField(verbose_name='Дата опубликации поста')),
                ('tema_bug', models.TextField(verbose_name='Полное описание')),
                ('published', models.BooleanField(default=False, verbose_name='Опубликовать на главную страницу')),
            ],
        ),
        migrations.CreateModel(
            name='Hache_vcego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gl', models.CharField(max_length=50, verbose_name='Имя и 2-3 слова ')),
                ('name', models.TextField(verbose_name='полное описаие тура')),
                ('datas', models.CharField(max_length=50, verbose_name='Сколько дней и ночей')),
                ('data', models.DateField(verbose_name='Дата опубликации поста')),
                ('img', models.ImageField(upload_to='', verbose_name='Картинка на главну cтраницу')),
                ('imgs', models.ImageField(upload_to='', verbose_name='Картинка вкладку')),
                ('many', models.CharField(max_length=50, verbose_name='цена в рудлях')),
                ('published', models.BooleanField(default=False, verbose_name='Опубликовать на главную страницу')),
                ('faer_tur', models.BooleanField(default=False, verbose_name='Горящий тур')),
                ('number_of_comments', models.IntegerField(default=0)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.putis', verbose_name='Где отдыхать?')),
            ],
        ),
    ]