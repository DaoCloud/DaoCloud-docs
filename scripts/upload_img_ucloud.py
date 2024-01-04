# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""

import re
import os
import sys
import time
from ufile import filemanager, config, logger

public_key = os.getenv("U_PUBLIC_KEY")
private_key = os.getenv("U_PRIVATE_KEY")
uploadsuffix = os.getenv("U_UPLOADSUFFIX")

config.set_default(uploadsuffix=uploadsuffix)  # ucloud domain

ufile_handler = filemanager.FileManager(public_key, private_key)

# bucket infomation
bucket = os.getenv("U_BUCKET")
bucket_folder = os.getenv("U_BUCKET_FOLDER")
remote_domain = os.getenv("U_REMOTE_DOMAIN")

logger.set_log_file('ufile.log')


def modify_image_url(md_file, image, remote_file_url):
    with open(md_file, 'r') as f:
        post = f.read()

    post = post.replace(image, remote_file_url)

    with open(md_file, 'w') as f:
        f.write(post)


def ufile_upload(bucket: str, remotefile: str, localfile: str, header=None):
    _, resp = ufile_handler.putfile(bucket, remotefile, localfile, header)
    if resp.status_code == 200:
        return remote_domain + '/' + remotefile
    else:
        return "failed"


def find_md_files(folder: str):
    md_files = []

    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))

    return md_files


def update_image_path(md_files: list):
    for md_file in md_files:
        # print('exquisite markdown document address: ', md_file)
        filepath, filename = os.path.split(md_file)
        with open(md_file, 'r') as f:
            post = f.read()

        images = re.compile(
            '!\\[.*?\\]\\((.*?)\\)|<img.*?src=[\'\"](.*?)[\'\"].*?>').findall(post)

        if images and len(images) > 0:
            for sub_images in images:
                for image in sub_images:
                    if image and len(image) > 0:
                        # 确定图像是否已经是远程图像，远程图像不会自动上传
                        if not image.startswith('http'):
                            # 如果图像的路径包含../，这意味着它被放置在 Markdown 文件的上级目录中。
                            if image.startswith('../'):
                                # 获取总共有多少层路径
                                depth = image.count('../')
                                # 文件路径列表
                                dir_list = filepath.split('/')

                                # 重写图像路径并根据前面路径层的数量自动连接它们
                                # new_image = f"{'/'.join(dir_list[:-depth])}/{image.replace('../', '')}"
                                path = '/'.join(dir_list[:-depth])
                                new_image = (
                                    f"{path}/"
                                    f"{image.replace('../', '')}"
                                )

                                # 确定图像是否存在
                                if os.path.exists(new_image):
                                    try:
                                        remote_file_url = ufile_upload(bucket, bucket_folder + new_image,
                                                                       new_image)
                                        if remote_file_url == 'failed':
                                            print('上传失败')
                                        else:
                                            modify_image_url(
                                                md_file, image, remote_file_url)

                                            # 删除图像
                                            os.remove(new_image)
                                    except Exception as e:
                                        print(e)

                            elif image.startswith('./'):
                                # 如果图像的前缀以"./"开头，表示当前目录，可以省略此步骤
                                if image.startswith('./'):
                                    image = image.replace('./', '')
                                    new_image = os.path.join(filepath, image)
                                    print(md_file, image, 'bad image path, 11111')

                                try:
                                    remote_file_url = ufile_upload(bucket, 'daocloud-docs-images/' + new_image,
                                                                   new_image)
                                    if remote_file_url == 'failed':
                                        print('upload failed')
                                    else:
                                        modify_image_url(
                                            md_file, './' + image, remote_file_url)

                                        # delete image
                                        os.remove(new_image)
                                except Exception as e:
                                    print(e)
                                    print(md_file, image, 'bad image path, 22222')

                            else:
                                print(md_file, image, 'bad image path, 33333')
    time.sleep(0.2)


if __name__ == '__main__':
    # defualt find docs folder
    folder = sys.argv[1] or "docs"
    update_image_path(find_md_files(folder))
