import io
from PIL import Image

class ImageProcessor:
    @staticmethod
    def bytes_to_image(bytes: bytes) -> Image.Image:
        """Convert encoded image file to PIL image object.

        Args:
            bytes (bytes): Encoded image file as byte string

        Returns:
            Image.Image
        """
        img_file = io.BytesIO(bytes)
        img_file.seek(0)
        return Image.open(img_file)

    @staticmethod
    def image_to_bytes(image: Image.Image) -> bytes:
        """Convert PIL image object to PNG.

        Args:
            image (Image.Image)

        Returns:
            bytes: PNG file as byte string
        """
        img_file = io.BytesIO()
        image.save(img_file, format="PNG")
        return img_file.getvalue()
