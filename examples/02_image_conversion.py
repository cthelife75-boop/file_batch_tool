"""
示例 2：图片格式转换
演示如何批量转换图片格式
"""
from file_batch_tool import batch_convert_image


def example_convert_to_webp():
    """转换为 WebP 格式（推荐用于网页）"""
    print("=== 示例：批量转换为 WebP ===")
    
    batch_convert_image(
        dir_path="./photos",
        to_format="webp"
    )


def example_convert_to_jpg():
    """转换为 JPG 格式"""
    print("\n=== 示例：批量转换为 JPG ===")
    
    batch_convert_image(
        dir_path="./photos",
        to_format="jpg"
    )


def example_single_file():
    """转换单个文件"""
    print("\n=== 示例：转换单个文件 ===")
    
    batch_convert_image(
        dir_path="./photos/photo.png",
        to_format="jpg"
    )


if __name__ == "__main__":
    import os
    test_dir = "./photos"
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
        print(f"已创建测试目录: {test_dir}")
        print("请在该目录中放入一些图片后运行示例")
    else:
        example_convert_to_webp()
