import json

with open("catalog.json", "r", encoding="utf-8") as f:
    text = f.read().strip()

# If already valid, nothing to do
try:
    json.loads(text)
    print("catalog.json is already valid.")
    exit()
except:
    pass

# Wrap objects in an array if needed
if not text.startswith("["):
    text = "[\n" + text

if not text.endswith("]"):
    text = text + "\n]"

# Remove trailing comma before closing ]
text = text.replace(",\n]", "\n]")

# Validate
data = json.loads(text)

with open("catalog_fixed.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Fixed file saved as catalog_fixed.json")