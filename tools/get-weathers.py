import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class GetWeathersTool(Tool):
    def _invoke(self, tool_parameters: dict) -> list[ToolInvokeMessage]:
        energyPlus_url = self.runtime.credentials.get("energyPlus_url", "http://192.168.0.66:8000")
        api_url = f"{energyPlus_url}/get-weathers"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            weathers = data.get("weathers", [])

            # ✅ 这里转换成字符串，防止 Dify 解析错误
            if isinstance(weathers, list):
                weathers_str = ", ".join(weathers)  # 把列表变成字符串
            else:
                weathers_str = str(weathers)

            return [self.create_text_message(f"Available weather files: {weathers_str}")]
        else:
            return [self.create_text_message(f"Failed to retrieve weathers: {response.text}")]
