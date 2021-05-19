from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):

    template = 'catalog.html'
    order = request.GET.get('order', 'name')
    # print(order)
    content = Phone.objects.all().order_by(order)
    descending = request.GET.get('descending', False)
    # print(content)
    if descending == 'True':
        content = content.reverse()
        print(content)
    # print(content)
    context = {'phones': content}

    return render(request, template, context)


def show_product(request, slug):
    print(slug)
    template = 'product.html'
    product = Phone.objects.all().get(slug=slug)
    context = {'phone': product}
    return render(request, template, context)
