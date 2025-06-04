# Database Connection Guide (Supabase PostgreSQL)

This guide explains how to connect the application to your Supabase PostgreSQL database.

## 1. Obtain Supabase Connection Details

To connect to your Supabase project's PostgreSQL database, you will need the following details:

*   **Host:** Found in your Supabase project's Database settings (e.g., `db.<project-ref>.supabase.co`)
*   **Port:** Also in Database settings (usually `5432` for PostgreSQL)
*   **Database Name:** Typically `postgres`
*   **User:** Typically `postgres`
*   **Password:** The password you set for your database when creating the Supabase project or a specific role's password.

Navigate to your Supabase project dashboard, go to "Settings" -> "Database", and find the connection parameters.

## 2. Configure `app/settings/config.py`

Open the `app/settings/config.py` file in the project. Locate the `TORTOISE_ORM` dictionary. You need to update the `credentials` for the `"postgres"` connection with the details you obtained in Step 1.

```python
# app/settings/config.py

# ... (other settings) ...

class Settings(BaseSettings):
    # ... (other settings) ...

    TORTOISE_ORM: dict = {
        "connections": {
            # PostgreSQL configuration
            # Install with: tortoise-orm[asyncpg]
            "postgres": {
                "engine": "tortoise.backends.asyncpg",
                "credentials": {
                    "host": "YOUR_SUPABASE_HOST",  # Replace with your Supabase host
                    "port": 5432,                  # Default PostgreSQL port, change if Supabase uses a different one
                    "user": "YOUR_SUPABASE_USER",  # Replace with your Supabase username (e.g., "postgres")
                    "password": "YOUR_SUPABASE_PASSWORD",  # Replace with your Supabase database password
                    "database": "YOUR_SUPABASE_DBNAME",  # Replace with your Supabase database name (e.g., "postgres")
                },
            },
        },
        "apps": {
            "models": {
                "models": ["app.models", "aerich.models"],
                "default_connection": "postgres",
            },
        },
        "use_tz": False,  # Whether to use timezone-aware datetimes
        "timezone": "Asia/Shanghai",  # Timezone setting
    }
    # ... (other settings) ...

settings = Settings()
```

**Replace the placeholder values:**

*   `YOUR_SUPABASE_HOST`
*   `YOUR_SUPABASE_PORT` (if different from 5432)
*   `YOUR_SUPABASE_USER`
*   `YOUR_SUPABASE_PASSWORD`
*   `YOUR_SUPABASE_DBNAME`

## 3. Timezone Setting

The default timezone for the application is set to `"Asia/Shanghai"` in `app/settings/config.py`:

```python
        "timezone": "Asia/Shanghai",  # Timezone setting
```

If you are based in Korea or prefer a Korean timezone, you can change this to `"Asia/Seoul"`:

```python
        "timezone": "Asia/Seoul",
```

## 4. Database Schema and Migrations

This application uses [Tortoise ORM](https://tortoise.github.io/) for database interactions and [Aerich](https://github.com/tortoise/aerich) for database migrations.

The database schema (table structures) is defined by the ORM models located in the `app/models/` directory (e.g., `app/models/admin.py`).

When the application starts, the `init_db` function in `app/core/init_app.py` attempts to initialize the database and apply any pending migrations using Aerich. This will create the necessary tables in your Supabase PostgreSQL database based on the defined models.

You generally do not need to manually create tables if you are starting with a fresh database, as the application handles this.
```
