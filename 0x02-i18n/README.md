# Short Specializations - i18n Project

This project involves building a Flask application with internationalization (i18n) support. The goal is to parametrize the application to support multiple languages and locales, and to demonstrate how to handle localization of time zones, languages, and user preferences.

## Learning Objectives
By the end of this project, you will have learned how to:
- Parametrize Flask templates to display different languages.
- Infer the correct locale based on URL parameters, user settings, or request headers.
- Localize timestamps to the user's time zone.

## Requirements
- Your files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All your files should end with a new line.
- A `README.md` file at the root of your project folder is mandatory.
- Your code should follow the `pycodestyle` style (version 2.5).
- All your Python files should be executable.
- Each module, class, and function should have proper documentation with Python docstrings.
- All functions and coroutines must be type-annotated.

## Tasks Overview

### 0. Basic Flask App
- **Objective:** Set up a basic Flask app in `0-app.py`.
- **Files:** `0-app.py`, `templates/0-index.html`.
- **Description:** Create a single route (`/`) and an index template that outputs "Welcome to Holberton" as the page title and "Hello world" as a header.

### 1. Basic Babel Setup
- **Objective:** Install and configure Flask-Babel.
- **Files:** `1-app.py`, `templates/1-index.html`.
- **Description:** Configure the Babel object, set available languages (`en`, `fr`), and set the default locale to `en` and timezone to `UTC`.

### 2. Get Locale from Request
- **Objective:** Detect and select the appropriate locale based on user preferences or request headers.
- **Files:** `2-app.py`, `templates/2-index.html`.
- **Description:** Implement a `get_locale` function to select the appropriate locale based on the `Accept-Language` request header.

### 3. Parametrize Templates
- **Objective:** Parametrize your templates for localization.
- **Files:** `3-app.py`, `babel.cfg`, `templates/3-index.html`, translations for `en` and `fr`.
- **Description:** Extract and translate messages in `home_title` and `home_header` for both English and French.

### 4. Force Locale with URL Parameter
- **Objective:** Allow users to force a locale through URL parameters.
- **Files:** `4-app.py`, `templates/4-index.html`.
- **Description:** Add a `locale` parameter to the URL to force a language change (e.g., `?locale=fr` or `?locale=en`).

### 5. Mock Logging In
- **Objective:** Emulate a login system to change user locale and timezone.
- **Files:** `5-app.py`, `templates/5-index.html`.
- **Description:** Create a mock user system, allowing users to log in and change their locale and timezone preferences.

### 6. Use User Locale
- **Objective:** Modify the locale detection logic to use a user’s preferred locale.
- **Files:** `6-app.py`, `templates/6-index.html`.
- **Description:** Adjust `get_locale` function to prioritize locale settings from URL, user preferences, and request headers.

### 7. Infer Appropriate Time Zone
- **Objective:** Implement time zone detection based on user settings or URL parameters.
- **Files:** `7-app.py`, `templates/7-index.html`.
- **Description:** Implement `get_timezone` function to determine and validate the user's time zone.
