# ## 1)просто код( ниже через дженерики)
# # from django.urls import path

# # from .views import cat_list, cat_detail, CatListApi

# # urlpatterns = [
# #     path('cats/', CatListApi.as_view()),
# #     path('cats/<int:pk>/', cat_detail),
# # ]

# ## 2) Еще
# from django.urls import path

# from cats.views import CatList, CatDetail

# urlpatterns = [
#     path('cats/', CatList.as_view()),
#     path('cats/<int:pk>/', CatDetail.as_view()),
# ]
from django.urls import path, include

from .views import CatViewSet, OwnerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]