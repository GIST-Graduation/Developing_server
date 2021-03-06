# ---------------------------------- [edit] ---------------------------------- #
from django.urls import path


from .views import Upload_views

app_name = 'gist-graduation'

urlpatterns = [
    path('main/', Upload_views.upload_file, name='upload_file'),
    path('', Upload_views.upload_start, name='upload_start'),
    path('developers/', Upload_views.devs, name='developers'),
]
# ---------------------------------------------------------------------------- #