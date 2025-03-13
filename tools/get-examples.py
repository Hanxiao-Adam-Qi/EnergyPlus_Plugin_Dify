import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class GetExamplesTool(Tool):
    def _invoke(self, tool_parameters: dict) -> ToolInvokeMessage:
        # 调用 FastAPI 获取示例 IDF 文件列表
        energyPlus_url = self.runtime.credentials.get("energyPlus_url", "http://192.168.0.66:8000")
        api_url = f"{energyPlus_url}/get-examples"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            examples = data.get("examples", [])

            # ✅ 这里转换成字符串，防止 Dify 解析错误
            if isinstance(examples, list):
                examples_str = ", ".join(examples)  # 把列表变成字符串
            else:
                examples_str = str(examples)

            return [self.create_text_message(f"Available examples: {examples_str}")]
        else:
            return [self.create_text_message(f"Failed to retrieve examples: {response.text}")]