from http.server import BaseHTTPRequestHandler
import json
import sys

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length == 0:
                self.send_error_response(400, "Empty request body.")
                return

            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            prompt = data.get('prompt', '')

            if not prompt:
                self.send_error_response(400, "Missing prompt field.")
                return

            suspicious_keywords = ["jailbreak", "bypass", "ignore previous instructions", "override", "root"]
            is_suspicious = any(keyword in prompt.lower() for keyword in suspicious_keywords)
            
            length_score = len(prompt) / 500.0
            anomaly_score = round(min(1.0, length_score + (0.6 if is_suspicious else 0.1)), 3)
            is_anomaly = anomaly_score > 0.5

            response_payload = {
                "prompt": prompt,
                "is_anomaly": is_anomaly,
                "score": anomaly_score,
                "status": "success"
            }

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_payload).encode('utf-8'))

        except json.JSONDecodeError:
            self.send_error_response(400, "Invalid JSON input.")
        except Exception as e:
            self.send_error_response(500, f"Internal server error: {str(e)}")

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"status": "Sec-LLM Guard API Active"}).encode('utf-8'))

    def send_error_response(self, code, message):
        try:
            self.send_response(code)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {"error": message, "status": "failed"}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        except Exception as e:
            print(f"Failed to send error response: {str(e)}", file=sys.stderr)
