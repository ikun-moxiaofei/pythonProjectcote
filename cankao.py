import csv
import qrcode
import os
import re
from PIL import Image

def clean_filename(filename):
    """
    Clean and sanitize the filename.
    """
    # Remove special characters and spaces, replace them with underscores
    filename = re.sub(r'[\\/*?:"<>| ]', "_", filename)
    return filename

def generate_qr_codes_with_colored_icon(csv_file_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    icon = Image.open('your_image.png')  # Load the colored icon image

    with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        counter = 1  # Initialize a counter

        for row in reader:
            name = clean_filename(row['name'])
            url = row['url']

            qr = qrcode.QRCode(
                version=8,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=3,
            )
            qr.add_data(url)
            qr.make(fit=True)

            # ... [previous code] ...

            # ... [之前的代码] ...

            # 将 QR 码图像转换为 RGBA 模式以便与图标兼容
            qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGBA')

            # 计算放置图标的中心位置
            qr_size = qr_image.size[0]
            icon_size = qr_image.size[0]  # 根据需要调整图标大小
            x = (qr_size - icon_size) // 2
            y = (qr_size - icon_size) // 2

            # 调整图标大小并确保其为 RGBA 模式
            resized_icon = icon.resize((icon_size, icon_size)).convert('RGBA')

            # 将调整后的图标粘贴到 QR 码上
            qr_image.paste(resized_icon, (x, y), mask=resized_icon)

            # 如有需要，将最终图像转换为 CMYK 模式
            final_image = qr_image.convert('CMYK')




            # ... [rest of the code] ...


            # Add a sequential number to the filename
            filename_with_number = f"[{counter}] {name}.jpg"
            png_file_path = os.path.join(output_folder, filename_with_number)
            final_image.save(png_file_path)

            counter += 1  # Increment the counter

# 使用示例
generate_qr_codes_with_colored_icon('csvfile.csv', 'output/')


