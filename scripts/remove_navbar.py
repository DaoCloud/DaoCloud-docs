from PIL import Image
import numpy as np
import os


def detect_navbar_height(image):
    """Detects the height of the navbar based on average row intensity."""
    gray_image = image.convert("L")
    image_np = np.array(gray_image)
    row_intensity = np.mean(image_np, axis=1)

    split_index = None
    for i in range(1, len(row_intensity)):
        if row_intensity[i] > 200:  # 阈值可根据实际情况调整
            split_index = i
            break
    return split_index


def remove_navbar(image_path, output_path):
    """Removes the navbar from an image."""
    try:
        image = Image.open(image_path)
        split_index = detect_navbar_height(image)

        if split_index:
            cropped_image = image.crop((0, split_index, image.width, image.height))
            cropped_image.save(output_path)
            print(f"已成功处理图片: {image_path}, 保存到: {output_path}")
        else:
            print(f"未检测到导航栏: {image_path}")

    except Exception as e:
        print(f"处理图片 {image_path} 时出错: {e}")


def batch_process(input_dir, output_dir):
    """Batch processes images in a folder to remove navbars."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            remove_navbar(image_path, output_path)


def find_images_dirs(root_dir):
    """Finds and prints paths of 'images' directories within the given root directory."""
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if "images" in dirnames:
            images_dir_path = os.path.join(dirpath, "images")
            print(os.path.relpath(images_dir_path, root_dir))


if __name__ == "__main__":
    input_folder = "input"
    output_folder = "output"

    batch_process(input_folder, output_folder)

    # Find and print 'images' directories within 'docs'
    docs_folder = "docs"
    find_images_dirs(docs_folder)
