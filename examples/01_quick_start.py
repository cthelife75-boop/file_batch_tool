"""
快速入门示例
演示如何使用 file_batch_tool 库
"""
from file_batch_tool import batch_rename, batch_convert_image, batch_compress
import os
from pathlib import Path

def example_1_rename():
    """示例1：批量重命名"""
    print("=" * 50)
    print("示例1：批量重命名")
    print("=" * 50)
    
    # 创建测试目录
    test_dir = Path("test_files")
    test_dir.mkdir(exist_ok=True)
    
    # 创建一些测试文件
    for i in range(3):
        (test_dir / f"test_{i}.txt").touch()
    
    # 批量重命名
    batch_rename(
        dir_path=str(test_dir),
        prefix="processed_",
        suffix="_v1"
    )

def example_2_convert():
    """示例2：图片格式转换"""
    print("\n" + "=" * 50)
    print("示例2：图片格式转换")
    print("=" * 50)
    
    # 如果有图片目录，可以在这里测试
    # batch_convert_image(
    #     dir_path="/path/to/images",
    #     to_format="webp"
    # )
    print("请准备图片目录后取消注释运行")

def example_3_compress():
    """示例3：文件压缩"""
    print("\n" + "=" * 50)
    print("示例3：文件压缩")
    print("=" * 50)
    
    test_dir = Path("test_files")
    if test_dir.exists():
        batch_compress(
            dir_path=str(test_dir),
            output="test_files.zip"
        )

if __name__ == "__main__":
    example_1_rename()
    example_2_convert()
    example_3_compress()
