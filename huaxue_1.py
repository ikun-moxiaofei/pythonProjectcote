from PIL import Image


def crop_and_save(input_path, output_path, left, top, right, bottom):
    # 打开原始BMP文件
    with Image.open(input_path) as img:
        # 使用crop方法截取指定区域
        cropped_img = img.crop((left, top, right, bottom)).convert("RGB")

        # 保存截取的图像为新的BMP文件
        cropped_img.save(output_path, "BMP")
        print(111)


is_ok = 0
zylan = 0
num = 0

def is_bai(bmp_file_path):
    with Image.open(bmp_file_path) as img:
        # 获取图像的宽度和高度
        width, height = img.size
        print(width, height)
        baise = 0
        for y in range(1, height):
            for x in range(1, width):
                if img.getpixel((x, y)) != (255, 255, 255):
                    baise = 1
                    break

        return baise


def locate_all_brackets_coordinates(bmp_file_path):
    global is_ok, zylan, num
    # print("aaa")
    # 打开 BMP 文件
    with Image.open(bmp_file_path) as img:
        # 获取图像的宽度和高度
        width, height = img.size
        print(width, height)

        # 遍历图像的每个像素
        for y in range(1, height):
            for x in range(1, 1250):

                if is_ok != 0:
                    # print(1)
                    start_x = 0
                    start_y = 0
                    end_x = 0
                    end_y = 0
                    yes = 0

                    if zylan == 1:
                        start_x = 1300
                        end_x = 2350
                    else:
                        start_x = 205
                        end_x = 1245

                    for x1 in range(1, 1250):
                        for start_y in range(1, height-20):
                            pixel = img.getpixel((x1, start_y))
                            if pixel != (255, 255, 255) and img.getpixel((x1 + 1, start_y)) != (255, 255, 255):
                                pixel = img.getpixel((x1, start_y + 1))
                                if pixel != (255, 255, 255) and img.getpixel((x1 + 1, start_y + 1)) != (255, 255, 255):
                                    pixel = img.getpixel((x1, start_y + 2))
                                    if pixel != (255, 255, 255) and img.getpixel((x1 + 1, start_y + 2)) != (
                                    255, 255, 255):
                                        pixel = img.getpixel((x1, start_y + 3))
                                        if pixel != (255, 255, 255) and img.getpixel((x1 + 1, start_y + 3)) != (
                                        255, 255, 255):
                                            pixel = img.getpixel((x1, start_y + 4))
                                            if pixel == (255, 255, 255) and img.getpixel((x1 + 1, start_y + 4)) == (
                                            255, 255, 255):
                                                pixel = img.getpixel((x1, start_y + 5))
                                                if pixel == (255, 255, 255) and img.getpixel((x1 + 1, start_y + 5)) == (
                                                255, 255, 255):
                                                    pixel = img.getpixel((x1, start_y + 6))
                                                    if pixel == (255, 255, 255) and img.getpixel(
                                                            (x1 + 1, start_y + 6)) == (255, 255, 255):
                                                        pixel = img.getpixel((x1, start_y + 7))
                                                        if pixel != (255, 255, 255) and img.getpixel(
                                                                (x1 + 1, start_y + 7)) != (255, 255, 255):
                                                            pixel = img.getpixel((x1, start_y + 8))
                                                            if pixel != (255, 255, 255) and img.getpixel(
                                                                    (x1 + 1, start_y + 8)) != (255, 255, 255):
                                                                pixel = img.getpixel((x1, start_y + 9))
                                                                if pixel != (255, 255, 255) and img.getpixel(
                                                                        (x1 + 1, start_y + 9)) != (255, 255, 255):
                                                                    pixel = img.getpixel((x1, start_y + 10))
                                                                    if pixel != (255, 255, 255) and img.getpixel(
                                                                            (x1 + 1, start_y + 10)) != (255, 255, 255):
                                                                        pixel = img.getpixel((x1, start_y + 11))
                                                                        if pixel == (255, 255, 255) and img.getpixel(
                                                                                (x1 + 1, start_y + 11)) == (
                                                                        255, 255, 255):
                                                                            pixel = img.getpixel((x1, start_y + 12))
                                                                            if pixel == (
                                                                            255, 255, 255) and img.getpixel(
                                                                                    (x1 + 1, start_y + 12)) == (
                                                                            255, 255, 255):
                                                                                pixel = img.getpixel((x1, start_y + 13))
                                                                                if pixel == (
                                                                                255, 255, 255) and img.getpixel(
                                                                                        (x1 + 1, start_y + 13)) == (
                                                                                255, 255, 255):
                                                                                    yes = start_y - 100
                                                                                    break
                        if yes != 0:
                            break
                    start_y = 300
                    # 找下一个【
                    y2 = start_y
                    for y2 in range(start_y, height):
                        for x2 in range(1, 1250):
                            # print(x,y)

                            # 获取当前像素的颜色值
                            pixel = img.getpixel((x2, y2))
                            index = 0

                            # 判断颜色是否符合【
                            if pixel == (246, 197, 127):
                                index = 1
                                print(x2, y2)
                                if img.getpixel((x2 + 1, y2)) != (58, 18, 13):
                                    print(img.getpixel((x2 + 1, y2)))
                                    index = 0
                                    print(x2 + 1, y2)
                                    print("!!!!!---------!!!!!!")
                                    break
                                if img.getpixel((x2 + 2, y2)) != (13, 13, 13):
                                    index = 0
                                    print(666666666666666)
                                    break
                                # 第二行
                                print(index)

                                print(666666666666666)
                                y2 += 1
                                if img.getpixel((x2 + 1, y2)) != (52, 8, 0):
                                    index = 0
                                    print(img.getpixel((x2 + 1, y2)))
                                    break
                                if img.getpixel((x2 + 2, y2)) != (0, 0, 0):
                                    print(img.getpixel((x2 + 2, y2)))
                                    index = 0
                                    break
                                if img.getpixel((x2 + 4, y2)) != (0, 0, 0):
                                    print(img.getpixel((x2 + 4, y2)))
                                    index = 0
                                    break
                                if img.getpixel((x2 + 6, y2)) != (0, 0, 0):
                                    print(img.getpixel((x2 + 6, y2)))
                                    index = 0
                                    break
                                if img.getpixel((x2 + 9, y2)) != (0, 0, 4):
                                    print(img.getpixel((x2 + 9, y2)))
                                    index = 0
                                    break
                                if img.getpixel((x2 + 10, y2)) != (26, 85, 156):
                                    print(img.getpixel((x2 + 10, y2)))
                                    index = 0
                                    break
                                print("////////////////////")
                                print(index)

                                if index == 1:
                                    break
                        if index == 1:
                            break
                    if index == 1:
                        print(2121)
                        end_y = y2 - 10
                    else:
                        end_y = 3150
                        is_ok = 1
                    # 定义截取区域的坐标(left, top, right, bottom)，根据需要进行调整
                    crop_coordinates = (start_x, start_y, end_x, end_y)
                    print("zuo")
                    print(start_x, start_y, end_x, end_y)

                    # 执行截取和保存操作
                    crop_and_save(bmp_file_path, output_bmp_path + str(num) + "-" + str(is_ok + 1) + ".bmp",
                                  *crop_coordinates)

                    if index == 1:
                        is_ok = 0
                    else:
                        is_ok =0

                    if is_ok == 3:
                        is_ok = 0

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

                    if img.getpixel((x + 2, y)) != (13, 13, 13):
                        index = 0
                        # print(666666666666666)

                    if img.getpixel((x + 4, y)) != (13, 13, 13):
                        index = 0
                        # print(666666666666666)

                    if img.getpixel((x + 6, y)) != (13, 13, 13):
                        index = 0
                        # print(666666666666666)

                    if img.getpixel((x + 10, y)) != (14, 17, 50):
                        index = 0
                        # print(666666666666666)

                    if img.getpixel((x + 11, y)) != (114, 182, 236):
                        index = 0
                        # print(666666666666666)

                    # 第二行

                    # print(666666666666666)
                    y += 1
                    if img.getpixel((x + 1, y)) != (52, 8, 0):
                        index = 0
                        # print(666666666666666)
                        break
                    if img.getpixel((x + 2, y)) != (0, 0, 0):
                        # print(666666666666666)
                        index = 0
                        break
                    if img.getpixel((x + 4, y)) != (0, 0, 0):
                        # print(666666666666666)
                        index = 0
                        break
                    if img.getpixel((x + 6, y)) != (0, 0, 0):
                        # print(666666666666666)
                        index = 0
                        break
                    if img.getpixel((x + 9, y)) != (0, 0, 4):
                        # print(666666666666666)
                        index = 0
                        break
                    if img.getpixel((x + 10, y)) != (26, 85, 156):
                        # print(666666666666666)
                        index = 0
                        break

                # 两行符合，大概可以判定符号是【
                if index == 1:
                    start_x = 0
                    start_y = 0
                    end_x = 0
                    end_y = 0
                    print(x, y)
                    if x < 1274:
                        zylan = 1
                    else:
                        zylan = 2
                    if x < 1274:
                        # 先判断这一行有没有分割线
                        have = 0
                        for x1 in range(1246, 1290):
                            for y1 in range(y, y + 150):
                                pixel = img.getpixel((x1, y1))
                                if pixel == (0, 0, 0):
                                    have = 1
                                    break
                                else:
                                    have = 0
                            if have == 1:
                                break
                        if have == 1:
                            end_x = 2400
                        else:
                            end_x = 1250

                    start_x = x - 20
                    start_y = y - 10
                    # print(x,y)

                    # 找下一个【
                    print("====---====")
                    print(x, y)
                    index = 0
                    for y2 in range(y + 60, height):
                        for x2 in range(1, 300):

                            # 判断颜色是否符合【
                            pixel = img.getpixel((x2, y2))

                            # 判断颜色是否符合【
                            if pixel == (246, 197, 127):
                                index = 1
                                print(x2, y2)
                                if img.getpixel((x2 + 1, y2)) != (58, 18, 13):
                                    print(img.getpixel((x2 + 1, y2)))
                                    index = 0
                                    print(x2 + 1, y2)
                                    print("!!!!!---------!!!!!!")
                                    break
                                if img.getpixel((x2 + 2, y2)) != (13, 13, 13):
                                    index = 0
                                    print(666666666666666)
                                    break
                                # 第二行
                                print(index)

                                print(666666666666666)
                                y2 += 1
                                if img.getpixel((x2 + 1, y2)) != (52, 8, 0):
                                    index = 0
                                    print(img.getpixel((x2 + 1, y2)))
                                    break
                                if img.getpixel((x2 + 2, y2)) != (0, 0, 0):
                                    print(img.getpixel((x2 + 2, y2)))
                                    index = 0
                                    break
                                if img.getpixel((x2 + 4, y2)) != (0, 0, 0):
                                    print(img.getpixel((x2 + 4, y2)))
                                    index = 0
                                    break
                                if img.getpixel((x2 + 6, y2)) != (0, 0, 0):
                                    print(img.getpixel((x2 + 6, y2)))
                                    index = 0
                                    break
                                if img.getpixel((x2 + 9, y2)) != (0, 0, 4):
                                    print(img.getpixel((x2 + 9, y2)))
                                    index = 0
                                    break
                                if img.getpixel((x2 + 10, y2)) != (26, 85, 156):
                                    print(img.getpixel((x2 + 10, y2)))
                                    index = 0
                                    break
                                print("////////////////////")
                                print(index)

                                if index == 1:
                                    break

                        if index == 1:
                            print(x2, y2)
                            print("++++++++++++++++++")
                            break

                    print(index)
                    print(",,,,,,,,,,,,,,,,,")
                    if index == 1:
                        print(2121)
                        end_y = y2 - 10
                    else:
                        end_y = 3150
                        is_ok += 1
                    # 定义截取区域的坐标(left, top, right, bottom)，根据需要进行调整
                    crop_coordinates = (start_x, start_y, end_x, end_y)
                    print("----------------------------")
                    print(start_y, start_x, end_x, end_y)
                    print("----------------------------")

                    # 执行截取和保存操作
                    num+=1
                    crop_and_save(bmp_file_path, output_bmp_path + str(num) + ".bmp", *crop_coordinates)


                    if is_ok != 0:

                        break
            if is_ok != 0:
                break

        for y in range(1, height):
            for x in range(1250, width):

                if is_ok != 0:
                    start_x = 0
                    start_y = 0
                    end_x = 0
                    end_y = 0
                    yes = 0

                    if zylan == 1:
                        start_x = 1300
                        end_x = 2350
                    else:
                        start_x = 205
                        end_x = 1245

                    for x1 in range(1246, 1290):
                        for start_y in range(1, height-20):
                            pixel = img.getpixel((x1, start_y))
                            if pixel != (255, 255, 255) and img.getpixel((x1 + 1, start_y)) != (255, 255, 255):
                                pixel = img.getpixel((x1, start_y + 1))
                                if pixel != (255, 255, 255) and img.getpixel((x1 + 1, start_y + 1)) != (255, 255, 255):
                                    pixel = img.getpixel((x1, start_y + 2))
                                    if pixel != (255, 255, 255) and img.getpixel((x1 + 1, start_y + 2)) != (
                                    255, 255, 255):
                                        pixel = img.getpixel((x1, start_y + 3))
                                        if pixel != (255, 255, 255) and img.getpixel((x1 + 1, start_y + 3)) != (
                                        255, 255, 255):
                                            pixel = img.getpixel((x1, start_y + 4))
                                            if pixel == (255, 255, 255) and img.getpixel((x1 + 1, start_y + 4)) == (
                                            255, 255, 255):
                                                pixel = img.getpixel((x1, start_y + 5))
                                                if pixel == (255, 255, 255) and img.getpixel((x1 + 1, start_y + 5)) == (
                                                255, 255, 255):
                                                    pixel = img.getpixel((x1, start_y + 6))
                                                    if pixel == (255, 255, 255) and img.getpixel(
                                                            (x1 + 1, start_y + 6)) == (255, 255, 255):
                                                        pixel = img.getpixel((x1, start_y + 7))
                                                        if pixel != (255, 255, 255) and img.getpixel(
                                                                (x1 + 1, start_y + 7)) != (255, 255, 255):
                                                            pixel = img.getpixel((x1, start_y + 8))
                                                            if pixel != (255, 255, 255) and img.getpixel(
                                                                    (x1 + 1, start_y + 8)) != (255, 255, 255):
                                                                pixel = img.getpixel((x1, start_y + 9))
                                                                if pixel != (255, 255, 255) and img.getpixel(
                                                                        (x1 + 1, start_y + 9)) != (255, 255, 255):
                                                                    pixel = img.getpixel((x1, start_y + 10))
                                                                    if pixel != (255, 255, 255) and img.getpixel(
                                                                            (x1 + 1, start_y + 10)) != (255, 255, 255):
                                                                        pixel = img.getpixel((x1, start_y + 11))
                                                                        if pixel == (255, 255, 255) and img.getpixel(
                                                                                (x1 + 1, start_y + 11)) == (
                                                                        255, 255, 255):
                                                                            pixel = img.getpixel((x1, start_y + 12))
                                                                            if pixel == (
                                                                            255, 255, 255) and img.getpixel(
                                                                                    (x1 + 1, start_y + 12)) == (
                                                                            255, 255, 255):
                                                                                pixel = img.getpixel((x1, start_y + 13))
                                                                                if pixel == (
                                                                                255, 255, 255) and img.getpixel(
                                                                                        (x1 + 1, start_y + 13)) == (
                                                                                255, 255, 255):
                                                                                    yes = start_y - 15
                                                                                    break
                        if yes != 0:
                            break

                    start_y = 10
                    # 找下一个【
                    y2 = start_y
                    for y2 in range(start_y, height):
                        for x2 in range(1270, width):
                            # print(x,y)

                            # 获取当前像素的颜色值
                            pixel = img.getpixel((x2, y2))
                            index = 0

                            # 判断颜色是否符合【
                            pixel = img.getpixel((x2, y2))
                            index = 0

                            # 判断颜色是否符合【
                            if pixel == (246, 197, 127):
                                index = 1
                                print(x2, y2)
                                if img.getpixel((x2 + 1, y2)) != (58, 18, 13):
                                    print(img.getpixel((x2 + 1, y2)))
                                    index = 0
                                    print(x2 + 1, y2)
                                    print("!!!!!---------!!!!!!")
                                    break
                                if img.getpixel((x2 + 2, y2)) != (13, 13, 13):
                                    index = 0
                                    print(666666666666666)
                                    break
                                # 第二行
                                print(index)

                                print(666666666666666)
                                y2 += 1
                                if img.getpixel((x2 + 1, y2)) != (52, 8, 0):
                                    index = 0
                                    print(img.getpixel((x2 + 1, y2)))
                                    break
                                if img.getpixel((x2 + 2, y2)) != (0, 0, 0):
                                    print(img.getpixel((x2 + 2, y2)))
                                    index = 0
                                    break
                                if img.getpixel((x2 + 4, y2)) != (0, 0, 0):
                                    print(img.getpixel((x2 + 4, y2)))
                                    index = 0
                                    break
                                if img.getpixel((x2 + 6, y2)) != (0, 0, 0):
                                    print(img.getpixel((x2 + 6, y2)))
                                    index = 0
                                    break
                                if img.getpixel((x2 + 9, y2)) != (0, 0, 4):
                                    print(img.getpixel((x2 + 9, y2)))
                                    index = 0
                                    break
                                if img.getpixel((x2 + 10, y2)) != (26, 85, 156):
                                    print(img.getpixel((x2 + 10, y2)))
                                    index = 0
                                    break
                                print("////////////////////")
                                print(index)

                                if index == 1:
                                    break
                        if index == 1:
                            break
                    if index == 1:
                        print(2121)
                        end_y = y2 - 10
                    else:
                        end_y = 3150
                        is_ok = 1
                    # 定义截取区域的坐标(left, top, right, bottom)，根据需要进行调整
                    crop_coordinates = (start_x, start_y, end_x, end_y)
                    print(start_x, start_y, end_x, end_y)

                    # 执行截取和保存操作
                    crop_and_save(bmp_file_path, output_bmp_path + str(num) +"-"+ str(is_ok + 1) + ".bmp",
                                  *crop_coordinates)

                    if index == 1:
                        is_ok = 0
                    else:
                        is_ok = 0
                        if is_ok==3:
                            is_ok = 0
                    # is_ok = 0

                pixel = img.getpixel((x, y))
                index = 0
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

                # 两行符合，大概可以判定符号是【
                start_x = 0
                start_y = 0
                end_x = 0
                end_y = 0
                if index == 1:
                    # print(1212)
                    if x < 1274:
                        zylan = 1
                    else:
                        zylan = 2
                        end_x = 2400
                    if x < 1274:
                        # 先判断这一行有没有分割线
                        have = 0
                        for x1 in range(1246, 1290):
                            for y1 in range(y, y + 150):
                                pixel = img.getpixel((x1, y1))
                                if pixel == (0, 0, 0):
                                    have = 1
                                    break
                                    # print(index)
                                else:
                                    have = 0
                                    # print(have)
                            if have == 1:
                                break
                        if have == 1:
                            end_x = 2400
                        else:
                            end_x = 1250

                    start_x = x - 20
                    start_y = y - 10

                    # 找下一个【
                    y2 = 0
                    for y2 in range(y + 20, height):
                        for x2 in range(1250, width):
                            # print(x,y)

                            # 获取当前像素的颜色值
                            pixel = img.getpixel((x2, y2))
                            index = 0

                            # 判断颜色是否符合【
                            pixel = img.getpixel((x2, y2))
                            index = 0

                            # 判断颜色是否符合【
                            if pixel == (246, 197, 127):
                                index = 1
                                print(x2, y2)
                                if img.getpixel((x2 + 1, y2)) != (58, 18, 13):
                                    print(img.getpixel((x2 + 1, y2)))
                                    index = 0
                                    print(x2 + 1, y2)
                                    print("!!!!!---------!!!!!!")
                                    break
                                if img.getpixel((x2 + 2, y2)) != (13, 13, 13):
                                    index = 0
                                    print(666666666666666)
                                    break
                                # 第二行
                                print(index)

                                print(666666666666666)
                                y2 += 1
                                if img.getpixel((x2 + 1, y2)) != (52, 8, 0):
                                    index = 0
                                    print(img.getpixel((x2 + 1, y2)))
                                    break
                                if img.getpixel((x2 + 2, y2)) != (0, 0, 0):
                                    print(img.getpixel((x2 + 2, y2)))
                                    index = 0
                                    break
                                if img.getpixel((x2 + 4, y2)) != (0, 0, 0):
                                    print(img.getpixel((x2 + 4, y2)))
                                    index = 0
                                    break
                                if img.getpixel((x2 + 6, y2)) != (0, 0, 0):
                                    print(img.getpixel((x2 + 6, y2)))
                                    index = 0
                                    break
                                if img.getpixel((x2 + 9, y2)) != (0, 0, 4):
                                    print(img.getpixel((x2 + 9, y2)))
                                    index = 0
                                    break
                                if img.getpixel((x2 + 10, y2)) != (26, 85, 156):
                                    print(img.getpixel((x2 + 10, y2)))
                                    index = 0
                                    break
                                print("////////////////////")
                                print(index)

                                if index == 1:
                                    break
                        if index == 1:
                            break
                    if index == 1:
                        print(2121)
                        end_y = y2 - 10
                    else:
                        end_y = 3150
                        is_ok = 1
                    # 定义截取区域的坐标(left, top, right, bottom)，根据需要进行调整
                    crop_coordinates = (start_x, start_y, end_x, end_y)
                    print(start_y, start_x, end_y, end_x)

                    # 执行截取和保存操作
                    num += 1
                    crop_and_save(bmp_file_path, output_bmp_path + str(num) + ".bmp", *crop_coordinates)


                    if is_ok == 1:

                        break
            if is_ok == 1:
                break


