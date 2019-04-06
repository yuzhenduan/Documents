# -*- coding: utf-8 -*-
#######################
# envDeploy.urls
#######################

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('deploy/', include("deploy.urls")),
]
