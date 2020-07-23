
from django.urls import path
from django.conf.urls import url
from . import views  # . means local library

#app_name = "articles" # чтобы при переходе на ссылку не было пересечений по приложениям и он доставал конкретную привязку
urlpatterns = [
    path("", views.home, name="home"),
    url(r"^detail/$", views.detail, name="detail"), # detail - псевдоним привязки для views, который выполнится когда # будет осуществлен переход по ссылке /articles/1/ или любая другая цифра
    url(r"^sections/", views.sections, name="sections"),
    url(r"^surgery/", views.surgery_section, name="surgery"),
    url(r"^cosmetics/", views.cosmetics_section, name="cosmetics"),
    url(r"^about/", views.about_us, name="about"),
    #url(r"^contacts", views.contacts, name="contacts")

]








