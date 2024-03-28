**#Library Inventory System**

The Library Inventory System is a comprehensive solution designed to streamline and manage daily library activities efficiently.

Technologies Used

This project is developed using Python with the Django Rest Framework, utilizing the following **versions**:

Python: 3.10.8
Django: 4.1.3
Django Rest Framework: 3.14.0

The system employs a **PostgreSQL database** to maintain records of user activities and library books. Please amend the database details in the settings.py file.



**Functionality**

The system encompasses seven distinct APIs, each serving a specific purpose:
1.**Health Check API**: Provides a quick check to ensure the application is up and running.

2.**Create User API**: Enables the creation of users with specific roles, allowing them to perform various tasks within the library.

3.**Books Available API**: Displays the number of copies available for borrowing and, if unavailable, provides information on when the book will be returned.

4.**Student Info API**: Allows students to view their borrowed books, including deadlines for return and borrowing history.

5.**Renew API**: Enables students to renew books that have not yet been renewed.

6.**Librarian View API**: Provides librarians with insights into which student has borrowed which book, return deadlines, borrowing history, etc.

7.**Student Record API**: Allows librarians to mark when a student borrows or returns a book.

Data Management

The project incorporates Django migrations to manage data related to books and user roles efficiently.

**Centralized Logging Mechanism**

This application incorporates a centralized logging mechanism to efficiently manage and store logs generated during its operation. The logging mechanism is designed to log messages both to a file and the console, ensuring comprehensive monitoring and analysis of system activities.

Key Features:

**Dual Logging:** Logs are simultaneously written to a designated log file and displayed in the console, providing real-time visibility into system events.

**Customizable Configuration:** The logging configuration can be customized according to requirements, including log levels, formatting, and output destinations.

**Error Handling:** The logging mechanism helps in identifying and troubleshooting errors by capturing relevant information, such as timestamps, error messages, and stack traces.

**Run the Application:** Execute the application, and observe the logging output in both the console and the designated log file. Monitor the logs to track system activities, debug issues, and analyze performance.

This system enhances library management by providing clear and accessible functionalities for both students and librarians, ensuring smooth operations and effective book tracking.
