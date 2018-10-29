from django.contrib import admin
from django.utils.translation import gettext as _
from blog_app.models import UserInfo
from blog_app.utils.cryptoutils import CryptoUtil

admin.site.site_header = _("my site header")
admin.site.site_title = _('my site title')


# Register your models here.

class UserInfoAmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'is_super', 'status', 'email', 'mobile')
    list_per_page = 10
    ordering = ('-id',)
    list_editable = ['is_super', 'status']
    list_display_links = ('id', 'username')
    list_filter = ('status',)  # 过滤器
    search_fields = ('username',)  # 搜索字段

    def save_model(self, request, obj, form, change):
        if obj.password is not None:
            obj.password = CryptoUtil.md5_encode(obj.password)
        obj.save()


admin.site.register(UserInfo, UserInfoAmin)
