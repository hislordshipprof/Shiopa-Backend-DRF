# Shiopa DRF Backend

## Quick Setup

Make sure you have **Python 3.x** installed and **the latest version of pip** _installed_ before running these steps.

Clone the repository using the following command

```bash
git clone https://github.com/Techminate/Shiopa-Backend-DRF.git
# After cloning, move into the directory having the project files using the change directory command
cd Shiopa-Backend-DRF
```

Create a virtual environment where all the required python packages will be installed

```bash
# Use this on Windows
python -m venv env
# Use this on Linux and Mac
python -m venv env
```

Activate the virtual environment

```bash
# Windows
.\env\Scripts\activate
# Linux and Mac
source env/bin/activate
```

Install all the project Requirements

```bash
pip install -r requirements.txt
```

-Apply migrations

```bash
# apply migrations and create your database
python manage.py migrate

# Create a user with manage.py
python manage.py createsuperuser
```

Run the development server

```bash
# run django development server
python manage.py runserver

```

Default Admin User

```bash
# Username : admin
# Email: admin@email.com
# Password: Password
```

## EndPoints

- `/api/v1/all-categories` **Get all categories**
  - Method `get`
  - Returns an array of all available categories
  - Sample Response
  ```json
  [
    {
      "id": 1,
      "name": "Summer",
      "slug": "summer",
      "image_url": "http://127.0.0.1:8000/media/images/summer.jfif",
      "image_alt": "summer",
      "parent": null,
      "get_absolute_url": "/summer/",
      "products": []
    },
    {
      "id": 2,
      "name": "Bikini",
      "slug": "bikini",
      "image_url": "http://127.0.0.1:8000/media/images/bikini.jfif",
      "image_alt": "bikini",
      "parent": 1,
      "get_absolute_url": "/bikini/",
      "products": []
    },
    {
      "id": 3,
      "name": "Crop Top",
      "slug": "crop_top",
      "image_url": "http://127.0.0.1:8000/media/images/crop_top.jfif",
      "image_alt": "crop_top",
      "parent": 1,
      "get_absolute_url": "/crop_top/",
      "products": [
        {
          "id": 1,
          "name": "Crop Top",
          "slug": "crop_top",
          "description": "Crop top description",
          "additional_info": "",
          "price": "500.00",
          "discount_price": null,
          "sku": null,
          "available_to_purchase": true,
          "get_absolute_url": "/crop_top/crop_top/",
          "main_image_url": "http://127.0.0.1:8000/media/images/crop_top_0qe9D6a.jfif",
          "get_thumbnail": "http://127.0.0.1:8000/media/thumbnail/images/crop_top_0qe9D6a.jfif",
          "images": [
            {
              "id": 2,
              "title": "Crop Top",
              "alt_text": "crop top image",
              "image_url": "http://127.0.0.1:8000/media/images/crop_top_6WJNkBu.jfif"
            }
          ]
        }
      ]
    }
  ]
  ```
- `/api/v1/all-products/` **Get all products**
  - Method `get`
  - Returns an array of all products in the store
  - Sample Response
  ```json
  [
    {
      "id": 1,
      "name": "Crop Top",
      "slug": "crop_top",
      "description": "Crop top description",
      "additional_info": "",
      "price": "500.00",
      "discount_price": null,
      "sku": null,
      "available_to_purchase": true,
      "get_absolute_url": "/crop_top/crop_top/",
      "main_image_url": "http://127.0.0.1:8000/media/images/crop_top_0qe9D6a.jfif",
      "get_thumbnail": "http://127.0.0.1:8000/media/thumbnail/images/crop_top_0qe9D6a.jfif",
      "images": [
        {
          "id": 2,
          "title": "Crop Top",
          "alt_text": "crop top image",
          "image_url": "http://127.0.0.1:8000/media/images/crop_top_6WJNkBu.jfif"
        }
      ]
    }
  ]
  ```
- `/api/v1/products/<category_slug>/<product_slug>/`

  - Method `get`
  - Returns the details of a product
  - Sample Response

  ```json
  {
    "id": 1,
    "name": "Crop Top",
    "slug": "crop_top",
    "description": "Crop top description",
    "additional_info": "",
    "price": "500.00",
    "discount_price": null,
    "sku": null,
    "available_to_purchase": true,
    "get_absolute_url": "/crop_top/crop_top/",
    "main_image_url": "http://127.0.0.1:8000/media/images/crop_top_0qe9D6a.jfif",
    "get_thumbnail": "http://127.0.0.1:8000/media/thumbnail/images/crop_top_0qe9D6a.jfif",
    "images": [
      {
        "id": 2,
        "title": "Crop Top",
        "alt_text": "crop top image",
        "image_url": "http://127.0.0.1:8000/media/images/crop_top_6WJNkBu.jfif"
      }
    ]
  }
  ```

- `/api/v1/products/<category_slug>/` **Gets details of a specific category**

  - Method `get`
  - Returns the details of a category
  - Sample Response

  ```json
  {
    "id": 3,
    "name": "Crop Top",
    "slug": "crop_top",
    "image_url": "http://127.0.0.1:8000/media/images/crop_top.jfif",
    "image_alt": "crop_top",
    "parent": 1,
    "get_absolute_url": "/crop_top/",
    "products": [
      {
        "id": 1,
        "name": "Crop Top",
        "slug": "crop_top",
        "description": "Crop top description",
        "additional_info": "",
        "price": "500.00",
        "discount_price": null,
        "sku": null,
        "available_to_purchase": true,
        "get_absolute_url": "/crop_top/crop_top/",
        "main_image_url": "http://127.0.0.1:8000/media/images/crop_top_0qe9D6a.jfif",
        "get_thumbnail": "http://127.0.0.1:8000/media/thumbnail/images/crop_top_0qe9D6a.jfif",
        "images": [
          {
            "id": 2,
            "title": "Crop Top",
            "alt_text": "crop top image",
            "image_url": "http://127.0.0.1:8000/media/images/crop_top_6WJNkBu.jfif"
          }
        ]
      }
    ]
  }
  ```

- `/api/v1/search/`
  - Method `post`
  - Params
    - query | Search term (could be part of the product name or product description)
  - Returns a list of products depending on the query param passed
  - Sample Response
  ```json
  [
    {
      "id": 1,
      "name": "Crop Top",
      "slug": "crop_top",
      "description": "Crop top description",
      "additional_info": "",
      "price": "500.00",
      "discount_price": null,
      "sku": null,
      "available_to_purchase": true,
      "get_absolute_url": "/crop_top/crop_top/",
      "main_image_url": "http://127.0.0.1:8000/media/images/crop_top_0qe9D6a.jfif",
      "get_thumbnail": "http://127.0.0.1:8000/media/thumbnail/images/crop_top_0qe9D6a.jfif",
      "images": [
        {
          "id": 2,
          "title": "Crop Top",
          "alt_text": "crop top image",
          "image_url": "http://127.0.0.1:8000/media/images/crop_top_6WJNkBu.jfif"
        }
      ]
    }
  ]
  ```
