# URL Shortener API

This is a simple Django Project for url shorten code

## 🔗 Sample Request to Shorten a URL (POST)

**Endpoint:**  
`POST /api/shorten`

**Request Body (JSON):**
```json
{
  "url": "https://www.example.com/long-article"
}
## 📊 Stats Endpoint (GET)

Endpoint:
`GET /api/shorten/<short_code>`

This will:

- Retrieve the original long URL
- Increment the access count
- Return details including how many times the short URL was used

**Sample Response:**

```json
{
  "id": 1,
  "url": "https://www.example.com/long-article",
  "short_code": "abc123",
  "created_at": "2025-07-16T14:33:40Z",
  "updated_at": "2025-07-16T14:41:45Z",
  "access_count": 3
}
## 🛠️ How to Run This Project

### 1. Clone the Repository
```bash
git clone https://github.com/FurqanAthar28/Furqan-innovaxel-Athar.git
cd Furqan-innovaxel-Athar


### Virtual enviroment for shorten_url Project
python -m venv .venv
source .venv/Scripts/activate