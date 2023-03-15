from django.contrib import admin
from .models import ( Anime,
                      Category,
                      Comment,
                      Episode)


admin.site.register(Anime)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Episode)