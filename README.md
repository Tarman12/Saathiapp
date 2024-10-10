# Saathi.app - Travel Itinerary Backend (Python Flask)

This is a backend API for generating personalized travel itineraries based on user preferences.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask server:
    ```bash
    python app.py
    ```

5. Test the API using Postman or `curl` by sending a POST request to `/generate-itinerary` with the following JSON body:
    ```json
    {
        "user_id": 1
    }
    ```

6. The API will return a destination and an itinerary based on the user data.

## Future Improvements
- Integrate with AWS RDS for storing user data.
- Implement a machine learning model to predict destinations based on trends or seasonality.
