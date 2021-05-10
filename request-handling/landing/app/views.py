from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    from_landing = request.GET.get('from-landing')
    if from_landing == 'original':
        counter_click['original'] += 1
    elif from_landing == 'test':
        counter_click['test'] += 1
    return render(request, 'index.html')


def landing(request):
    ab_test_arg = request.GET.get('ab_test_arg')
    landing_html = 'landing.html'
    if ab_test_arg == 'original':
        counter_show['original'] += 1
    elif ab_test_arg == 'test':
        counter_show['test'] += 1
        landing_html = 'landing_alternate.html'
    return render(request, landing_html)


def stats(request):
    test_conversion = counter_click['test'] / counter_show['test']
    original_conversion = counter_click['original'] / counter_show['original']
    return render(request, 'stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
