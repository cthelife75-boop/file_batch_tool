"""
示例 1：基础批量重命名
演示如何使用 file_batch_tool 进行简单的批量重命名操作
"""
from file_batch_tool import batch_rename


def example_simple_rename():
    """简单重命名示例"""
    print("=== 示例：简单批量重命名 ===")
    
    # 重命名文件夹中的所有文件，添加前缀
    batch_rename(
        dir_path="./test_images",
        prefix="vacation_",
        find_str="img",
        replace_str="photo"
    )


def example_with_logger():
    """带自定义日志回调的示例"""
    print("\n=== 示例：自定义日志回调 ===")
    
    def custom_log(msg):
        if msg.startswith("progress:"):
            # 处理进度消息
            progress = msg.split(":")[1]
            print(f"进度: {progress}%")
        else:
            # 处理普通日志
            print(f"[LOG] {msg}")
    
    batch_rename(
        dir_path="./test_images",
        suffix="_processed",
        log_callback=custom_log
    )


if __name__ == "__main__":
    # 确保您有测试文件夹，或者修改路径为您的实际路径
    import os
    test_dir = "./test_images"
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
        print(f"已创建测试目录: {test_dir}")
        print("请在该目录中放入一些测试图片后运行示例")
    else:
        example_simple_rename()
        example_with_logger()
