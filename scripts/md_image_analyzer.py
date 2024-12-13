import re
import sys
import os
from typing import Dict, List, Tuple
from urllib.parse import urlparse

# Import functions from upload_img_ucloud.py
from upload_img_ucloud import ufile_upload, modify_image_url


class MarkdownImageAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        # Corrected Markdown 图片语法的正则表达式
        self.md_image_pattern = r"!\[([^\]]*)\]\(([^)]+)\)"
        # HTML img 标签的正则表达式
        self.html_image_pattern = r'<img[^>]+src=["\'](.*?)["\']'

    def is_url(self, path: str) -> bool:
        """判断路径是否为URL"""
        parsed = urlparse(path)
        return parsed.scheme in ("http", "https")

    def analyze_images(self) -> Dict[int, List[Tuple[str, str]]]:
        """分析Markdown文件中的图片引用

        Returns:
            Dict[int, List[Tuple[str, str]]]:
            键为行号，值为包含(图片路径, 引用类型)的列表
        """
        results = {}

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                for line_num, line in enumerate(file, 1):
                    # 查找Markdown格式的图片
                    md_matches = re.finditer(self.md_image_pattern, line)
                    # 查找HTML格式的图片
                    html_matches = re.finditer(self.html_image_pattern, line)

                    images = []

                    # 处理Markdown格式的图片
                    for match in md_matches:
                        path = match.group(2).strip()
                        img_type = "HTTP" if self.is_url(path) else "本地"
                        images.append((path, img_type))

                    # 处理HTML格式的图片
                    for match in html_matches:
                        path = match.group(1).strip()
                        img_type = "HTTP" if self.is_url(path) else "本地"
                        images.append((path, img_type))

                    if images:
                        results[line_num] = images

            return results

        except FileNotFoundError:
            print(f"错误：找不到文件 {self.file_path}")
            return {}
        except (IOError, OSError) as e:
            print(f"处理文件时发生IO错误: {str(e)}")
            return {}
        except re.error as e:
            print(f"处理文件时发生正则表达式错误：{str(e)}")
            return {}

    def upload_and_replace_images(
        self, bucket: str, bucket_folder: str, remote_domain: str
    ):
        """上传本地图片到UCloud并替换Markdown文件中的图片路径"""
        results = self.analyze_images()
        if not results:
            print("未找到任何图片引用")
            return

        for line_num, images in results.items():
            for path, img_type in images:
                if img_type == "本地":
                    abs_path = os.path.abspath(
                        os.path.join(os.path.dirname(self.file_path), path)
                    )
                    if os.path.exists(abs_path):
                        try:
                            remote_file_url = ufile_upload(
                                bucket, bucket_folder + path, abs_path
                            )
                            if remote_file_url != "failed":
                                modify_image_url(self.file_path, path, remote_file_url)
                                os.remove(abs_path)
                            else:
                                print(f"上传失败: {path}")
                        except Exception as e:
                            print(f"上传图片时发生错误: {str(e)}")
                    else:
                        print(f"本地图片不存在: {abs_path}")


def main():
    # 使用示例
    if len(sys.argv) < 2:
        print("请提供Markdown文件路径作为参数")
        return

    file_path = sys.argv[1]  # Use the first command-line argument
    analyzer = MarkdownImageAnalyzer(file_path)

    # Define bucket information
    bucket = os.getenv("U_BUCKET")
    bucket_folder = os.getenv("U_BUCKET_FOLDER")
    remote_domain = os.getenv("U_REMOTE_DOMAIN")

    analyzer.upload_and_replace_images(bucket, bucket_folder, remote_domain)


if __name__ == "__main__":
    main()
