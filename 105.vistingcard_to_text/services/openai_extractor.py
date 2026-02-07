import json
import base64
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)

def image_to_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def extract_visiting_card(image_path: str) -> dict:
    image_base64 = image_to_base64(image_path)

    prompt = """
Extract ONLY visible text from the visiting card.

Return STRICT JSON:
{
  "Organization Name": null,
  "Person Name": null,
  "Contact Number": null,
  "Address": null,
  "Email ID": null,
  "Website": null
}
"""

    message = HumanMessage(
        content=[
            {"type": "text", "text": prompt},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{image_base64}"
                }
            }
        ]
    )

    response = llm.invoke([message])

    raw = response.content
    print("🔍 RAW OPENAI RESPONSE:", raw)

    # ✅ STRIP MARKDOWN SAFELY
    cleaned = raw.strip()

    if cleaned.startswith("```"):
        cleaned = cleaned.replace("```json", "")
        cleaned = cleaned.replace("```", "")
        cleaned = cleaned.strip()

    print("🧹 CLEANED JSON:", cleaned)

    data = json.loads(cleaned)

    # ✅ Fix multiple emails
    if data.get("Email ID") and " " in data["Email ID"]:
        data["Email ID"] = data["Email ID"].split()[0]

    print("✅ FINAL RETURN DATA:", data)
    return data
