from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='home'),
    path('about', views.about, name = 'about'),

    #Ссылки на таблицы
    path('Transport', views.transport, name = 'Transport'),
    path('Type', views.type, name = 'Type'),
    path('Firm', views.firm, name = 'Firm'),

    #Ссылки на формы для создания
    path('Create_firm', views.create_firm, name = 'Create_firm'),
    path('Create_transport', views.create_transport, name = 'Create_transport'),
    path('Create_type', views.create_type, name = 'Create_type'),

    #Ссылка на страницу с выбором добавления
    path('create', views.create, name = 'create'),

    #Конкретный элемент таблицы
    path('Transport/<int:pk>', views.DetailViewTransport.as_view(), name = 'transport-detail'),
    path('Type/<int:pk>', views.DetailViewType.as_view(), name = 'type-detail'),
    path('Firm/<int:pk>', views.DetailViewFirm.as_view(), name = 'firm-detail'),

    #Обновление элемента
    path('Transport/<int:pk>/update', views.DetailUpdateTransport.as_view(), name = 'transport-update'),
    path('Type/<int:pk>/update', views.DetailUpdateType.as_view(), name = 'type-update'),
    path('Firm/<int:pk>/update', views.DetailUpdateFirm.as_view(), name = 'firm-update'),

    #Удаление элемента
    path('Transport/<int:pk>/delete', views.DetailDeleteTransport.as_view(), name = 'transport-delete'),
    path('Type/<int:pk>/delete', views.DetailDeleteType.as_view(), name = 'type-delete'),
    path('Firm/<int:pk>/delete', views.DetailDeleteFirm.as_view(), name = 'firm-delete')
]
