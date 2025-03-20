import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class GetExamplesTool(Tool):
    def _invoke(self, tool_parameters: dict) -> ToolInvokeMessage:
        # 调用 FastAPI 获取示例 IDF 文件列表
        energyPlus_url = self.runtime.credentials.get("energyPlus_url", "http://192.168.0.66:8000")
        
        file_name = tool_parameters.get("file_name")

        if not file_name:
            return [self.create_text_message("Missing required parameter: file_name")]
        
        api_url = f"{energyPlus_url}/get-specific-weather-file/{file_name}"
        
        try:
            response = requests.get(api_url)

            if response.status_code == 200:
                return [self.create_json_message(response.json())]
            else:
                return [self.create_text_message(f"Failed to get file information: {response.text}")]
        except Exception as e:
            return [self.create_text_message(f"Error occurred: {str(e)}")]