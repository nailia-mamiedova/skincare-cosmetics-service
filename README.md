# skincare-cosmetics-service

## Description

This project is a simple platform created to explore and discover different skin care products, 
brands and skin types. Members can share and learn about different skincare products and 
find products that suit their specific skin types and preferences. It's a community-driven project 
that aims to increase knowledge and awareness of different skincare products and 
help individuals make informed choices for their skincare routines. 

## Local Setup

### Prerequisites

Ensure you have the following installed on your local machine:

- Python (3.8 or higher)
- git

### Steps to Set Up

1. Clone the Repository:
    
    Clone the repository to your local machine with:
    
    ```git clone https://github.com/nailia-mamiedova/skincare-cosmetics-service.git```

2. Navigate to the Project Directory:

    ```cd skincare-cosmetics-service```

3. Create a Virtual Environment:
    
    ```python -m venv venv```

4. Activate the Virtual Environment:

    - On Windows:

        ```.\venv\Scripts\activate```

    - On macOS/Linux:

        ```source venv/bin/activate```

5. Install the Required Packages:
    
    ```pip install -r requirements.txt```

6. Setup Environment Variables:

    - Copy the sample environment variables file:
   
        ```cp .env.sample .env```
    
    - Open the .env file and replace your-secret-key-here with your actual secret key.

7. Apply Migrations:
    
    ```python manage.py migrate```

8. Run the Server:
    
    ```python manage.py runserver```

The application will start running on http://127.0.0.1:8000/.

## Login Credentials

After migrating you can use these default credentials for login or create new superuser:
- **Username:** admin
- **Password:** admin
