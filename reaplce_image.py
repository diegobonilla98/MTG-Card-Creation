from PIL import Image


def replace_image(background, image, top_left=[29, 59], bottom_right=[345, 290], aspect_ratio_tolerance=0.1):
    target_width = bottom_right[0] - top_left[0]
    target_height = bottom_right[1] - top_left[1]
    target_aspect_ratio = target_width / target_height

    original_width, original_height = image.size
    original_aspect_ratio = original_width / original_height

    if original_aspect_ratio > target_aspect_ratio:
        new_height = target_height
        new_width = int(original_aspect_ratio * new_height)
        image_resized = image.resize((new_width, new_height), Image.ANTIALIAS)
        if abs(original_aspect_ratio - target_aspect_ratio) > aspect_ratio_tolerance:
            left = (new_width - target_width) // 2
            right = left + target_width
            image_cropped = image_resized.crop((left, 0, right, new_height))
        else:
            image_cropped = image_resized
    else:
        new_width = target_width
        new_height = int(new_width / original_aspect_ratio)
        image_resized = image.resize((new_width, new_height), Image.ANTIALIAS)
        if abs(original_aspect_ratio - target_aspect_ratio) > aspect_ratio_tolerance:
            top = (new_height - target_height) // 2
            bottom = top + target_height
            image_cropped = image_resized.crop((0, top, new_width, bottom))
        else:
            image_cropped = image_resized
    background.paste(image_cropped, (top_left[0], top_left[1]))
    return background
