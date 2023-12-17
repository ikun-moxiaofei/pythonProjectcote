# 帮我修改一下程序，图片来源是一个文件夹，文件夹中相同数字开头的文件是需要用这种方法拼接的，如1-1和1-2和1-3，输出到一个特定的文件夹，文件名与输入第一个的文件名重名
from PIL import Image

def find_place(img):
    x1, y1 = img.size
    index = -1

    for x in range(1, x1 - 22):
        for y in range(1, y1 - 5):
            # 判断颜色是否符合【
            pixel = img.getpixel((x, y))
            if pixel == (215,232,252):
                index = 1
                for i in range(1,20):
                    if img.getpixel((x, y + i)) != (96,169,242):
                        index = -1
                        break
            if index == 1:
                break
        if index == 1:
            break

    if index == 1:
        print(x,y)
        image = img.crop((x+2, y-5, x1, y+55))
        return image

    else:
        return -1



def find____(img):
    x1, y1 = img.size
    index = -1

    for x in range(1, x1 - 22):
        for y in range(1, y1 - 5):
            # 判断颜色是否符合【
            pixel = img.getpixel((x, y))
            if pixel == (208, 157, 112):
                # print(y)
                index = 1
                for i in range(1, 20):
                    pixel1 = img.getpixel((x + i, y))
                    if pixel1 == (92, 90, 90):
                        index = 1
                        # print(index)
                    else:
                        index = 0
                    if i == 19:
                        pixel1 = img.getpixel((x + i + 1, y))
                        if pixel1 == (131, 176, 220):
                            index = 1
                            # print(index)
                        else:
                            index = 0
                            print(index)
                # 第二行
                y += 1
                pixel2 = img.getpixel((x, y))
                if index == 1 and pixel2 == (190, 119, 46):
                    for i in range(1, 19):
                        pixel2 = img.getpixel((x + i, y))
                        if i == 1:
                            if pixel2 == (6, 0, 0):
                                index = 1
                                # print(index)
                            else:
                                index = 0
                                # print(index)
                            continue

                        if i == 18:
                            pixel1 = img.getpixel((x + i, y))
                            if pixel2 == (0, 4, 28):
                                index = 1
                                # print(index)
                            else:
                                index = 0
                                print(index)
                            pixel1 = img.getpixel((x + i + 1, y))
                            if pixel1 == (71, 130, 187):
                                index = 1
                                # print(index)
                            else:
                                index = 0
                                print(index)
                            pixel1 = img.getpixel((x + i + 2, y))
                            if pixel1 == (229, 252, 255):
                                index = 1
                                # print(index)
                            else:
                                index = 0
                                print(index)
                            continue

                        if pixel2 == (0, 0, 0):
                            index = 1
                            # print(index)
                        else:
                            index = 0
                            print(index)
            if index == 1:
                break
        if index == 1:
            break

    if index == 1:
        # print(y)
        return y
    else:
        return -1


def trim_whitespace(image):
    # 获取图像的宽度和高度
    width, height = image.size

    # 仅切除每组第一张照片的一部分
    if "first_image_trimmed" not in trim_whitespace.__dict__:
        index = find____(image)
        if index != -1:
            print(index)
            image = image.crop((0, index + 50, width, height))

        trim_whitespace.first_image_trimmed = True

    # 获取新图像的宽度和高度
    width, height = image.size

    # 初始化上下左右边界
    top_bound = 0
    bottom_bound = height - 1
    left_bound = 0
    right_bound = width - 1

    # 查找上边界
    for y in range(height):
        row = [image.getpixel((x, y)) for x in range(width)]
        if any(color != (255, 255, 255) for color in row):
            top_bound = y
            break

    # 查找下边界
    for y in range(height - 1, 0, -1):
        row = [image.getpixel((x, y)) for x in range(width)]
        if any(color != (255, 255, 255) for color in row):
            bottom_bound = y
            break

    # 查找左边界
    for x in range(width):
        column = [image.getpixel((x, y)) for y in range(height)]
        if any(color != (255, 255, 255) for color in column):
            left_bound = x
            break

    # 查找右边界
    for x in range(width - 1, 0, -1):
        column = [image.getpixel((x, y)) for y in range(height)]
        if any(color != (255, 255, 255) for color in column):
            right_bound = x
            break

    # 切除白边
    trimmed_image = image.crop((left_bound, top_bound, right_bound + 1, bottom_bound + 1))

    return trimmed_image

def merge_images_vertically_and_trim_whitespace(top_half_path, bottom_half_path, output_path, row_spacing=35):
    # 打开上半段和下半段的图片
    top_image = Image.open(top_half_path)
    bottom_image = Image.open(bottom_half_path)

    place = find_place(top_image)

    # 对上半段进行白边切割
    trimmed_top = trim_whitespace(top_image)

    # 对下半段进行白边切割
    trimmed_bottom = trim_whitespace(bottom_image)

    # 获取上半段和下半段的宽度和高度
    top_width, top_height = trimmed_top.size
    bottom_width, bottom_height = trimmed_bottom.size

    # 初始化拼接后图片的宽度和高度，考虑行间距
    final_width = max(top_width, bottom_width)
    final_height = top_height + bottom_height + row_spacing + 50 + 35

    # 创建一个新的图片，白色背景
    merged_image = Image.new('RGB', (final_width, final_height), 'white')

    # 将上半段粘贴到新的图片上
    if place != -1:
        merged_image.paste(place, (0, 0))

    merged_image.paste(trimmed_top, (0, 70))

    # 计算下半段粘贴位置，考虑行间距
    paste_position = (0, top_height + row_spacing + 70)

    # 将下半段粘贴到新的图片上
    merged_image.paste(trimmed_bottom, paste_position)

    # 保存合并后的图片
    merged_image.save(output_path)

def gogogo():
    top_image_path = r"D:\zhuomian\end\ 1.bmp"
    bottom_image_path = r"D:\zhuomian\end\ 1-2.bmp"
    output_path = r"D:\zhuomian\end_\ result.bmp"

    merge_images_vertically_and_trim_whitespace(top_image_path, bottom_image_path, output_path)

gogogo()
