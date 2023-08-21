from django.contrib import admin

class BookrAdminSite(admin.AdminSite):
    title_header = "Bookr Admin"
    site_header = "Bookr Adminstration"
    index_title = "Bookr site admin"
    list_filter = "publisher"

