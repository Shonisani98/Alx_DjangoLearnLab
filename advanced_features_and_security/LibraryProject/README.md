# Permissions and Groups Setup

## Custom Permissions
Defined in the `Book` model:
- `can_view`: Allows viewing book entries.
- `can_create`: Allows creating new books.
- `can_edit`: Allows editing existing books.
- `can_delete`: Allows deleting books.

## Groups
Created via Django admin:
- **Viewers**: Assigned `can_view`
- **Editors**: Assigned `can_view`, `can_create`, `can_edit`
- **Admins**: Assigned all permissions

## Views
Each view is protected using `@permission_required` decorators:
- `book_list` → requires `can_view`
- `create_book` → requires `can_create`
- `edit_book` → requires `can_edit`
- `delete_book` → requires `can_delete`

## Testing
Test users were assigned to each group and verified against protected views.

## Notes
Permissions are enforced using Django’s built-in system. Groups are managed via the admin panel or programmatically.
