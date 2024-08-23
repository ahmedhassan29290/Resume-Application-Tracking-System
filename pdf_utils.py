import base64
import io
import pdf2image

class PDFUtils:
    @staticmethod
    def convert_pdf_to_image(uploaded_file):
        """
        Convert the uploaded PDF file to a base64-encoded JPEG image.

        Parameters:
        - uploaded_file (UploadedFile): PDF file uploaded by the user.

        Returns:
        - list: List containing base64-encoded JPEG image.
        """
        if uploaded_file is not None:
            # Convert PDF to images
            images = pdf2image.convert_from_bytes(uploaded_file.read())

            # Convert the first page to JPEG format
            first_page = images[0]
            img_byte_arr = io.BytesIO()
            first_page.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()

            # Encode image as base64
            pdf_parts = [
                {
                    "mime_type": "image/jpeg",
                    "data": base64.b64encode(img_byte_arr).decode()  # Encode to base64
                }
            ]
            return pdf_parts
        else:
            raise FileNotFoundError("No file uploaded")
