# EnergyPlus API 服务

这是一个基于 FastAPI 和 Docker 的 EnergyPlus 模拟引擎 API 服务。该服务提供了一个 RESTful API 接口，允许用户远程运行 EnergyPlus 模拟计算并获取结果。

## 功能特点

- 基于 FastAPI 构建的现代化 RESTful API
- 使用 Docker 容器化部署，确保环境一致性
- 支持 EnergyPlus 24.1.0 版本
- 提供完整的模拟计算流程 API
- 支持多种结果文件格式的获取

## 系统要求

- Docker Engine 20.10+
- Docker Compose 2.0+
- 至少 4GB 可用内存
- 至少 10GB 可用磁盘空间

## 快速开始

### 1. 克隆项目

```bash
git clone <repository-url>
cd energyPlus
```

### 2. 环境配置

创建 `.env` 文件并设置必要的环境变量：

```bash
cp .env.example .env
# 编辑 .env 文件设置您的环境变量 PYTHONPATH为EnergyPlus的安装目录
```

### 3. 启动服务

使用 Docker Compose 构建并启动服务：

```bash
docker-compose up -d --build
```

服务将在 http://localhost:8000 启动

### 4. API 端点

主要的 API 端点包括：

- `POST /run-simulation`: 运行 EnergyPlus 模拟
  - 参数：`idf_file`（IDF文件名）和 `weather_file`（天气文件名）
  - 返回：运行ID和输出目录路径

- `GET /get-specific-results/{run_id}/{file_name}`: 获取特定结果文件
  - 返回：文件下载链接

- `GET /get-examples`: 获取示例输入文件列表
- `GET /get-weathers`: 获取可用的天气文件列表
- `GET /get-all-results`: 获取所有模拟结果列表