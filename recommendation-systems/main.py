import pandas as pd
import numpy as np


# generate dataset
np.random.seed(42)

# number of records/samples
num_samples = 1000

"""
Hotel recommender 
how many hotels can i sleep in a night 

HOTEL RECOMMENDATION
hotel_id, user_id, rating, review_count, price_per_night, distance_to_city_center, amenities_score, room_comfort_score, 
cleanliness_score, staff_friendliness_score, free_wifi, breakfast_included

"""

hotel_ids = np.arange(1, 101) # 100 unique hotels
user_ids = np.arange(1, 501) # 500 unique users


data = {
    'hotel_id': np.random.choice(hotel_ids, num_samples),
    'user_id': np.random.choice(user_ids, num_samples),
    'rating': np.random.randint(1,6), # ratings beetween 1 and 5
    'review_count': np.random.randint(1, 300, num_samples),
    'price_per_night': np.round(np.random.uniform(50, 500, num_samples),2), # price per night is between $50 to $500
    'distance_to_city_center': np.round(np.random.uniform(0.5, 20, num_samples),2), # distance to city centre between 0.5 to 20 km
    'amenities_score': np.round(np.random.uniform(1, 10, num_samples), 1), # amenities score between 1 and 10
    'room_comfort': np.round(np.random.uniform(1, 10, num_samples), 1),  # room comfort between 1 and 10
    'cleanliness_score': np.round(np.random.uniform(1, 10, num_samples), 1),  # cleanliness score between 1 and 10
    'staff_friendliness_score': np.round(np.random.uniform(1, 10, num_samples), 1),  # staff friendliness score between 1 and 10
    'free_wifi': np.random.choice([0, 1], num_samples), # free wifi (0 = No, 1 = Yes)
    'breakfast_included': np.random.choice([0, 1], num_samples),  # breakfast included (0 = No, 1 = Yes)
}

# create a data frame
df = pd.DataFrame(data)

# save to csv
path = 'recommendation-systems'
df.to_csv(path, index=False)

df.head()

# The Process
# 1. Load and process the data
# 2. Create a user-item interaction matrix
# 3. Perform SVD (Singular Value Decomposition)
# 4. Predict Ratings
# 5. Generate Recommendations

