from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import customer_detail, customer_list, product_list , product_detail ,order_api

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Rest API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('customer_list/', customer_list, name="customer-list"),
    path('customer_list/<int:pk>/', customer_detail, name="customer-detail"),
    path('product_list/', product_list, name="product-list"),
    path('product_list/<int:pk>/', product_detail, name="product-detail"),
    path('order_api/', order_api, name="order-api"),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
