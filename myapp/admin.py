from django.contrib import admin

# Register your models here.

from .models import Post,calci,book,books
# Register your models here.
admin.site.register(Post)

admin.site.register(calci)
admin.site.register(book)
admin.site.register(books)
