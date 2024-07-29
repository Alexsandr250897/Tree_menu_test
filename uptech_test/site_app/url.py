from django.urls import path
import site_app.views as view

urlpatterns = [
    path('', view.main_view, name='main-page'),
    path('1/', view.second_view, name='second-view'),
    path('2/', view.third_view, name='third-view'),
    path('3/', view.fourth_view, name='fourth-view'),
    path('4/', view.fifth_view, name='fifth-view'),
    path('5/', view.sixth_view, name='sixth-view'),
]
