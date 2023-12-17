from collections import defaultdict

from PIL import Image
import os


def group_files_by_prefix(input_folder):
    # 获取输入文件夹中的所有文件
    input_files = os.listdir(input_folder)

    # 创建一个字典，用于存储以相同数字开头的文件
    file_groups = defaultdict(list)

    # 遍历文件夹中的每个文件
    # for input_file in input_files:
        # 检查文件是否是以数字开头的图片文件
        # if input_file.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
        #     # 提取文件名中的数字和后缀
        #     parts = input_file.split('-')
        #     prefix = parts[0]
        #     suffix = parts[1] if len(parts) > 1 else None
        #
        #     # 如果没有后缀或者后缀为1、2、3等，将文件路径添加到对应的数组中
        #     if suffix is None or suffix.isdigit() and int(suffix) in {1, 2, 3}:
        #         file_path = os.path.join(input_folder, input_file)
        #         file_groups[prefix].append(file_path)
    # file_groups[1].append(222)
    # file_groups[1].append(222)
    for input_file in input_files:
        # print(input_file)
        parts_ = input_file.split('.')
        # print(parts_[0])
        parts = str(parts_[0]).split('-')
        strr = str(parts[0]).replace(' ', '')
        # strrr = input_file.replace(' ', '')
        file_groups[strr].append(input_file)
        # print(file_groups)

        # for i in file_groups:
        #     parts_ = i.split('.')
        #     # print(parts_[0])
        #     partstemp = str(parts_[0]).split('-')
        #     file_groups[str(partstemp[0])].append(input_file)
            # if parts[0] == partstemp[0]:
            #     print(111)
            #     print(input_file)
            #     print(i)
            # # print(partstemp[0])



    # 返回存储文件路径的字典
    return file_groups

# def group_files_by_prefix(input_folder):
#     # 获取输入文件夹中的所有文件
#     input_files = os.listdir(input_folder)
#
#     # 创建一个字典，用于存储以相同数字开头的文件
#     file_groups = defaultdict(list)
#
#     # 遍历文件夹中的每个文件
#     for input_file in input_files:
#         # 检查文件是否是以数字开头的图片文件
#         if input_file.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
#             # 提取文件名中的数字和后缀
#             parts = input_file.split('-')
#             prefix = parts[0]
#             suffix = parts[1] if len(parts) > 1 else None
#
#             # 如果没有后缀或者后缀为1、2、3等，将文件路径添加到对应的数组中
#             if suffix is None or suffix.isdigit() and int(suffix) in {2, 3, 4, 5, 6, 7}:
#                 file_path = os.path.join(input_folder, input_file)
#                 file_groups[prefix].append(file_path)
#
#     # 返回存储文件路径的字典
#     return file_groups


def find_place(imgs):
    x1, y1 = imgs.size
    index = -1

    for y in range(1, y1 - 5):
        for x in range(1, x1 - 22):
            # 判断颜色是否符合【
            pixel = imgs.getpixel((x, y))
            index = 0

            # 判断颜色是否符合【
            if pixel == (71, 143, 214):
                if imgs.getpixel((x, y+1)) == (71, 143, 214):
                    if imgs.getpixel((x, y + 2)) == (71, 143, 214):
                        if imgs.getpixel((x, y + 3)) == (71, 143, 214):
                            if imgs.getpixel((x, y + 4)) == (71, 143, 214):
                                if imgs.getpixel((x, y + 5)) == (71, 143, 214):
                                    if imgs.getpixel((x, y + 6)) == (71, 143, 214):
                                        index = 1




            if index == 1:
                break
        if index == 1:
            break

    if index == 1:
        print(x, y)
        print("“@@@@@@@@@@@@@@”")
        for x1 in range(0,x+3):
            for y1 in range(0,y+46):
                imgs.putpixel((x1, y1), (255, 255, 255))

        print(imgs)
        return imgs

    else:
        return -1


