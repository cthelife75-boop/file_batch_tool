"""
高级用法示例
演示如何使用回调函数、多任务处理等
"""
from file_batch_tool import batch_rename, batch_watermark, batch_extract_exif
from datetime import datetime
from pathlib import Path

def custom_log_callback(msg):
    """自定义日志回调函数"""
    if msg.startswith("progress:"):
        progress = int(msg.split(":")[1])
        print(f"\r进度: [{progress}%]", end="", flush=True)
    else:
        print(f"\n{msg}")

def example_with_progress():
    """带进度回调的示例"""
    print("=" * 50)
    print("带进度回调的示例")
    print("=" * 50)
    
    test_dir = Path("test_files")
    if test_dir.exists():
        batch_rename(
            dir_path=str(test_dir),
            prefix="final_",
            log_callback=custom_log_callback
        )

def example_watermark():
    """添加水印示例"""
    print("\n" + "=" * 50)
    print("添加水印示例")
    print("=" * 50)
    
    # 文字水印
    # batch_watermark(
    #     dir_path="/path/to/images",
    #     type_="text",
    #     content="My Watermark",
    #     size=40
    # )
    print("请准备图片目录后取消注释运行")

def example_extract_exif():
    """提取EXIF示例"""
    print("\n" + "=" * 50)
    print("提取EXIF示例")
    print("=" * 50)
    
    # batch_extract_exif(
    #     dir_path="/path/to/images",
    #     output_csv="exif_data.csv"
    # )
    print("请准备图片目录后取消注释运行")

if __name__ == "__main__":
    example_with_progress()
    example_watermark()
    example_extract_exif()
