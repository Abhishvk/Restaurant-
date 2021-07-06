import django
from django.contrib import admin

from .models import BookTable, Customer,ContactMessage


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','age','contact','email','address','password')
    ordering=('id',)
    list_filter=('age','address')
    search_fields=('first_name','email','address')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone',
                    'subject', 'message', 'date_sent'
                    ]
    search_fields = ['name', 'email']

@admin.register(BookTable)
class BookTableAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone',
                    'bdate', 'btime','bmessage','npeople'
                    ]
    list_filter=('btime','bdate')
    search_fields = ['name', 'email']
