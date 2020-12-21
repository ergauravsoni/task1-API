from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = routers.DefaultRouter()
router.register(r'api/timefhuman', views.tfRequestResponseViewSet)
#router.register(r'api/duckling', views.dkRequestResponseViewSet)
router.register(r'api/spacy', views.spRequestResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
