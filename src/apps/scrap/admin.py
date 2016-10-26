from django.contrib import admin
from .models import Page, Images

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
	pass


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
	pass

