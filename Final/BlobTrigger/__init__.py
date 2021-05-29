import logging
import io
import azure.functions as func
from PIL import Image


def generate_thumbnail(blob: func.InputStream, size=(128, 128)):
    pil_image = Image.open(blob)
    in_memory_file = io.BytesIO()
    pil_image.thumbnail(size, Image.ANTIALIAS)

    pil_image.save(in_memory_file, format=pil_image.format)
    return in_memory_file.getvalue()


def main(myblob: func.InputStream, blobout: func.Out[bytes], context: func.Context):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    thumbnail = generate_thumbnail(myblob)
    blobout.set(thumbnail)

    logging.info(f"Thumbnail generated successfully")
