import io
import PIL

class ImageProcessor:
    @staticmethod
    def bytes_to_image(bytes: bytes) -> PIL.Image.Image:
        """Convert encoded image file to PIL image object.

        Args:
            bytes (bytes): Encoded image file as byte string

        Returns:
            PIL.Image.Image
        """
        img_file = io.BytesIO(bytes)
        img_file.seek(0)
        return PIL.Image.open(img_file)

    @staticmethod
    def image_to_bytes(image: PIL.Image.Image) -> bytes:
        """Convert PIL image object to PNG.

        Args:
            image (PIL.Image.Image)

        Returns:
            bytes: PNG file as byte string
        """
        img_file = io.BytesIO()
        image.save(img_file, format="PNG")
        return img_file.getvalue()
