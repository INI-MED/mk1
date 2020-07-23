
from django.urls import path

from . import views  # . means local library
from django.conf.urls import url

#app_name = "articles" # чтобы при переходе на ссылку не было пересечений по приложениям и он доставал конкретную привязку
urlpatterns = [
    url(r"product/(?P<product_id>\w+)/$", views.product, name="product"),

    #path("", views.index, name ="index"),
    #path("<int:article_id>/", views.detail, name ="detail"), # detail - псевдоним привязки для views, который выполнится когда
                                                             # будет осуществлен переход по ссылке /articles/1/ или любая другая цифра
    #path("<int:article_id>/leave_comment/", views.leave_comment, name ="leave_comment"),

]








