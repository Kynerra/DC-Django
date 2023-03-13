from django.shortcuts import render, redirect
from .models import ( Anime,
                      Category,
                      Comment,
                      Episode)


def index_view(request) -> render:
    context = {
        "carousel": list( Anime.objects.order_by('-date') )[:10],
        "trending__product": list( Anime.objects.order_by('-views', '-comments') )[:9], 
        "recent__product": list( Anime.objects.order_by('-date') )[:9],
        "top__views": list( Anime.objects.order_by('-views') )[:5],
        "new__comment": { Anime.objects.get(id=x.for_anime.id) for x in Comment.objects.order_by('-date') }
    }


    return render(
        request=request,
        template_name='index.html',
        context=context
    )


def search_view(request, page) -> render:
    if request.GET.get('query'):
        response = list(Anime.objects.filter( title__icontains=request.GET.get('query'))) + list(Anime.objects.filter(about__icontains=request.GET.get('query')))

        context = {
            "top__views": list( Anime.objects.order_by('-views') )[:5],
            "new__comment": { Anime.objects.get(id=x.for_anime.id) for x in Comment.objects.order_by('-date') },
            "response": response[ ((page-1)*12+1) : ((page)*12+1)],
            "pages": ( page, list( range( 1, (len(response)//12+1 )) ), len( response )//12 +1 ),
            "query": request.GET.get('query')
        }
        
        return render(
            request=request,
            template_name='search.html',
            context=context
        )
    else:
        return redirect('index_url')


def anime_detail_view(request, id) -> render:
    pass