from django.contrib import admin
from .models import Menssagens, VideoSugestao, SobreMim


class MenssagensAdmin(admin.ModelAdmin):
    list_display = ('id', 'menssagem', 'usuario', 'mostrar')
    list_display_links = ('id', 'menssagem')
    list_editable = ('mostrar', 'usuario')


class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario_video')
    list_display_links = ('id', 'usuario_video')
    


class SobreMimAdmin(admin.ModelAdmin):
    list_display = ('id', 'sobre', 'projetos', 'mostrar')
    list_display_links = ('sobre', )
    list_editable = ('mostrar', )

admin.site.register(Menssagens, MenssagensAdmin)
admin.site.register(VideoSugestao, VideoAdmin)
admin.site.register(SobreMim, SobreMimAdmin)
