from django.shortcuts import render
from .models import Page

# Create your views here.


def index(request, pagename):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    page_list = Page.objects.all()
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': page_list,
    }
    # assert False
    return render(request, "pages/page.html", context)
