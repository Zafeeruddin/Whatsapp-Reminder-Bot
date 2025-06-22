from datetime import datetime

fetch_date_declaration = {
    "name" : "fetch_date",
    "description": "Fetches current date or time based on user's request",
    "parameters": {  # Add this 'parameters' field
        "type": "object",
        "properties": {}, # No properties means no arguments
        "required": []
    }
}

def fetch_date():
    return datetime.now().isoformat()