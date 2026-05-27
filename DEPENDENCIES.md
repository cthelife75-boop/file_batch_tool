# 📦 依赖管理指南
=======

## 一、如何在您的项目中依赖其他项目

### 方式1：requirements.txt（推荐用于开发）

创建 `requirements.txt` 文件：

```txt
# 直接指定包名和版本
Pillow>=10.0.0
PyQt5>=5.15.0

# 或者使用精确版本
requests==2.31.0

# 从Git仓库安装
# git+https://github.com/username/repo.git@v1.0.0#egg=package-name

# 从本地目录安装
# -e ./path/to/local/package
```

安装依赖：
```bash
pip install -r requirements.txt
```

---

### 方式2：setup.py（推荐用于发布）

在 [setup.py](file:///c:/Users/LX/Desktop/filetool/file_batch_tool/setup.py#L17-L20) 中声明：

```python
setup(
    # ... 其他配置
    install_requires=[
        "Pillow>=10.0.0",
        "PyQt5>=5.15.0",
    ],
    # 可选依赖
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
        ],
        "all": [
            "Pillow>=10.0.0",
            "PyQt5>=5.15.0",
        ]
    }
)
```

---

### 方式3：pyproject.toml（现代方式）

创建 `pyproject.toml`：

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "file-batch-tool"
version = "1.1.0"
dependencies = [
    "Pillow>=10.0.0",
    "PyQt5>=5.15.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
]
```

---

## 二、如何让其他项目依赖您的项目

### 1. 发布到 PyPI（推荐）

#### 步骤1：构建包

```bash
# 安装构建工具
pip install build twine

# 构建
python -m build
```

#### 步骤2：上传到 PyPI

```bash
# 测试上传（TestPyPI）
twine upload --repository testpypi dist/*

# 正式上传
twine upload dist/*
```

#### 步骤3：其他人可以安装使用

```bash
pip install file-batch-tool
```

然后在他们的代码中：
```python
from file_batch_tool import batch_rename

batch_rename("/path/to/files", prefix="my_")
```

---

### 2. 从 Git 仓库直接安装

其他项目可以这样依赖您的项目：

```txt
# 在 requirements.txt 中
git+https://github.com/c-the-life/file_batch_tool.git@v1.1.0#egg=file-batch-tool
```

或使用 SSH：
```txt
git+ssh://git@github.com/c-the-life/file_batch_tool.git@v1.1.0#egg=file-batch-tool
```

---

### 3. 使用 GitHub Releases 发布

1. 在 GitHub 创建 Release
2. 上传构建的 `.whl` 和 `.tar.gz` 文件
3. 其他人可以从 Release 页面下载安装

---

## 三、实际案例演示

### 案例1：另一个项目依赖您的库

假设有人要做一个图片管理工具，他们可以这样做：

#### 他们的项目结构：
```
photo-manager/
├── requirements.txt
├── setup.py
└── photo_manager/
    ├── __init__.py
    └── main.py
```

#### 他们的 requirements.txt：
```txt
file-batch-tool>=1.1.0
Pillow>=10.0.0
```

#### 他们的代码（main.py）：
```python
from file_batch_tool import batch_convert_image, batch_watermark

def process_photos(input_dir, output_dir):
    # 转换格式
    batch_convert_image(input_dir, to_format="webp")
    
    # 添加水印
    batch_watermark(
        input_dir,
        type_="text",
        content="© Photo Manager"
    )

if __name__ == "__main__":
    process_photos("./photos", "./output")
```

---

### 案例2：在脚本中使用

```python
#!/usr/bin/env python3
"""
我的自动化脚本
依赖 file_batch_tool
"""
from file_batch_tool import batch_rename, batch_compress
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory>")
        return
    
    directory = sys.argv[1]
    
    # 重命名
    batch_rename(directory, prefix="auto_")
    
    # 压缩
    batch_compress(directory, output="backup.zip")

if __name__ == "__main__":
    main()
```

---

## 四、版本号规范

使用语义化版本（Semantic Versioning）：`MAJOR.MINOR.PATCH`

- **MAJOR**：不兼容的 API 变更
- **MINOR**：向下兼容的功能性新增
- **PATCH**：向下兼容的问题修正

示例：
- `1.0.0` - 首个稳定版本
- `1.1.0` - 新增功能
- `1.1.1` - 修复 bug
- `2.0.0` - 破坏性更新

---

## 五、最佳实践

1. **固定版本范围**：使用 `>=1.0.0,<2.0.0` 而不是 `==1.0.0`
2. **使用虚拟环境**：`python -m venv venv`
3. **定期更新依赖**：`pip list --outdated`
4. **记录依赖变更**：使用 `pip freeze > requirements.txt`
5. **添加类型注解**：提升代码可维护性
