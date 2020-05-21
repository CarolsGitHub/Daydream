from django.contrib import admin
from .models import Users

# Register your models here.

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'sex', 'phone', 'email', 'password', 'c_time')

    # 文章列表里显示想要的字段

    list_per_page = 50
    # 满50条数据就自动分页

    ordering = ('c_time',)
    # 后台数据列表排列方式

    list_display_links = ('id', 'user')
    # 设置哪些字段可以点击进入编辑界面
