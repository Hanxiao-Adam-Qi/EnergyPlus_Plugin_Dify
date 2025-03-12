import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
import mimetypes

class GetAllResultFilesTool(Tool):
    def _invoke(self, tool_parameters: dict) -> list[ToolInvokeMessage]:
        run_id = tool_parameters.get("run_id")
        if not run_id:
            return [self.create_text_message("Missing required parameter: run_id")]
        energyPlus_url = self.runtime.credentials.get("energyPlus_url", "http://192.168.0.66:8000")
        api_url = f"{energyPlus_url}/get-result-file-list/{run_id}"
        response = requests.get(api_url)
        if response.status_code == 200:
            return [self.create_json_message(response.json())]
        else:
            return [self.create_text_message(f"Failed to get result files: {response.text}")]
