import random
import json

# Mock user data for the demonstration
mock_user_data = [
    {
        "user_id": 1,
        "expenses": "moderate",
        "vibe": "adventure",
        "reviews": ["Loved the hiking trails in Switzerland", "Great beach vibes in Bali"],
        "instagram_photos": ["link_to_photo1", "link_to_photo2"],
        "previous_destinations": ["Switzerland", "Bali"],
        "favorite_activities": ["hiking", "swimming"]
    },
    {
        "user_id": 2,
        "expenses": "luxury",
        "vibe": "relaxation",
        "reviews": ["Great spa experience in Thailand", "Amazing luxury stay in Maldives"],
        "instagram_photos": ["link_to_photo3", "link_to_photo4"],
        "previous_destinations": ["Thailand", "Maldives"],
        "favorite_activities": ["spa", "fine dining"]
    }
]

def get_user_data(user_id):
    """Fetch user data based on user_id."""
    user_data = next((user for user in mock_user_data if user['user_id'] == user_id), None)
    return user_data

def select_destination(user_data):
    """Select a destination based on user data."""
    # Example logic: Based on user's vibe and previous travel history, we select a destination
    possible_destinations = ["Paris", "New York", "Tokyo", "Sydney", "Rome"]
    destination = random.choice(possible_destinations)
    return destination

def generate_itinerary(user_data, destination):
    """Generate a day-wise itinerary for a user."""
    # Example itinerary generation logic based on user preferences and expenses
    activities = {
        "Paris": ["Eiffel Tower visit", "Louvre Museum", "Seine River Cruise"],
        "New York": ["Statue of Liberty", "Times Square", "Central Park"],
        "Tokyo": ["Shibuya Crossing", "Meiji Shrine", "Tokyo Skytree"],
        "Sydney": ["Sydney Opera House", "Bondi Beach", "Harbour Bridge"],
        "Rome": ["Colosseum", "Vatican Museums", "Trevi Fountain"]
    }

    itinerary = [
        {"day": 1, "activities": activities[destination][:2]},
        {"day": 2, "activities": activities[destination][1:3]},
        {"day": 3, "activities": activities[destination][:3]}
    ]
    
    return itinerary
