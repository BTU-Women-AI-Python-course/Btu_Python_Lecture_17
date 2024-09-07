## Django REST Framework Features

- **Serializers:**
    - Transform complex data types into native Python data types.
- **Views in DRF:**
    - Define the logic for handling API requests.
- **SimpleRouter and DefaultRouter:**
    - Automatically generate URL routing for your API.
- **Permissions:**
    - Control access to your API endpoints.
  
## 📚 Task: Implement DRF Features with a `Book` Model using Viewsets

### 1. Create a `BookSerializer`:
- Create a `Book` model with fields: `title`, `author`, and `published_date`.
- Build a `BookSerializer` to transform `Book` model data into JSON format.

### 2. Implement a `BookViewSet`:
- Create a `BookViewSet` to handle both listing all books and creating a new book.
- Use the `ModelViewSet` class to automatically provide `GET`, `POST`, `PUT`, and `DELETE` methods.

### 3. Set Up Routing:
- Use `DefaultRouter` to automatically generate routes for the `BookViewSet`.
- Example URLs should be:
  - `/api/books/` for listing and creating books.

### 4. Apply Permissions:
- Apply `IsAuthenticated` permission to restrict the creation of new books to logged-in users.
- The `GET` request should remain accessible to all users.


