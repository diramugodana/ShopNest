# ShopNest - Design Document

## Overview
ShopNest is a web application developed using Flask, a Python web framework. The application follows a Model-View-Controller (MVC) architecture, promoting organized and maintainable code.

## Project Structure

- `templates`: Contains HTML templates for different pages.
- `app.py`: Main application file with Flask routes and logic.
- `helpers.py`
- `commerce.db`: SQLite database file.
- `static`: Includes CSS and JavaScript files for styling and interactivity.

    ## JavaScript Files
- I have acknowledged the use of MIT licensing in the files where I've incorporated it to give due credit to the original authors.
    1. **breakpoint.min.js**
        - Handles how the site adjusts for different screen sizes.

    2. **browser.min.js**
         - Ensures the site functions well across various web browsers.

    3. **jquery.dropotron.js**
         - Enhances dropdown menus, making them more interactive.

    4. **jquery.min.js**
        - Enables interactive and responsive features on the site.

    5. **jquery.scrollex.min.js**
        - Adds special effects as you scroll through the site.

    6. **util.js**
        - Includes useful tools to improve various site functions.

    7. **main.js**
        - Sets up and initiates crucial features for the website.

    8. **script.js**
        - Provides additional functions for cart page implementation.

    ## Stylesheet Files (Sass)

    1. **_breakpoint.scss**
    - Manages the site's appearance on different devices and screens.

    2. **_functions.scss**
    - Contains tools for easier styling of the site.

    3. **_html-grid.scss**
    - Defines the layout of different sections on the website.

    4. **_mixins.scss**
    - Facilitates the reuse of certain styles throughout the site.

    5. **_vars.scss**
   - Keeps track of colors, sizes, and other design details.

    6. **_vendor.scss**
   - Handles styles for a consistent look across devices.

## Database
The SQLite database (`commerce.db`) plays a crucial role in storing user information, product details, and shopping cart data.

## Flask Routes
Flask routes define the application's navigation flow. From displaying product categories to managing the shopping cart, each route is meticulously designed for a coherent user experience.

## Templates
HTML templates in the `templates` folder provide the structure for rendering various pages. This approach enhances code clarity and facilitates template reuse throughout the application.

## Static Files
Styling is achieved through CSS files in `static/css`, while JavaScript files in `static/js` contribute to enhanced interactivity. jQuery is employed for efficient DOM manipulation.

## User Authentication
User authentication relies on Flask-Session, and passwords are securely hashed using Werkzeug's hashing functions. These measures ensure the security of sensitive user information.

## Cart Management
The shopping cart functionality allows users to seamlessly add, remove, and update quantities of items. Cart data is stored and managed within the SQLite database.

## Dependencies
ShopNest utilizes the following dependencies:
- Flask: Web framework.
- Flask-Session: Session management.
- SQLAlchemy: ORM for database interaction. (MIT licensed)
- jQuery: JavaScript library.

## Security
Security is prioritized with the secure storage of user information and the use of password hashes for authentication. Input validation safeguards against common security vulnerabilities.

## Design Decisions
Several design decisions contribute to the efficiency of ShopNest:
- Use of Flask for its simplicity and flexibility.
- Adoption of SQLite for easy database setup and management.
- Implementation of a responsive and intuitive user interface for a positive shopping experience.

## Future Enhancements
Looking ahead, potential enhancements include:
- Integration with a payment gateway for real transactions.
- Implementation of user profile management for order history and preferences.

