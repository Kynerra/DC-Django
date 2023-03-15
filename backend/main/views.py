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
        response = list( set( list(Anime.objects.filter( title__icontains=request.GET.get('query'))) + list(Anime.objects.filter(about__icontains=request.GET.get('query'))) ) )

        context = {
            "top__views": list( Anime.objects.order_by('-views') )[:5],
            "new__comment": { Anime.objects.get(id=x.for_anime.id) for x in Comment.objects.order_by('-date') },
            "response": response[ ((page-1) * 12) : ((page) * 12)],
            "pages": ( page, list( range( 1, (len(response) // 12 + 2 )) ), len( response ) // 12 + 1 ),
            "query": request.GET.get('query')
        }

        return render(
            request=request,
            template_name='search.html',
            context=context
        )
    
    else:
        return redirect('index_url')


def trending_all_view(request, page):
    response = list( Anime.objects.order_by('-views', '-comments') )

    context = {
        "top__views": list(Anime.objects.order_by('-views'))[:5],
        "new__comment": {Anime.objects.get(id=x.for_anime.id) for x in Comment.objects.order_by('-date')},
        "trending__products": response[((page - 1) * 12): ((page) * 12)],
        "pages": (page, list(range(1, (len(response) // 12 + 2))), len(response) // 12 + 1),
    }

    return render(
        request=request,
        template_name='trending.html',
        context=context
    )

def recent_all_view(request, page):
    response = list( Anime.objects.order_by('-date') )

    context = {
        "top__views": list(Anime.objects.order_by('-views'))[:5],
        "new__comment": {Anime.objects.get(id=x.for_anime.id) for x in Comment.objects.order_by('-date')},
        "recent__products": response[((page - 1) * 12): ((page) * 12)],
        "pages": (page, list(range(1, (len(response) // 12 + 2))), len(response) // 12 + 1),
    }

    return render(
        request=request,
        template_name='recently_added.html',
        context=context
    )


def anime_detail_view(request, id) -> render:
    context = {
        "anime": Anime.objects.get( id=id ),
        "comments": Comment.objects.filter( for_anime_id = id ),
        "episodes": Episode.objects.filter( for_anime_id = id )
    }

    return  render(
        request=request,
        template_name='anime-details.html',
        context=context
    )

def anime_watching_view(request, id, ep) -> render:
    context = {
        "anime": Anime.objects.get( id=id ),
        "comments": Comment.objects.filter( for_anime_id = id ),
        "episodes": Episode.objects.filter( for_anime_id = id ),
        "this_ep": Episode.objects.filter( for_anime_id = id ).get( number = ep )
    }

    return render(
        request=request,
        template_name='anime-watching.html',
        context=context
    )


def trending_all_nopage_view(request):
    return redirect('trending_all_url', 1)

def recent_all_nopage_view(request):
    return redirect('recent_all_url', 1)