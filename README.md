# Web Monitoring Dashboard with System Information

This web application allows you to create a real-time dashboard for monitoring various system information, including CPU usage, memory usage, disk usage, network statistics, system uptime, and the number of running processes. It's built using Python and Flask for the backend, and HTML/CSS for the frontend.

## Prerequisites

Before you start using this web monitoring dashboard, make sure you have the following prerequisites in place:

1. **Python**:
   - Ensure that Python is installed on your system. If you don't have it, you can download and install Python from the [official Python website](https://www.python.org/downloads).
2. **flask**
   - Install the Flask library, which is used for creating the web application, by running:

   ```shell
   pip install Flask
3. **psutil Library**
   - Install the psutil library, which is used to collect system information, with the following command:
     ```shell
     pip install psutil

## Getting Started
1. Clone or download this repository to your local machine.
2. Navigate to the project directory using your terminal:
   ```shell
   cd web-system-monitoring
3. Install the required Python libraries:
   ```shell
   pip install Flask psutil
4. Start the web monitoring dashboard:
   ```shell
   python main.py
5. Access the dashboard in your web browser at http://127.0.0.1:80
6. The dashboard will display real-time system information, including CPU usage, memory usage, disk usage, network statistics, system uptime, and the number of running processes.
## Customization
You can customize the web monitoring dashboard to suit your needs. The following variables and options can be adjusted in the code:
   - **Additional Metrics**: You can add more metrics and system information to be displayed on the dashboard by modifying the Flask route and the HTML template.
   - **Styling**: Customize the CSS in the HTML template to change the look and feel of the dashboard to match your preferences.
   - **Refresh Rate**: Adjust the refresh rate for the real-time data update in the JavaScript part of the HTML template to control how often the data is       refreshed.
## Stopping the Dashboard
To stop the web monitoring dashboard and the real-time system information display, simply terminate the Flask application by pressing Ctrl+C in the terminal where it's running.
