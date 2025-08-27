# ALX Backend Caching Property Listings

## Overview
This project is part of the **ALX Backend Caching** series.  
It demonstrates how to build a Django-based property listing application with **Dockerized PostgreSQL** and **Redis caching**.

The project highlights:
- PostgreSQL for relational data persistence.
- Redis for caching querysets and view responses.
- Django caching strategies including cache invalidation and cache metrics analysis.

---

## Features & Tasks Completed

### 0. Set Up Django Project with Dockerized PostgreSQL and Redis
- Created a Django project named **`alx-backend-caching_property_listings`**.
- Added a `properties` app with a `Property` model:
  - `title` (CharField, max_length=200)
  - `description` (TextField)
  - `price` (DecimalField, max_digits=10, decimal_places=2)
  - `location` (CharField, max_length=100)
  - `created_at` (DateTimeField, auto_now_add=True)
- Configured `docker-compose.yml` with:
  - **PostgreSQL** (official `postgres:latest` image).
  - **Redis** (official `redis:latest` image).
- Updated Django settings:
  - PostgreSQL as the database backend.
  - Redis as the cache backend via **django-redis**.

---

### 1. Cache Property List View
- Implemented a `property_list` view in `properties/views.py`.
- Cached the response in Redis for **15 minutes** using `@cache_page(60 * 15)`.
- Mapped the view to `/properties/` via `properties/urls.py` and project-level `urls.py`.

---

### 2. Low-Level Caching for Property Queryset
- Added `get_all_properties()` in `properties/utils.py`:
  - Checks Redis for `all_properties`.
  - Fetches `Property.objects.all()` if not cached.
  - Stores queryset in Redis for **1 hour (3600 seconds)**.
- Updated `property_list` to use `get_all_properties()` for optimized caching.

---

### 3. Cache Invalidation Using Signals
- Implemented `properties/signals.py` with `post_save` and `post_delete` signal handlers.
- These handlers **invalidate the Redis cache** by deleting `all_properties` whenever a `Property` object is created, updated, or deleted.
- Registered signals in `properties/apps.py` using the `ready()` method.
- Updated `properties/__init__.py` to point to the custom `AppConfig`.

---

### 4. Cache Metrics Analysis
- Implemented `get_redis_cache_metrics()` in `properties/utils.py`:
  - Connects to Redis via `django_redis`.
  - Retrieves **`keyspace_hits`** and **`keyspace_misses`** from Redis INFO.
  - Calculates the **hit ratio**:  
    ```python
    hit_ratio = hits / total_requests if total_requests > 0 else 0
    ```
  - Returns metrics in a dictionary and logs them for monitoring.

---

## Tech Stack
- **Backend:** Django & Django REST Framework
- **Database:** PostgreSQL
- **Cache:** Redis (`django-redis`)
- **Containerization:** Docker & Docker Compose

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Killian1UP/alx-backend-caching_property_listings.git
   cd alx-backend-caching_property_listings
   ```

2. Start services:
   ```bash
   docker-compose up -d
   ```

3. Run migrations:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. Access the app:
   - API: `http://localhost:8000/api/properties/`
   - Admin: `http://localhost:8000/admin/`

---

## Author
**Ikaelelo Motlhako**  
ALX Backend Developer | Property Listings with Redis Caching