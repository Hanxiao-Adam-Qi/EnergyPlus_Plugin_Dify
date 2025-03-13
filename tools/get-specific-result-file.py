import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
import mimetypes

class GetSpecificResultFileTool(Tool):
    def _get_mime_type(self, filename: str) -> str:
        """根据文件名确定MIME类型"""
        # EnergyPlus 特有的文件类型映射
        energyplus_extensions = {
            '.err': 'text/plain',           # 错误日志文件
            '.end': 'text/plain',           # 结束状态文件
            '.eio': 'text/plain',           # EnergyPlus 初始化输出
            '.eso': 'text/plain',           # EnergyPlus 标准输出
            '.mtr': 'text/plain',           # 计量输出
            '.mtd': 'text/plain',           # 计量详细信息
            '.rdd': 'text/plain',           # 报告数据字典
            '.shd': 'text/plain',           # 遮阳计算结果
            '.bnd': 'text/plain',           # 边界条件
            '.dxf': 'application/dxf',      # CAD 文件
            '.svg': 'image/svg+xml',        # SVG 图形
            '.audit': 'text/plain',         # 审计文件
            '.edd': 'text/plain',           # EnergyPlus 数据字典
            '.mdd': 'text/plain',           # 计量数据字典
            '.wrl': 'model/vrml',           # VRML 文件
            '.zsz': 'text/plain',           # 区域尺寸摘要
            '.ssz': 'text/plain',           # 系统尺寸摘要
            '.csv': 'text/csv',             # CSV 输出
            '.tab': 'text/tab-separated-values', # 制表符分隔值
            '.htm': 'text/html',            # HTML 报告
            '.html': 'text/html'            # HTML 报告
        }

        # 首先检查是否是 EnergyPlus 特有的文件类型
        file_ext = '.' + filename.split('.')[-1].lower() if '.' in filename else ''
        if file_ext in energyplus_extensions:
            return energyplus_extensions[file_ext]

        # 如果不是 EnergyPlus 特有的文件类型，使用 mimetypes 模块猜测
        mime_type, _ = mimetypes.guess_type(filename)
        if mime_type:
            return mime_type

        # 如果都无法确定，返回通用的文本类型（因为大多数 EnergyPlus 输出都是文本格式）
        return 'text/plain'

    def _invoke(self, tool_parameters: dict) -> list[ToolInvokeMessage]:
        run_id = tool_parameters.get("run_id")
        file_name = tool_parameters.get("file_name")
        
        if not run_id:
            return [self.create_text_message("Missing required parameter: run_id")]
        if not file_name:
            return [self.create_text_message("Missing required parameter: file_name")]

        energyPlus_url = self.runtime.credentials.get("energyPlus_url", "http://192.168.0.66:8000")
        api_url = f"{energyPlus_url}/get-specific-result-file/{run_id}/{file_name}"
        
        try:
            response = requests.get(api_url)
            
            if response.status_code == 200:
                return [self.create_json_message(response.json())]
            else:
                return [self.create_text_message(f"Failed to get file information: {response.text}")]
        except Exception as e:
            return [self.create_text_message(f"Error occurred: {str(e)}")]