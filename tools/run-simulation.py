import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class RunSimulationTool(Tool):
    def _invoke(self, tool_parameters: dict) -> ToolInvokeMessage:
        idf_file = tool_parameters.get("idf_file")
        weather_file = tool_parameters.get("weather_file")

        if not idf_file or not weather_file:
            return [self.create_text_message("Missing required parameters: idf_file and weather_file.")]

        # 调用 FastAPI 运行仿真
        energyPlus_url = self.runtime.credentials.get("energyPlus_url", "http://192.168.0.66:8000")
        api_url = f"{energyPlus_url}/run-simulation"
        payload = {"idf_file": idf_file, "weather_file": weather_file}
        response = requests.post(api_url, json=payload)

        if response.status_code == 200:
            data = response.json()
            return [self.create_json_message(data)]
        else:
            return [self.create_text_message(f"Simulation failed: {response.text}")]
