import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
import pandas as pd
import pyodbc
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Type in browser name e.g. chrome or edge")


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class")
def browser_setup(browser):
    if browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-features=SSLHandshake")
        chrome_options.add_argument("--allow-running-insecure-content")  # Allow HTTP content instead of https content
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-features=BlockInsecurePrivateNetworkRequests")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--ignore-certificate-errors")
        edge_options.add_argument("--allow-running-insecure-content")  # Allow HTTP content instead of https content
        edge_options.add_argument("--disable-features=BlockInsecurePrivateNetworkRequests")
        edge_options.add_argument("--disable-features=SSLHandshake")
        driver = webdriver.Edge(options=edge_options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


########## PyTest HTML Report ############
def pytest_configure(config):
    # Check if pytest-html is being used
    if hasattr(config, 'metadata'):
        config.metadata['Project Name'] = 'MITR'
        config.metadata['Module Name'] = 'LoginTesting'
        config.metadata['Tester'] = 'Mani'


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    # Your existing hook logic
    pass


@pytest.fixture(scope="class")
def pandas_excel():
    def _load_data(sheet_name):
        file_path = r'C:\Users\manikanta\PycharmProjects\PythonTesting\HIS_POM_Pytest_Hybrid_framework\TestData\HIS_DATA_WorkBook.xlsx'
        data = pd.read_excel(file_path, sheet_name=sheet_name)
        return data

    return _load_data


# DataBase fixture - Setup
@pytest.fixture(scope="class")
def db_connection():
    """
    Establish a database connection to MS SQL Server.
    """
    connection_string = (
        "Driver={ODBC Driver 18 for SQL Server};"
        "Server=10.10.100.44;"
        "Database=HISTree_UAT;"
        "UID=10013887;"
        "PWD=Aigh@123$;"
        "Encrypt=no;"
    )
    try:
        conn = pyodbc.connect(connection_string)
        print("Database connection established.")
        yield conn  # Provide the connection object to the test
    except Exception as e:
        pytest.fail(f"Database connection failed: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")


# Query executing Fixture
@pytest.fixture(scope="class")
def execute_query(db_connection):
    """
    Execute a query on the database.
    """

    def _execute_query(query):
        try:
            cursor = db_connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()  # Fetch all results
            cursor.close()
            return results
        except Exception as e:
            pytest.fail(f"Query execution failed: {e}")

    return _execute_query


# Reusable email function
def send_email(recipients, subject, body, attachment_path=None):
    sender_email = "cheryshma.nadimpalli@aighospitals.com"
    password = "Cap@2405"

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Attach file if provided
    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename={os.path.basename(attachment_path)}'
        )
        msg.attach(part)

    # Connect to the email server and send the email
    try:
        with smtplib.SMTP("smtp.office365.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, recipients, msg.as_string())
            print("Emails sent successfully via Outlook!")
    except smtplib.SMTPAuthenticationError as e:
        print("Authentication failed. Please check your email or password.")
        print(f"Error details: {e}")
    except Exception as e:
        print(f"An error occurred while sending email: {e}")


# Fixture for email sending
@pytest.fixture(scope="session")
def email_manager():
    def _send_email(recipients, subject, body, attachment_path=None):
        send_email(recipients, subject, body, attachment_path)

    return _send_email
