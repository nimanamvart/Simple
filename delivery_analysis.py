import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import folium

# Load dataset (replace with actual dataset path)
df = pd.read_csv("delivery_data_finland.csv")

# Data Cleaning
df.dropna(inplace=True)
df = df[df["distance_km"] > 0]  # Remove invalid distances

# Exploratory Data Analysis (EDA)
plt.figure(figsize=(10,5))
sns.histplot(df['distance_km'], bins=20, kde=True)
plt.title('Distribution of Delivery Distances')
plt.xlabel('Distance (km)')
plt.ylabel('Count')
plt.savefig("distance_distribution.png")
plt.show()

# Create a delivery network graph
G = nx.Graph()
for _, row in df.iterrows():
    G.add_edge(row['origin'], row['destination'], weight=row['distance_km'])

# Find the shortest path between two cities
shortest_path = nx.shortest_path(G, source='Helsinki', target='Tampere', weight='weight')
print("Optimized Route:", shortest_path)

# Create a folium map
delivery_map = folium.Map(location=[60.1695, 24.9354], zoom_start=6)
for _, row in df.iterrows():
    folium.Marker([row['lat'], row['lon']], popup=row['destination']).add_to(delivery_map)
delivery_map.save("delivery_map.html")

print("Project completed. Check 'delivery_map.html' for visualization.")
