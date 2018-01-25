from PIL import Image, ImageFilter
from resizeimage import resizeimage


def blue_line(path, side=800):
    blue = Image.open(
        '/home/basecamp/Projects/DailyExercises/December/Instagram/mysite/static/mysite/images/lighting.jpg'
    ).convert('RGB')
    blue = resizeimage.resize_cover(blue, [side, side], validate=False)
    blue = blue.convert('RGB').quantize(64).convert('RGB')

    image = Image.open(path).convert('RGB')
    w, h = image.size
    s = min([w, h])
    box = ((w - s) // 2, (h - s) // 2, (s + w) // 2, (s + h) // 2)
    image = image.crop(box=box)

    image = resizeimage.resize_cover(image, [side, side], validate=False)
    image = image.convert('RGB').quantize(255).convert('RGB')

    # get the new size
    w, h = image.size
    pixel_data = list(image.getdata())

    new_data = []
    n = len(pixel_data)
    for i in range(n):
        t = pixel_data[i]
        r, g, b = t
        new_data.append((r, max(0, int(g - 255 * (i**2 / n**2))), max(
            0, int(b - 255 * (i**2 / n**2)))))

    image = Image.new('RGB', (w, h))
    image.putdata(new_data)
    image = resizeimage.resize_cover(image, [side, side], validate=False)
    image = image.convert('RGB')

    finalimage = Image.blend(image, blue, .3)
    finalimage.save(path)
    return True