from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    with open('inflation_russia.csv', newline='', encoding='utf=8') as file:
        file_csv = csv.reader(file, delimiter=';')
        context = {'data': file_csv}

        return render(request, template_name, context)
