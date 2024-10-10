# Saathiapp - Travel Itinerary API

This project provides a personalized travel itinerary generation system using a Flask backend. It processes user data like preferences, past travel history, expenses, and social context to create custom itineraries for specific destinations.

## Features
- **Personalized Itineraries**: Generates itineraries based on user vibe, past travels, and social context.
- **Dynamic Destination Selection**: Suggests destinations using random or preference-based logic.
- **Modular Structure**: Separated backend and logic layers for easier scalability.

## Project Structure
Saathiapp/ │ ├── app.py # Main Flask server with route definitions ├── services/ │ ├── init.py # Empty init file for services module │ └── itinerary_service.py # Core logic for user data handling, destination selection, and itinerary generation └── data/ └── mock_user_data.json # Mock data for testing the system


## Prerequisites
Make sure you have the following installed:
- Python 3.x
- Flask (`pip install Flask`)

## Installation and Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Tarman12/Saathiapp.git
    cd Saathiapp
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the Flask server:
    ```bash
    python app.py
    ```

    The server should now be running at `http://127.0.0.1:5000`.

2. **Test the API**:
    - Use Postman or any other API testing tool.
    - **Endpoint**: `POST /generate-itinerary`
    - **URL**: `http://127.0.0.1:5000/generate-itinerary`
    - **Body** (JSON):
      ```json
      {
          "user_id": 1
      }
      ```

### Example Response

```json
{
    "destination": "Paris",
    "itinerary": [
        {
            "day": 1,
            "activities": ["Eiffel Tower visit", "Louvre Museum"]
        },
        {
            "day": 2,
            "activities": ["Louvre Museum", "Seine River Cruise"]
        },
        {
            "day": 3,
            "activities": ["Eiffel Tower visit", "Louvre Museum", "Seine River Cruise"]
        }
    ]
}