# 示例用法
for i in range(18,459):
    # "D:\zhuomian\新高考化学真题全刷：基础1500题 含扉页_18\新高考化学真题全刷：基础1500题 含扉页_00.bmp"
    bmp_file_path = "D:\zhuomian\新高考化学真题全刷：基础1500题 含扉页_18\新高考化学真题全刷：基础1500题 含扉页_"+str(i)+".bmp"
    output_bmp_path = "D:\zhuomian\huaxue\ "
    if is_bai(bmp_file_path) == 0:
        print(bmp_file_path)
    else:
        print(bmp_file_path)
        locate_all_brackets_coordinates(bmp_file_path)


# bmp_file_path = "D:\zhuomian\新高考化学真题全刷：基础1500题 含扉页_18\新高考化学真题全刷：基础1500题 含扉页_" + str(
#     18) + ".bmp"
# output_bmp_path = "D:\zhuomian\huaxue\ "
# locate_all_brackets_coordinates(bmp_file_path)

# bmp_file_path = "D:\zhuomian\新高考生物真题全刷：基础1000题 含扉页_25.bmp"
# output_bmp_path = "D:\zhuomian\end\ "
# locate_all_brackets_coordinates(bmp_file_path)

# D:\zhuomian\新高考生物真题全刷：基础1000题 含扉页_05.bmp
