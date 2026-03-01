from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

AVAILABLE_COOKWARE = {"Spatula", "Frying Pan", "Little Pot", 
                      "Stovetop", "Whisk", "Knife", "Ladle", "Spoon"}

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search(query: str) -> str:
    results = client.search(query)
    return results

def validate_cookware(equipment: list) -> dict:
    missing = [e for e in equipment if e not in AVAILABLE_COOKWARE]
    
    return {
        "can_cook": len(missing) == 0,
        "missing": missing
    }