"""medicSearchAdmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #                    app     pasta arquivo
    path('', include('medicSearch.urls.HomeUrls')),
    path('profile/', include('medicSearch.urls.ProfileUrls')),      # url que lida com a mídia veiuculada na pasta media_root
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    


# MEDIA_URL = '/media/'  url que lida com a mídia veiuculada na pasta media_root

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media') Caminho absoluto do sistema de arquivos, 
# para pasta que conterá todos arquivos enviados pelo usuário 
