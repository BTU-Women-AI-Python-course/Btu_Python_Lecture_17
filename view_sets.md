# Django Rest Framework ViewSet

---

### **1. What are ViewSets?**
ViewSets in DRF allow you to combine the logic for multiple views in a single class. Instead of writing separate views for listing, retrieving, creating, updating, and deleting, ViewSets bundle them into one class, reducing redundancy and promoting DRY (Don't Repeat Yourself) principles.

### **2. Types of ViewSets**
There are three main types of ViewSets in DRF:

- **`ViewSet`**: The most basic ViewSet. You must define which actions (like list, create, retrieve, etc.) are supported.
- **`ModelViewSet`**: A powerful ViewSet that automatically provides actions such as list, create, retrieve, update, and delete for a model.
- **`ReadOnlyModelViewSet`**: A ViewSet that only provides read-only actions (list and retrieve).

### **3. Key Actions**
- **list**: Retrieve a list of all objects.
- **create**: Create a new object.
- **retrieve**: Retrieve a specific object by its ID.
- **update**: Update an object.
- **partial_update**: Update part of an object (PATCH).
- **destroy**: Delete an object.

### **4. Routers**
Routers in DRF automatically map ViewSets to URLs, which significantly simplifies URL configuration. A `router` will take care of mapping URLs for all actions of a ViewSet.

### **5. Example: Using a `ModelViewSet`**

```python
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

Here, the `BookViewSet` automatically provides list, retrieve, create, update, and delete actions for the `Book` model. 

### **6. Setting Up Routers**

```python
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

With the router, the following URL patterns are generated:
- `GET /books/` – List all books.
- `POST /books/` – Create a new book.
- `GET /books/{id}/` – Retrieve a specific book by its ID.
- `PUT /books/{id}/` – Update a book.
- `PATCH /books/{id}/` – Partially update a book.
- `DELETE /books/{id}/` – Delete a book.

### **7. Customizing ViewSets**

You can also customize the behavior of a ViewSet. For example, if you want to limit which actions are available or add custom behavior:

```python
class CustomBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request):
        # Custom logic for list view
        pass

    def retrieve(self, request, pk=None):
        # Custom logic for retrieve view
        pass
```

### **8. Mixins**
If you don't need all the actions provided by `ModelViewSet`, you can create a custom ViewSet using **mixins**:

```python
from rest_framework import viewsets, mixins

class CustomBookViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

This ViewSet only supports `list` and `retrieve` actions.

---
