# SimpleRouter/DefaultRouter

---

### **1. SimpleRouter**
The **SimpleRouter** is a basic router that automatically maps ViewSets to URLs but doesn’t provide additional features like handling a root view or adding a trailing slash to the URLs.

- **Use Case**: You can use `SimpleRouter` when you don’t need features like the root API view or trailing slashes.

#### **Example:**

```python
from rest_framework.routers import SimpleRouter
from .views import BookViewSet

router = SimpleRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

#### **Generated URL Patterns:**
- `GET /books/` – List all books.
- `POST /books/` – Create a new book.
- `GET /books/{id}/` – Retrieve a specific book by its ID.
- `PUT /books/{id}/` – Update a book.
- `PATCH /books/{id}/` – Partially update a book.
- `DELETE /books/{id}/` – Delete a book.

#### **Pros:**
- Simple and lightweight.
- Maps URLs directly to ViewSets.
- Good for cases where you don’t need advanced routing.

#### **Cons:**
- Lacks additional features like root API view and URL trailing slash handling.

---

### **2. DefaultRouter**
The **DefaultRouter** extends the functionality of **SimpleRouter** by adding some useful features like:
- **Root view**: A landing page that lists all available routes.
- **Trailing slashes**: It automatically handles URL routing with a trailing slash (`/`) at the end.

- **Use Case**: Use `DefaultRouter` when you want a more user-friendly API that automatically lists all routes and handles both trailing and non-trailing slashes.

#### **Example:**

```python
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

#### **Generated URL Patterns:**
- `GET /books/` – List all books.
- `POST /books/` – Create a new book.
- `GET /books/{id}/` – Retrieve a specific book by its ID.
- `PUT /books/{id}/` – Update a book.
- `PATCH /books/{id}/` – Partially update a book.
- `DELETE /books/{id}/` – Delete a book.
- **Root view**: `GET /` – List all the available ViewSets and routes in the API.

#### **Pros:**
- Automatically provides a root view for your API.
- Adds trailing slash support to all URLs.
- More user-friendly for clients consuming the API.

#### **Cons:**
- Slightly heavier than `SimpleRouter` due to the additional root view and trailing slash support.

---

### **Differences between SimpleRouter and DefaultRouter:**

| Feature                | SimpleRouter | DefaultRouter |
|------------------------|--------------|---------------|
| Root API view           | ❌ No         | ✅ Yes        |
| Basic routing support   | ✅ Yes        | ✅ Yes        |
| Suitable for minimal APIs | ✅ Yes     | ❌ More complex APIs |

---

### Conclusion:
- Use **SimpleRouter** when you want minimal, straightforward URL routing.
- Use **DefaultRouter** when you need the convenience of a root view and trailing slashes.
  
