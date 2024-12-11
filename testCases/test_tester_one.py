
class TestSheet1:
    def test_email_sending(self, email_manager):
        recipients = ["cheryshma.nadimpalli@aighospitals.com."]
        subject = "Test Email"
        body = "This is a test email sent via pytest."
        attachment_path = "C:\\Users\\manikanta\\PycharmProjects\\PythonTesting\\HIS_POM_Pytest_Hybrid_framework\\TestData\\Output_One.xlsx"

        # Test without attachment
        email_manager(recipients, subject, body)

        # Test with attachment
        email_manager(recipients, subject, body, attachment_path=attachment_path)


