from django.urls import path
from . import views

urlpatterns = [
    
    # * Users endpoints
    path('users/find/all', views.getAllUsers, name="findAllUsers"),
    path('users/find/<str:id>', views.getById, name="findUserById"),
    path("users/create", views.createUser, name="createUser"),
    path("users/edit/<str:id>", views.updateUser, name="editUser"),
    path("users/delete/<str:id>", views.deleteUser, name="deleteUser"),
    path("users/login", views.authenticate, name="loginUser"),
    
    # * Collections endpoints
    path("collections/find/all", views.findAllCollections, name="findAllCollections"),
    path("collections/create", views.createNewCollection, name="createNewCollection"),
    path("collections/find/<str:id>", views.findCollectionById, name="findOneCollection"),
    path("collections/edit/<str:id>", views.updateCollection, name="editCollection"),
    path("collections/delete/<str:id>", views.deleteCollection, name="deleteCollection"),

    # * Books endpoints
    
    path("books/create", views.createNewBook, name="createNewBook"),
    path("books/find/all", views.findAllBooks, name="findAllBooks"),
    path("books/find/collection/<str:id>", views.findAllBooksIntoCollection, name="findAllBooksIntoCollection"),
    path("books/find/<str:id>", views.findBookById, name="findBookBydId"),
    path("books/edit/<str:id>", views.updateBook, name="updateBook"),
    path("books/delete/<str:id>", views.deleteBook, name="deleteBook")
]