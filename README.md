## Django REST Framework Features

- **Serializers:**
    - Transform complex data types into native Python data types.
- **Views in DRF:**
    - Define the logic for handling API requests.
- **SimpleRouter and DefaultRouter:**
    - Automatically generate URL routing for your API.
- **Permissions:**
    - Control access to your API endpoints.
  
## 📚 Task: Implement DRF Features

### 1. Create Serializers:
- Build serializers for transforming data from your models into JSON format.
- Use the serializers to handle both `GET` and `POST` requests.

### 2. Implement Views:
- Create views that use your serializers to handle API requests.
- Write views for retrieving and creating resources.

### 3. Set Up Routing:
- Use `SimpleRouter` or `DefaultRouter` to automatically generate URL routes for your API.
- Ensure the routes map correctly to your views.

### 4. Apply Permissions:
- Set up permission classes to restrict access to specific API endpoints.
- Test the permissions to ensure only authorized users can access certain views.