def find____(img):
    x1, y1 = img.size
    index = -1

    y = 0
    for x in range(1, x1 - 22):
        for y in range(1, y1 - 5):
            # 判断颜色是否符合【
            pixel = img.getpixel((x, y))
            index = 0

            # 判断颜色是否符合【
            if pixel == (246, 197, 127):
                index = 1
                print(x, y)
                if img.getpixel((x + 1, y)) != (58, 18, 13):
                    index = 0
                    print(22121)
                    break
                if img.getpixel((x + 2, y)) != (13, 13, 13):
                    index = 0
                    # print(666666666666666)
                    break
                if img.getpixel((x + 4, y)) != (13, 13, 13):
                    index = 0
                    # print(666666666666666)
                    break
                if img.getpixel((x + 6, y)) != (13, 13, 13):
                    index = 0
                    print(666666666666666)
                    break
                if img.getpixel((x + 10, y)) != (14, 17, 50):
                    index = 0
                    print(666666666666666)
                    break
                if img.getpixel((x + 11, y)) != (114, 182, 236):
                    index = 0
                    print(666666666666666)
                    break
                # 第二行

                # print(666666666666666)
                y += 1
                if img.getpixel((x + 1, y)) != (52, 8, 0):
                    index = 0
                    print(666666666666666)
                    break
                if img.getpixel((x + 2, y)) != (0, 0, 0):
                    print(666666666666666)
                    index = 0
                    break
                if img.getpixel((x + 4, y)) != (0, 0, 0):
                    print(666666666666666)
                    index = 0
                    break
                if img.getpixel((x + 6, y)) != (0, 0, 0):
                    print(666666666666666)
                    index = 0
                    break
                if img.getpixel((x + 9, y)) != (0, 0, 4):
                    print(666666666666666)
                    index = 0
                    break
                if img.getpixel((x + 10, y)) != (26, 85, 156):
                    print(666666666666666)
                    index = 0
                    break

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
    trimmed_image = image.crop((left_bound-1, top_bound-1, right_bound + 1, bottom_bound + 1))

    return trimmed_image

def save(img,output_path):
    img.save(output_path)


def merge_images_vertically_and_trim_whitespace(top_half_path, bottom_half_path, row_spacing=35):
    # 打开上半段和下半段的图片
    top_image = Image.open(top_half_path)
    bottom_image = Image.open(bottom_half_path)

    top_image = find_place(top_image)

    # 对上半段进行白边切割
    trimmed_top = trim_whitespace(top_image)

    # 对下半段进行白边切割
    trimmed_bottom = trim_whitespace(bottom_image)

    # 获取上半段和下半段的宽度和高度
    top_width, top_height = trimmed_top.size
    bottom_width, bottom_height = trimmed_bottom.size

    # 初始化拼接后图片的宽度和高度，考虑行间距
    final_width = max(top_width, bottom_width)
    final_height = top_height + bottom_height + row_spacing + 35 + 10

    # 创建一个新的图片，白色背景
    merged_image = Image.new('RGB', (final_width, final_height), 'white')

    merged_image.paste(trimmed_top, (0, 0))

    # 计算下半段粘贴位置，考虑行间距
    paste_position = (0, top_height + row_spacing -10)

    # 将下半段粘贴到新的图片上
    merged_image.paste(trimmed_bottom, paste_position)

    # 保存合并后的图片
    return merged_image

def merge_two(top_half_path, bottom_half_path, row_spacing=35):
    # 打开上半段和下半段的图片
    top_image = Image.open(top_half_path)
    bottom_image = Image.open(bottom_half_path)

    # 对上半段进行白边切割
    trimmed_top = trim_whitespace(top_image)

    # 对下半段进行白边切割
    trimmed_bottom = trim_whitespace(bottom_image)

    # 获取上半段和下半段的宽度和高度
    top_width, top_height = trimmed_top.size
    bottom_width, bottom_height = trimmed_bottom.size

    # 初始化拼接后图片的宽度和高度，考虑行间距
    final_width = max(top_width, bottom_width)
    final_height = top_height + bottom_height + row_spacing + 35 + 10

    # 创建一个新的图片，白色背景
    merged_image = Image.new('RGB', (final_width, final_height), 'white')

    merged_image.paste(trimmed_top, (0, 0))

    # 计算下半段粘贴位置，考虑行间距
    paste_position = (0, top_height + row_spacing -10)

    # 将下半段粘贴到新的图片上
    merged_image.paste(trimmed_bottom, paste_position)

    # 保存合并后的图片
    return merged_image

