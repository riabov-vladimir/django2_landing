from collections import Counter
from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
from app.counter import counter_show, counter_click


def index(request):

    if request.GET.get('from-landing') == 'test':
        counter_click['test'] += 1
    elif request.GET.get('from-landing') == 'original':
        counter_click['original'] += 1
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    return render_to_response('index.html')


def landing(request):
    counter_show['original'] += 1
    print(counter_show['original'])
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    return render_to_response('landing.html')


def landing_alter(request):
    counter_show['test'] += 1
    print(counter_show['test'])
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    return render_to_response('landing_alternate.html')


def stats(request):
    if counter_show['test'] > 0:
        test_conversion = (counter_click.get('test') / counter_show['test'])
    else:
        test_conversion = 'страница не была просмотрена ни разу'

    if counter_show['original'] > 0:
        original_conversion = (counter_click['original'] / counter_show['original'])
    else:
        original_conversion = 'страница не была просмотрена ни разу'
    print(counter_show, counter_click, original_conversion, test_conversion)
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
