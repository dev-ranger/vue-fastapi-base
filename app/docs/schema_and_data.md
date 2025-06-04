# Database Schema and Initial Data

This document provides an overview of how the database schema is defined and how initial data is populated.

## Database Schema (DDL)

The database schema for this application is defined by the [Tortoise ORM](https://tortoise.github.io/) models located in the `app/models/` directory, primarily in `app/models/admin.py`. These models describe the structure of the tables, columns, relationships, and data types.

Key models include:
*   `User`: Stores user information.
*   `Role`: Defines user roles and their permissions.
*   `Menu`: Manages the navigation menu structure.
*   `Api`: Lists available API endpoints and their permissions.
*   `Dept`: Manages department information.
*   `AuditLog`: Records audit trail of HTTP requests.

**Generating DDL (Optional):**

The application uses [Aerich](https://github.com/tortoise/aerich) (the migration tool for Tortoise ORM) to manage schema migrations. When the application starts with a new database, Aerich will create the tables based on these models.

If you need to inspect the DDL (Data Definition Language) that corresponds to the current models, you can use Aerich commands. After setting up your database connection in `app/settings/config.py` and ensuring `aerich` is installed (`pip install aerich`), you can typically run:

```bash
# Initialize aerich (if not already done for your specific database setup)
# aerich init-db

# To see the SQL that would be applied for migrations (includes table creation if new)
# aerich migrate --name some_migration_name (this generates a migration file)
# Then inspect the generated migration file in the 'migrations/models/' directory.

# Or, to directly inspect the database schema as understood by Tortoise ORM (less direct DDL):
# aerich inspect-db > schema_inspect.sql
```
The `init_db` function within `app/core/init_app.py` handles the schema initialization and migration process automatically when the application boots.

## Initial Data

Upon first startup with an empty or newly created database, the application automatically populates some essential initial data. This process is handled by the `init_data` function in `app/core/init_app.py`.

This function calls several sub-functions to create:

*   **Default Superuser:**
    *   Username: `admin`
    *   Password: `123456` (It is strongly recommended to change this immediately after first login)
    *   Email: `admin@admin.com`
    *   Details: See `init_superuser()` in `app/core/init_app.py`.

*   **Default Menus:**
    *   A set of pre-defined menus for system administration (User Management, Role Management, etc.).
    *   Details: See `init_menus()` in `app/core/init_app.py`.

*   **API Endpoint Registration:**
    *   The application scans available API endpoints and registers them in the `Api` table.
    *   Details: See `init_apis()` and `api_controller.refresh_api()` in `app/core/init_app.py`.

*   **Default Roles and Permissions:**
    *   **"관리자" (Administrator) Role:** Granted full access to all menus and APIs.
    *   **"일반 사용자" (Regular User) Role:** Granted access to all menus but only basic (GET) APIs and "기본 모듈" (Basic Module) APIs.
    *   Details: See `init_roles()` in `app/core/init_app.py`.

This initial data provides a ready-to-use system environment for administrative tasks. You can modify or add to this data through the application's interface after the initial setup.
```
