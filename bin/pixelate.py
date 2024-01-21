from PIL import Image
import math
import random

static_root = "static/"


def recreate_image_with_n_pixels(filename, n):
    n = math.sqrt(n) * 5
    # Open the image file
    original_image = Image.open(static_root + filename)

    # Calculate new size
    original_width, original_height = original_image.size
    aspect_ratio = original_width / original_height
    new_height = int(math.sqrt(n / aspect_ratio))
    new_width = int(n / new_height)

    # Resize the image, reducing quality
    if new_height < original_height:
    	resized_image = original_image.resize((new_width, new_height))
    else:
        resized_image = original_image

    # Save the new image
    new_filename = str(random.randint(1, 99999999)) + "_" + filename
    resized_image.save(static_root + new_filename, 'PNG')

    return new_filename


