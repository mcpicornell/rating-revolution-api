from django.contrib import admin
from .models import Company, Reviewer, Review


class CompanyAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'CIF', 'is_active')
    list_filter = ('is_active',)
    ordering = ('id', 'name')


class ReviewerAdmin(admin.ModelAdmin):

        list_display = ('id', 'name', 'is_active')
        list_filter = ('is_active',)
        ordering = ('id', 'name')


class ReviewAdmin(admin.ModelAdmin):

        list_display = ('id', 'reviewer', 'company', 'rating', 'is_active')
        list_filter = ('is_active',)
        ordering = ('id', 'reviewer')


admin.site.register(Review, ReviewAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Reviewer, ReviewerAdmin)
