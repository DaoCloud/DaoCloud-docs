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
        print('exquisite markdown document address', md_file)
        filepath, filename = os.path.split(md_file)
        with open(md_file, 'r') as f:
            post = f.read()

        images = re.compile(
            '!\\[.*?\\]\\((.*?)\\)|<img.*?src=[\'\"](.*?)[\'\"].*?>').findall(post)

        if images and len(images) > 0:
            for sub_images in images:
                for image in sub_images:
                    if image and len(image) > 0:
                        # determine whether the image is already a remote image, remote images are not automatically uploaded.
                        if not image.startswith('http'):
                            print('not images startswith http', image)
                            # if the path of the image contains ../, it means that it is placed in the parent directory of the markdown file.
                            if image.startswith('../'):
                                # Get how many layers of paths are in total.
                                depth = image.count('../')
                                # List of file paths
                                dir_list = filepath.split('/')

                                # rewrite image paths and automatically concatenate them based on the number of preceding path layers.
                                new_image = f"{'/'.join(dir_list[:-depth])}/{image.replace('../', '')}"

                                # determine if the image exists.
                                if os.path.exists(new_image):
                                    try:
                                        remote_file_url = ufile_upload(bucket, bucket_folder + new_image,
                                                                       new_image)
                                        if remote_file_url == 'failed':
                                            print('上传失败')
                                        else:
                                            modify_image_url(
                                                md_file, image, remote_file_url)

                                            # Delete image
                                            os.remove(new_image)
                                    except Exception as e:
                                        print(e)
                            else:
                                # if the prefix of the image starts with ./, it means the current directory and this step can be omitted.
                                if image.startswith('./'):
                                    image = image.replace('./', '')

                                # determine if the image exists.
                                if os.path.exists(image):
                                    new_image = os.path.join(filepath, image)

                                try:
                                    remote_file_url = ufile_upload(bucket, 'daocloud-docs-images/' + new_image,
                                                                   new_image)
                                    if remote_file_url == 'failed':
                                        print('upload failed')
                                    else:
                                        modify_image_url(
                                            md_file, image, remote_file_url)

                                        # delete image
                                        os.remove(new_image)
                                except Exception as e:
                                    print(e)
    time.sleep(0.2)


if __name__ == '__main__':
    # defualt find docs folder
    folder = sys.argv[1] or "docs"
    print(folder)
    update_image_path(find_md_files(folder))
