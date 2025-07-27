# AI Chat Flask Application

A simple Flask web application featuring an AI chat interface with a modern UI design including a header menu and left navigation sidebar.

## Features

- **Modern UI Design**: Clean and responsive design with gradient header and sidebar navigation
- **AI Chat Interface**: Interactive chat interface with simulated AI responses
- **Responsive Layout**: Works on desktop and mobile devices
- **Modular Structure**: Separate CSS and JavaScript files for maintainability
- **Multiple Pages**: Home, About, and Contact pages

## Project Structure

```
testversions/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── base.html         # Base template with header and sidebar
│   ├── index.html        # Home page with chat interface
│   ├── about.html        # About page
│   └── contact.html      # Contact page with form
└── static/               # Static files
    ├── css/
    │   └── style.css     # Main stylesheet
    └── js/
        └── main.js       # JavaScript functionality
```

## Installation and Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Access the application:**
   Open your web browser and navigate to `http://localhost:5000`

## Pages

- **Home (`/`)**: Main page with AI chat interface and feature cards
- **About (`/about`)**: Information about the AI Chat application
- **Contact (`/contact`)**: Contact form for user inquiries

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with modern design patterns
- **Responsive Design**: Mobile-first approach

## Development

The application follows modular design principles:
- CSS and JavaScript are kept in separate files
- Templates extend a base template for consistency
- Responsive design for mobile compatibility
- Clean and maintainable code structure

## Customization

You can easily customize the application by:
- Modifying colors in `static/css/style.css`
- Adding new routes in `app.py`
- Creating new templates in the `templates/` directory
- Extending JavaScript functionality in `static/js/main.js` 