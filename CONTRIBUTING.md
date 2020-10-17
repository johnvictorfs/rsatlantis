# How to contribute

- [Build instructions](#build-instructions)
- [Contribution guidelines](#contribution-guidelines)
  - [Tests](#tests)
  - [Linting](#linting)
  - [Coding Conventions](#coding-conventions)
- [License](#license)

---

# Build instructions

- Use [poetry](https://github.com/python-poetry/poetry) to install Python dependencies
  ```bash
  poetry install
  ```

- Make sure you have two [PostgresQL databases](https://www.postgresql.org/docs/9.1/app-createdb.html) created and running locally

- Create a settings file `/backend/local_settings.py` (git ignored file), make sure it is in the same directory as the already existing `settings.py` file (`/backend/settings.py`)

- Fill out your local settings file
  ```python
  import os

  # Generate secret key with the command below (from terminal)
  # python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())
  SECRET_KEY = 'your-secret-key-here'

  DEBUG = True

  # Datbase configuration, fill out your info for 2 databases
  DATABASES = {
      # API Database
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': 'rsatlantis',
          'USER': 'YOUR-USER',
          'PASSWORD': '',
          'HOST': 'localhost',
          'PORT': '',
      },
      # Discord Bot Database
      'discord': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': 'atlantisbot',
          'USER': 'YOUR-USER',
          'PASSWORD': '',
          'HOST': 'localhost',
          'PORT': '',
      }
  }

  # Discord OAuth settings
  # Reference: https://discord.com/developers/docs/topics/oauth2
  # Not needed to fill out anything below
  # if you're not using Discord Oauth locally
  DISCORD_OAUTH2_CLIENT_ID = 'YOUR-CLIENT-ID'
  DISCORD_OAUTH2_CLIENT_SECRET = 'YOUR-CLIENT-SECRET'
  DISCORD_OAUTH2_REDIRECT_URI = 'http://localhost:8080'

  DISCORD_API_BASE_URL = 'https://discord.com/api/v6'
  DISCORD_AUTHORIZATION_BASE_URL = DISCORD_API_BASE_URL + '/oauth2/authorize'
  DISCORD_TOKEN_URL = DISCORD_API_BASE_URL + '/oauth2/token'

  CORS_ORIGIN_WHITELIST = [
      # If your Vue local server is running on a different
      # port for some reason, change it accordingly here
      'http://localhost:8080'
  ]

  if DISCORD_OAUTH2_REDIRECT_URI.startswith('http://'):
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = 'true'
  ```

- Run database migrations
  ```bash
  poetry run python manage.py migrate
  ```

- Create superuser for local use
  ```bash
  poetry run python manage.py createsuperuser
  ```

- Run local Django server
  ```bash
  poetry run python manage.py runserver
  ```

- Run tests
  ```bash
  poetry run python manage.py test
  ```

- Reference documentation:
  - DRF Docs: https://www.django-rest-framework.org
  - Django Docs: https://docs.djangoproject.com

---
---

# Contribution Guidelines

## Tests

Always write tests for new or heavily changed features. Tests are located in the same folder as the [`'app'`](https://docs.djangoproject.com/en/3.1/ref/applications) with the name `tests.py` you are working on, if it has an API (`app_name/api` folder) then also create a `tests.py` for that.

![image](https://user-images.githubusercontent.com/37747572/95692790-ccc51980-0bfe-11eb-8595-03877ba4e33d.png)

See examples of tests in the project by looking at existing apps and their `tests.py` files.

Try to test only end results and not rely on implementation details for your tests, so they don't break if the API is changed even though their results could still be correct.

Refer to the [Django Docs](https://docs.djangoproject.com/en/3.1/topics/testing/) on creating tests.

---

## Linting

Every `app` needs to be properly linted and already come with the used configuration and libraries used for linting in their package manager files, so should already be installed.

If you use the [Visual Studio Code](https://github.com/microsoft/vscode) editor and open the workspace `ws.code-workspace` in the project root, it should ask you to install recommended extensions, those extensions will setup linting in the editor for you and highlight any linting errors automatically.

Linting is also checked for with CI when you make a pull request, pull requests that fail CI for linting will not be merged.

- **Python linting**
  ```bash
  flake8 --config=setup.cfg
  ```

---

## Coding conventions

- Every API endpoint should be a new app created with the command `python manage.py createapp APP_NAME`
  - Refer to [Django Docs](https://docs.djangoproject.com/en/3.1/ref/applications) on applications

  - Ex.: `/api/guides` API endpoint should be created with `python manage.py createapp guides` and a sub-folder `/guides/api` should be created. The `api` folder will have the serializers, views, tests and (if necessary) permission files, refer to the [DRF Docs](https://www.django-rest-framework.org/tutorial/quickstart) for more information on this entire folder.

  - CRUD API endpoints should preferably be made with a [DRF ViewSet](https://www.django-rest-framework.org/api-guide/viewsets) so most of its routes will be automatically generated by DRF and you will be able to easily add its endpoint to [`/backend/urls.py`](/backend/urls.py)
    ```python
    # /backend/urls.py
    from guides.api import views as guide_views

    router.register(r'guides', guide_views.GuideViewSet)
    ```

  - File structure example:

    ![image](https://user-images.githubusercontent.com/37747572/95693227-a18ff980-0c01-11eb-95da-a6164848980b.png)

---

## License

Refer to [LICENSE](LICENSE)
