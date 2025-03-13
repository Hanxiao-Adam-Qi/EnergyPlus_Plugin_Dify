# EnergyPlus Tools Plugin for Dify

这是一个用于 Dify 平台的 EnergyPlus 工具插件，允许用户通过 Dify 的对话界面来运行 EnergyPlus 建筑能耗模拟计算并获取结果。

## 注意，本插件需要与[EnergyPlus API](https://github.com/Hanxiao-Adam-Qi/EnergyPlus_FastAPI)项目搭配使用

## 功能特点

- 运行 EnergyPlus 模拟计算
- 获取模拟结果文件
- 支持多种结果文件格式
- 提供示例文件和天气数据文件列表
- 支持中英文双语界面

## 配置说明

需要在插件配置中设置 EnergyPlus 引擎的 URL：
- energyPlus_url: EnergyPlus 引擎的访问地址（默认：http://192.168.0.66:8000）

## 工具列表

1. **运行模拟** (run_simulation)
   - 输入：IDF文件名和天气文件名
   - 输出：运行ID和结果目录路径
   - 功能：执行 EnergyPlus 模拟计算

2. **获取特定结果文件** (get_specific_result_file)
   - 输入：运行ID和文件名
   - 输出：结果文件的下载链接
   - 功能：获取指定模拟运行中的特定结果文件

3. **获取示例文件列表** (get_examples)
   - 输出：可用的示例IDF文件列表
   - 功能：列出系统中所有可用的示例模型文件

4. **获取天气文件列表** (get_weathers)
   - 输出：可用的天气数据文件列表
   - 功能：列出系统中所有可用的天气数据文件

5. **获取所有模拟结果** (get_all_performed_simulation)
   - 输出：所有已执行的模拟运行结果列表
   - 功能：查看所有历史模拟记录

6. **获取模拟结果文件列表** (get_simulation_result_file_list)
   - 输入：运行ID
   - 输出：指定模拟运行中的所有结果文件列表
   - 功能：列出某次模拟产生的所有结果文件

