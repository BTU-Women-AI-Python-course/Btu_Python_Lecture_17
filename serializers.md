# Django REST Framework - Advanced Serializers

This document covers advanced features of Django REST Framework's (DRF) Serializers. It assumes you are already familiar with the basics of DRF and Serializers.

## Table of Contents

- [Nested Serializers](#nested-serializers)
- [Serializer Method Fields](#serializer-method-fields)
- [Writable Nested Serializers](#writable-nested-serializers)
- [Custom Validation](#custom-validation)
- [Dynamic Fields](#dynamic-fields)
- [Inheritance with Serializers](#inheritance-with-serializers)

---

### Nested Serializers

When a serializer needs to include data from related models, use nested serializers.

```python
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'author']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'comments']
```

- `many=True`: This specifies that multiple comment objects will be serialized.
- Use nested serializers to include related models' data in the serialized output.

---

### Serializer Method Fields

`SerializerMethodField` allows you to define a custom field in your serializer that is not part of the model.

```python
class PostSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'comment_count']

    def get_comment_count(self, obj):
        return obj.comments.count()
```

- `get_<fieldname>`: This method is called to populate the custom field.
- Use for read-only fields that require custom logic.

---

### Writable Nested Serializers

To make nested serializers writable, use `create()` and `update()` methods to handle the saving of nested data.

```python
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'comments']

    def create(self, validated_data):
        comments_data = validated_data.pop('comments')
        post = Post.objects.create(**validated_data)
        for comment_data in comments_data:
            Comment.objects.create(post=post, **comment_data)
        return post
```

- `create()`: Handles the creation of related objects when the parent object is created.
- Use writable nested serializers to save related data alongside the parent model.

---

### Custom Validation

You can define custom validation for fields and objects by overriding `validate_<field>()` or `validate()` methods.

```python
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'publish_date']

    def validate_title(self, value):
        if 'django' not in value.lower():
            raise serializers.ValidationError("Title must contain the word 'django'")
        return value

    def validate(self, data):
        if data['publish_date'] < timezone.now():
            raise serializers.ValidationError("Publish date must be in the future.")
        return data
```

- Field-level validation (`validate_<field>`): Use this for single-field validation.
- Object-level validation (`validate`): Use this for cross-field validation.

---

### Dynamic Fields

You can customize which fields get included based on runtime logic using `get_fields()`.

```python
class DynamicFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'comments']

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(DynamicFieldsSerializer, self).__init__(*args, **kwargs)
        if fields:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
```

- This allows filtering the fields dynamically by passing a `fields` argument to the serializer.

**Example**

```python
from rest_framework import viewsets


class MyModelSerializer(DynamicFieldsSerializer):
    class Meta:
        model = MyModel  
        fields = ['id', 'slug', 'title', 'description', 'created_at']


class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()  # Replace with your actual model
    
    def get_serializer(self, *args, **kwargs):
        fields = ['id', 'slug', 'title']
        if fields:
            return MyModelSerializer(*args, **kwargs, fields=fields)
        return MyModelSerializer(*args, **kwargs)
```

---

### Inheritance with Serializers

Serializer inheritance allows you to reuse logic across serializers.

```python
class BasePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content']

class ExtendedPostSerializer(BasePostSerializer):
    comments = CommentSerializer(many=True)

    class Meta(BasePostSerializer.Meta):
        fields = BasePostSerializer.Meta.fields + ['comments']
```

- Base serializers can be extended to add or override fields in child serializers.

---
