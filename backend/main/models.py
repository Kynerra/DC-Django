from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=225)


    def __str__(self) -> str:
        return self.name


class Anime(models.Model):
    title = models.CharField('Title', max_length=225)
    about = models.TextField('About')
    release_date = models.DateField('Release Date', blank=True, null=True)
    image = models.ImageField('Image', upload_to='anime/images/')
    carousel = models.ImageField('Image for carousel', upload_to='anime/carousel/')
    date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField('Views', default=0, auto_created=True)
    categories = models.ManyToManyField(Category, blank=True)
    anime_type = models.IntegerField('Anime Type', choices=[ (0, 'anime'), (1, 'series') ])
    studio = models.CharField('Studio', max_length=225)
    duration = models.IntegerField('Duration')
    video = models.FileField('Video', upload_to='anime/videos/', blank=True, null=True)
    comments = models.IntegerField('Comments', default=0, auto_created=True)


    def __str__(self) -> str:
        return self.title


class Episode(models.Model):
    title = models.CharField(max_length=225, blank=True, null=True)
    for_anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    video = models.FileField('Video', upload_to='anime/videos/')
    number = models.IntegerField('Number', unique=True)


class Comment(models.Model):
    text = models.TextField('Comment')
    date = models.DateTimeField('Comment Date', auto_now_add=True)
    for_anime = models.ForeignKey(Anime, on_delete=models.CASCADE)