from django.shortcuts import render

def index(request):
        return render(request, 'mainApp/homePage.html')


def  contact(request):
        return render(request, 'mainApp/basic.html', {'content': ['Если у вас остались вопросы, то задавайте их мне по телефону', '(+7)9214805398']} )