def merge_one(top_half_path, row_spacing=35):
    # 打开上半段和下半段的图片
    top_image = Image.open(top_half_path)

    top_image = find_place(top_image)

    # 对上半段进行白边切割
    trimmed_top = trim_whitespace(top_image)


    # 获取上半段和下半段的宽度和高度
    top_width, top_height = trimmed_top.size


    # 初始化拼接后图片的宽度和高度，考虑行间距
    final_width = top_width
    final_height = top_height
    # 创建一个新的图片，白色背景
    merged_image = Image.new('RGB', (final_width, final_height), 'white')

    merged_image.paste(trimmed_top, (0, 0))

    # 保存合并后的图片
    return merged_image

def gogogo():

    top_image_path = r"D:\zhuomian\huaxue\ "
    bottom_image_path = r"D:\zhuomian\huaxue\ "
    output_path = r"D:\zhuomian\hx\ "
    baie = r"D:\zhuomian\baise.bmp"
    temp = r"D:\zhuomian\temp\temp.bmp"

    top_image_path = top_image_path.replace(" ",'')
    bottom_image_path = bottom_image_path.replace(" ",'')
    output_path = output_path.replace(" ",'')
    temp = temp.replace(" ",'')

    input_folder_path = r"D:\zhuomian\huaxue"

    # merge_images_vertically_and_trim_whitespace(top_image_path + "1.bmp", baie, output_path+ "1.bmp")

    file_groups = group_files_by_prefix(input_folder_path)
    # print(file_groups)
    for prefix, files in file_groups.items():
        num = len(files)
        if num == 1:
            img = merge_one(top_image_path+str(files[0]))
            save(img, output_path+str(prefix) + ".bmp")
            print(files)
        elif num == 2:   # [' 1058-2.bmp', '1058-3.bmp', ' 1058.bmp']
            # files = sorted(files, key=lambda x: (len(x), x.replace(" ", "")))
            files = sorted(files, key=lambda x: (len(x.replace(" ", "")), x))
            print(files)
            img = merge_images_vertically_and_trim_whitespace(top_image_path + str(files[0]), bottom_image_path + str(files[1]))
            save(img, output_path + str(prefix) + ".bmp")
        elif num == 3:
            files = sorted(files, key=lambda x: (len(x.replace(" ", "")), x))
            print(files)
            img = merge_images_vertically_and_trim_whitespace(top_image_path + str(files[0]),bottom_image_path + str(files[1]))
            save(img, temp)
            img = merge_two(temp,bottom_image_path + str(files[2]))
            save(img, output_path + str(prefix) + ".bmp")
        elif num == 4:
            files = sorted(files, key=lambda x: (len(x.replace(" ", "")), x))
            print(files)
            img = merge_images_vertically_and_trim_whitespace(top_image_path + str(files[0]),bottom_image_path + str(files[1]))
            save(img, temp)
            img = merge_two(temp,bottom_image_path + str(files[2]))
            save(img, temp)
            img = merge_two(temp, bottom_image_path + str(files[3]))
            save(img, output_path + str(prefix) + ".bmp")

        elif num == 5:
            files = sorted(files, key=lambda x: (len(x.replace(" ", "")), x))
            print(files)
            img = merge_images_vertically_and_trim_whitespace(top_image_path + str(files[0]),bottom_image_path + str(files[1]))
            save(img, temp)
            img = merge_two(temp, bottom_image_path + str(files[2]))
            save(img, temp)
            img = merge_two(temp, bottom_image_path + str(files[3]))
            save(img, temp)
            img = merge_two(temp, bottom_image_path + str(files[4]))
            save(img, output_path + str(prefix) + ".bmp")


    # files = os.listdir(input_folder_path)
    # sorted_files = sorted(files)
    #
    # # 输出所有文件名
    # for file in sorted_files:
    #     print(file)


gogogo()
# group_files_by_prefix(r"D:\zhuomian\huaxue")