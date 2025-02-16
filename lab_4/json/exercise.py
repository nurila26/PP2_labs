import json
import os

file_path = os.path.join(os.path.dirname(__file__), "sample-data.json")

if not os.path.exists(file_path):
    raise FileNotFoundError(f"Файл '{file_path}' не найден! Убедитесь, что он находится в правильной папке.")

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

def parse_json_and_print(data):
    print("Interface Status")
    print("=" * 80)
    print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
    print("-" * 80)
    
    for item in data.get("imdata", []):
        attributes = item.get("l1PhysIf", {}).get("attributes", {})
        dn = attributes.get("dn", "")
        description = attributes.get("descr", "") 
        speed = attributes.get("speed", "") 
        mtu = attributes.get("mtu", "")
        
        print(f"{dn:<50} {description:<20} {speed:<8} {mtu:<6}")

parse_json_and_print(data)

