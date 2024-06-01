from django.shortcuts import render
from rating.models import Rating
import math
# Create your views here.

def pagination_view(request, *args, **kwargs):
    qs = Rating.objects.all()
    page = int(request.GET.get('page', '1'))
    paginate_by = 5
    max_page = math.ceil(len(qs)/paginate_by)
    index = (page-1)*paginate_by
    #page = max_page if page > max_page else page
    #page = page+1 if page < 1 else page
    if page < 1: 
        start = 0
        end = 5
    elif page > max_page:
        start = (max_page*paginate_by)-5
        end = max_page*paginate_by
    else:
        start = index
        end = index+5
    return render(request, 'pagination_example/pagination_example.html',
                {'page': qs[start:end],
                'next_page': page+1, 'last_page': page-1 })
