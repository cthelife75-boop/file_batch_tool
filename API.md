# 📚 API 文档

> **API 说明**：本页面提供了 file_batch_tool 库的完整 API 参考文档，包括所有核心功能函数的使用方法、参数说明和示例代码。

---

## 目录
- [安装](#安装)
- [快速开始](#快速开始)
- [API 参考](#api-参考)

---

## 安装

```bash
# 从 PyPI 安装
pip install file-batch-tool

# 或从源码安装（开发模式）
git clone https://github.com/c-the-life/file_batch_tool.git
cd file_batch_tool
pip install -e .
```

## 快速开始

```python
from file_batch_tool import (
    batch_rename,
    batch_convert_image,
    batch_compress,
    batch_classify,
    batch_watermark,
    batch_modify_file_time,
    batch_extract_exif,
    batch_copy_move
)
```

---

## API 参考

### 1. 批量重命名

```python
from file_batch_tool import batch_rename

# 重命名单个文件
batch_rename(
    dir_path="/path/to/file.jpg",
    prefix="new_",
    suffix="_v2",
    find_str="old",
    replace_str="new"
)

# 重命名整个目录
batch_rename(
    dir_path="/path/to/folder",
    prefix="backup_",
    find_str="photo",
    replace_str="image"
)

# 带日志回调
def my_log(msg):
    print(msg)

batch_rename(
    dir_path="/path/to/folder",
    prefix="processed_",
    log_callback=my_log
)
```

---

### 2. 图片格式转换

```python
from file_batch_tool import batch_convert_image

# 支持格式：jpg, jpeg, png, webp
batch_convert_image(
    dir_path="/path/to/images",
    to_format="webp"
)
```

---

### 3. 文件压缩

```python
from file_batch_tool import batch_compress

batch_compress(
    dir_path="/path/to/files",
    output="/path/to/output.zip",
    exclude="txt,md"
)
```

---

### 4. 文件分类

```python
from file_batch_tool import batch_classify

# 按扩展名分类
batch_classify(
    dir_path="/path/to/files",
    mode="ext"
)

# 按日期分类
batch_classify(
    dir_path="/path/to/files",
    mode="date"
)
```

---

### 5. 添加水印

```python
from file_batch_tool import batch_watermark
from datetime import datetime

# 文字水印
batch_watermark(
    dir_path="/path/to/images",
    type_="text",
    content="© 2024",
    size=36,
    color="(255,255,255,128)"
)

# 图片水印
batch_watermark(
    dir_path="/path/to/images",
    type_="image",
    watermark_path="/path/to/logo.png",
    size=100,
    opacity=128
)
```

---

### 6. 修改文件时间

```python
from file_batch_tool import batch_modify_file_time
from datetime import datetime

target_time = datetime(2024, 1, 1, 12, 0, 0)

# 修改创建和修改时间
batch_modify_file_time(
    dir_path="/path/to/files",
    target_time=target_time,
    time_type="both"
)
```

---

### 7. 提取 EXIF

```python
from file_batch_tool import batch_extract_exif

batch_extract_exif(
    dir_path="/path/to/images",
    output_csv="/path/to/exif_data.csv"
)
```

---

### 8. 复制/移动

```python
from file_batch_tool import batch_copy_move

# 复制
batch_copy_move(
    dir_path="/path/to/source",
    target_dir="/path/to/dest",
    mode="copy"
)

# 移动
batch_copy_move(
    dir_path="/path/to/source",
    target_dir="/path/to/dest",
    mode="move",
    exclude="log"
)
```
