from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    with open ('inflation_russia.csv', newline='', encoding='utf=8') as csvfile:

        file_csv = csv.reader(csvfile, delimiter=';')
        context = {'data': file_csv}

    # чтение csv-файла и заполнение контекста

        return render(request, template_name, context)
