# QuizTech

QuizTech is a powerful quiz application built using Flask, Python, and MySQL. This repository contains the source code and necessary files to create an interactive and feature-rich quiz platform. The application enables users to register, log in, select quiz categories, attempt quizzes, and view their results.

## Features

- **User Authentication**: The application includes user registration and login functionality to ensure secure access to the quiz platform.
- **Quiz Categories**: Users can choose from various quiz categories, providing a personalized quiz experience.
- **Dynamic Quiz Generation**: The application fetches questions and options from the MySQL database based on the selected quiz category, creating dynamic and engaging quizzes for each user.
- **Quiz Attempt and Scoring**: Users can attempt quizzes by selecting options for each question. The application calculates and displays the user's score and percentage based on the selected options.
- **User Responses**: The application stores user responses in the MySQL database, enabling future analysis and tracking of user performance.

## Getting Started

To set up the QuizTech application, follow these steps:

1. Ensure you have Python installed on your system.
   
2. Clone this repository to your local machine using the command:


3. Install the required dependencies by running the following command in your terminal:
   'pip install -r requirements.txt'
   
4. Set up a MySQL database and update the `db_config` dictionary in the code with your database details.
 
5. Run the application using the command:
                    'python main.py'
6. Access the application in your web browser at `http://localhost:5000`.

## File Structure

The repository is organized as follows:

- `main.py`: Contains the main application code and handles routing and logic.
- `templates/`: Directory containing HTML templates for the different application views.
- `static/`: Directory containing static files such as CSS stylesheets and JavaScript files.

## Dependencies

The QuizTech application has the following dependencies:

- Flask: A lightweight web framework for Python.
- MySQL Connector: A Python library for connecting and interacting with MySQL databases.

These dependencies are listed in the `requirements.txt` file and can be installed using `pip`.

## Contributing

Contributions to QuizTech are welcome! If you encounter any bugs or want to add new features, feel free to create issues or submit pull requests. Please ensure you follow the repository's code style and guidelines.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code in any way you see fit.

## Acknowledgements

The QuizTech application was developed by [ASTHA] as a demonstration of Flask, Python, and MySQL integration for building robust quiz platforms. It was inspired by the desire to create a user-friendly and technically advanced quiz application.
   
