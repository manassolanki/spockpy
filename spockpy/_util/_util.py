# imports - standard imports
import io
import base64

# imports - third-party imports
import numpy as np
from PIL import Image
import cv2

def _resize_image(image, size, maintain_aspect_ratio = False):
    copy = image.copy()

    copy.thumbnail(size, Image.ANTIALIAS)

    return copy

def _round_int(value):
    result = int(np.rint(value))

    return result

def _to_grayscale(array):
    gray = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)

    return gray

def _get_opencv_version():
    version = cv2.__version__
    version = version.split('.')

    major, minor, patch = int(version[0]), int(version[1]), int(version[2])

    return (major, minor, patch)

def _mount_roi(array, roi, color = (0, 255, 0), thickness = 1):
    x, y, w, h = roi

    cv2.rectangle(array, (x, y), (x + w, y + h), color = color, thickness = thickness)

    return array

def _image_to_bytes(image, format_ = '.jpg'):
    array   = np.asarray(image)
    _, jpeg = cv2.imencode(format_, array)
    bytes_  = jpeg.tobytes()

    return bytes_

def _base64_str_to_image(string):
    decode = base64.b64decode(string)
    bytes_ = io.BytesIO(decode)
    image  = Image.open(bytes_)

    return image