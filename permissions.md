# **Permissions in Django REST Framework ViewSets**

**Permissions** in Django REST Framework determine whether a user is allowed to perform a specific action 
(e.g., retrieve, create, update, delete) on a ViewSet. By default, DRF allows any request, but you can restrict access using permission classes.

### **1. Default Permission Classes**
DRF provides several built-in permission classes that you can use:

- **AllowAny**: Grants permission to all users, including unauthenticated users.
- **IsAuthenticated**: Grants permission only to authenticated users.
- **IsAdminUser**: Grants permission only to users with admin status.
- **IsAuthenticatedOrReadOnly**: Grants read-only access to unauthenticated users but requires authentication for write actions.

### **2. Setting Permissions in ViewSets**
You can set permission classes in your ViewSets using the `permission_classes` attribute. This can be done at the global level or at the individual ViewSet level.

#### **Global Permissions**
You can set global permissions in your settings.py file:

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

#### **ViewSet-Level Permissions**
You can override global permissions by specifying them in a specific ViewSet:

```python
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this ViewSet
```

### **3. Custom Permissions**
You can create custom permission classes by subclassing `BasePermission`. This allows you to define your own logic for granting or denying access.

#### **Example: Custom Permission Class**

```python
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
```

You can then apply this custom permission to your ViewSet:

```python
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsOwner]  # Only the owner of the book can edit it
```

### **4. Permissions and Actions**
You can customize permissions for different actions within a ViewSet using the `get_permissions()` method:

```python
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return super().get_permissions()  # Allow any user for read actions
```

### **5. Combining Multiple Permissions**
You can combine multiple permission classes by providing a list:

```python
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]  # User must be authenticated and an admin
```

### **Summary Table: Common Permission Classes**

| Permission Class                  | Description                                   |
|-----------------------------------|-----------------------------------------------|
| **AllowAny**                      | Grants permission to all users                |
| **IsAuthenticated**               | Grants permission only to authenticated users  |
| **IsAdminUser**                   | Grants permission only to admin users         |
| **IsAuthenticatedOrReadOnly**     | Grants read-only access to unauthenticated users but requires authentication for writes |
| **Custom Permissions**            | Define specific logic for access control      |

---

### Conclusion
Using permissions effectively in Django REST Framework ViewSets is crucial for securing your API. 
By leveraging built-in permissions, creating custom ones, and applying them at the global 
or ViewSet level, you can control access to your resources efficiently.
