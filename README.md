# Music application which is implemented by Django version 5 for fullstack.
#This project will use python3.10, Django 5.0.5 and Postgresql for database.
The frontend site will be handled by bootstrap, html and javascript.

# Django Music App

A web application built with Django that allows users to manage and listen to their favorite music tracks.

![music_home_page](https://github.com/user-attachments/assets/dd1c5f07-ce84-4854-86af-3c09c2950537)

## Features

- User authentication and authorization
- Music track management (CRUD operations)
- Playlist creation and management
- Music streaming and playback
- Search functionality for tracks and playlists
- Responsive design for mobile and desktop

## Installation

### Prerequisites

- Python 3.10+
- Django 5.0.5
- Git

### Clone the Repository

```bash
git clone https://github.com/burmese-girl/django_music_app.git
cd django_music_app
```

### Create a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to view the app in your browser.

## Usage

- Sign up or log in to start using the app.
- Create, update, or delete your playlists.
- Search for your favorite music tracks and add them to your playlists.
- Enjoy streaming your music directly from the app.

## Project Structure

- **music_app/**: Main Django application directory.
  - **settings.py**: Project settings.
  - **urls.py**: URL routing for the project.
  - **views.py**: Application logic and handling.
  - **models.py**: Database models for music tracks, playlists, etc.
  - **static/**: Static files like CSS, JavaScript, and images.
  - **templates/**: HTML templates for rendering the web pages.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, feel free to contact me via [devstella80@gmail.com](mailto:devstella80@gmail.com).




