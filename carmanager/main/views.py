from django.shortcuts import render,redirect
from .models import Transport,Type_transport,Firm
from .forms import TransportForm,TypeForm,FirmForm
from django.views.generic import DetailView, UpdateView, DeleteView


#Классы для удаления элемента
class DetailDeleteTransport(DeleteView):
    model = Transport
    success_url = '/Transport'
    template_name = 'main/delete_transport.html'

class DetailDeleteType(DeleteView):
    model = Type_transport
    success_url = '/Type'
    template_name = 'main/delete_type.html'

class DetailDeleteFirm(DeleteView):
    model = Firm
    success_url = '/Firm'
    template_name = 'main/delete_firm.html'


#Классы для обновления элемента
class DetailUpdateTransport(UpdateView):
    model = Transport
    template_name = 'main/create_transport.html'

    form_class = TransportForm

class DetailUpdateType(UpdateView):
    model = Type_transport
    template_name = 'main/create_type.html'

    form_class = TypeForm

class DetailUpdateFirm(UpdateView):
    model = Firm
    template_name = 'main/create_firm.html'

    form_class = FirmForm



#Классы для обработки каждого элемента
class DetailViewTransport(DetailView):
    model = Transport
    template_name = 'main/details_view_transport.html'
    context_object_name = 'record_transport'

class DetailViewFirm(DetailView):
    model = Firm
    template_name = 'main/details_view_firm.html'
    context_object_name = 'record_firm'

class DetailViewType(DetailView):
    model = Type_transport
    template_name = 'main/details_view_type.html'
    context_object_name = 'record_type'

# Главная страница
def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница сайта'})

#Создатель страница
def about(request):
    return render(request, 'main/about.html')

#Добавление страница
def create(request):
    return render(request, 'main/create.html', {'title': 'Внесение изменений'})

#Таблицы
def transport(request):
    transport = Transport.objects.all()
    return render(request, 'main/transport.html', {'title': 'Транспорт', 'transport' : transport})

def firm(request):
    firm = Firm.objects.all()
    return render(request, 'main/firm.html', {'title': 'Фирмы', 'firm' : firm})

def type(request):
    type = Type_transport.objects.all()
    return render(request, 'main/type.html', {'title': 'Типы транспорта', 'type' : type})

#Добавление в таблицу
def create_transport(request):
    error = ''
    if request.method == 'POST':
        form = TransportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Transport')
        else:
            error = 'Форма была неверной'

    form = TransportForm()

    data = {
        'form' : form,
        'error': error
    }

    return render(request, 'main/create_transport.html',data)

def create_firm(request):
    error = ''
    if request.method == 'POST':
        form = FirmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Firm')
        else:
            error = 'Форма была неверной'

    form = FirmForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/create_firm.html', data)

def create_type(request):
    error = ''
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Type')
        else:
            error = 'Форма была неверной'

    form = TypeForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/create_type.html', data)



