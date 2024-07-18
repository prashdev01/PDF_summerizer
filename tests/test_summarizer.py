import unittest
from app.summarizer import extract_text_from_pdf, summarize_text
from io import BytesIO

class TestSummarizer(unittest.TestCase):

    def setUp(self):
        # Setup code, if needed
        pass

    def test_extract_text_from_pdf(self):
        # Create a simple PDF in memory
        pdf_content = b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R >>\nendobj\n4 0 obj\n<< /Length 44 >>\nstream\nBT /F1 24 Tf 100 700 Td (Hello, World!) Tj ET\nendstream\nendobj\nxref\n0 5\n0000000000 65535 f \n0000000010 00000 n \n0000000053 00000 n \n0000000100 00000 n \n0000000194 00000 n \ntrailer\n<< /Size 5 /Root 1 0 R >>\nstartxref\n281\n%%EOF"
        pdf_file = BytesIO(pdf_content)

        text = extract_text_from_pdf(pdf_file)
        self.assertIn("Hello, World!", text)

    def test_summarize_text(self):
        text = "Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of intelligent agents: any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals."
        summary = summarize_text(text)
        
        self.assertTrue(isinstance(summary, str))
        self.assertGreater(len(text), len(summary))
        self.assertIn("intelligence", summary)

    def tearDown(self):
        # Teardown code, if needed
        pass

if __name__ == '__main__':
    unittest.main()
