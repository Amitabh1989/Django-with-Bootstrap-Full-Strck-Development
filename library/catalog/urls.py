from django.urls import path
from catalog.views import *

app_name = 'catalog'

# Remeber how update was not working
# After updating name and URL name as same, it worked.
# So keep names and url same. Atleast my experience says so.
# If I am able to find more details, will update.
urlpatterns = [
    path("", index, name="index"),
    path("create", BookCreate.as_view(), name="book_create"),
    path("list/", BookList.as_view(), name="book_list"),
    path("book_detail/<int:pk>", BookDetail.as_view(), name="book_detail"),
    path("book_update/<int:pk>", BookUpdate.as_view(), name="book_update"),
    path("book_delete/<int:pk>", BookDelete.as_view(), name="book_delete"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", CheckedOutBooksByUserView.as_view(), name="profile"),
]