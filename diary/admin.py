from django.contrib import admin

# Register your models here.
from .models import Diary

# 管理サイトに登録
admin.site.register(Diary)
