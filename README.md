# Restaurant Booking Application

This is a Django application for managing restaurant reservations.

## Setup

### Environment Setup

1. **Clone the repository**

   ```bash
   git clone <URL_OF_YOUR_REPOSITORY>
   cd restaurant_booking
   ```

2. **Setup Virtual Environment**

   ```bash
   # Create a new virtual environment (optional)
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database**

   Ensure PostgreSQL is installed and configured. Create a PostgreSQL database and set the credentials in `restaurant_booking/settings.py`.

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_database_name',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. **Apply Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

7. **Access the Application**

   Access the application at [http://localhost:8000](http://localhost:8000)

## Using the APIs with Postman

1. **Authentication**

   - **Endpoint**: `http://localhost:8000/api/login/`
   - **Method**: POST
   - **Request Body**:
     ```json
     {
         "email": "your_email@example.com",
         "password": "your_password"
     }
     ```
   - **Example Response**:
     ```json
     {
         "access": "your_access_token",
         "refresh": "your_refresh_token"
     }
     ```

2. **List Reservations**

   - **Endpoint**: `http://localhost:8000/api/reservations/`
   - **Method**: GET
   - **Headers**: Add Authorization with value `Bearer your_access_token`
   - **Example Response**:
     ```json
     [
         {
             "id": 1,
             "customer_name": "João",
             "reservation_date": "2024-08-06T20:00:00Z",
             "number_of_guests": 4,
             "table_number": 5,
             "status": "active"
         },
         {
             "id": 2,
             "customer_name": "Maria",
             "reservation_date": "2024-08-08T19:30:00Z",
             "number_of_guests": 2,
             "table_number": 3,
             "status": "active"
         }
     ]
     ```

3. **Create a New Reservation**

   - **Endpoint**: `http://localhost:8000/api/reservations/`
   - **Method**: POST
   - **Headers**: Add Authorization with value `Bearer your_access_token`
   - **Request Body**:
     ```json
     {
         "customer_name": "Carlos",
         "reservation_date": "2024-08-10T21:00:00Z",
         "number_of_guests": 3,
         "table_number": 10
     }
     ```
   - **Example Response**:
     ```json
     {
         "id": 3,
         "customer_name": "Carlos",
         "reservation_date": "2024-08-10T21:00:00Z",
         "number_of_guests": 3,
         "table_number": 10,
         "status": "active"
     }
     ```

4. **Cancel a Reservation**

   - **Endpoint**: `http://localhost:8000/api/reservations/<id>/`
   - **Method**: DELETE
   - **Headers**: Add Authorization with value `Bearer your_access_token`
   - **Example Response**:
     ```json
     {
         "success": "Reservation 3 deleted successfully."
     }
     ```
