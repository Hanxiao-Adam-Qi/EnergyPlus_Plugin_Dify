import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class GetAllResultsTool(Tool):
    def _invoke(self, tool_parameters: dict) -> ToolInvokeMessage:
        # 调用 FastAPI 获取 EnergyPlus 仿真结果
        energyPlus_url = self.runtime.credentials.get("energyPlus_url", "http://192.168.0.66:8000")
        api_url = f"{energyPlus_url}/get-all-results"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            return [self.create_json_message(data)]
        else:
            return [self.create_text_message(f"Failed to retrieve results: {response.text}")]
