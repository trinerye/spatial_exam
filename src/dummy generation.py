import os
import pandas as pd
import random
import geopandas as gpd
from shapely.geometry import Point

os.chdir(os.path.dirname(__file__))

def load_original_dataset(file_path):
    """Load the original dataset containing coordinates and states."""
    df = pd.read_csv(file_path)
    df['state'] = df['state'].str.strip()  # Strip leading/trailing whitespaces
    return df

def count_locations_per_state(df):
    """Count the number of locations per state in the original dataset."""
    return df['state'].value_counts().to_dict()

def load_state_geometries(shapefile_path):
    """Load the state geometries from a shapefile."""
    gdf = gpd.read_file(shapefile_path)
    gdf['State_Name'] = gdf['State_Name'].str.strip().str.upper()  # Convert state names to uppercase for matching
    return gdf

def generate_random_point_within_geometry(geometry):
    """Generate a random point within a given geometry."""
    minx, miny, maxx, maxy = geometry.bounds
    while True:
        p = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
        if geometry.contains(p):
            return p

def generate_random_coordinates(state, count, state_geometries):
    """Generate random coordinates within the geometry of a given state."""
    state_geometry = state_geometries[state_geometries['State_Name'] == state.upper()].geometry.values
    if len(state_geometry) == 0:
        raise ValueError(f"No geometry found for state: {state}")
    state_geometry = state_geometry[0]
    points = [generate_random_point_within_geometry(state_geometry) for _ in range(count)]
    latitudes = [point.y for point in points]
    longitudes = [point.x for point in points]
    return latitudes, longitudes

def create_dummy_dataset(state_counts, state_geometries):
    """Create a dummy dataset with random coordinates based on state counts."""
    new_latitudes = []
    new_longitudes = []
    new_states = []

    for state, count in state_counts.items():
        print(f"Generating coordinates for state: {state}, count: {count}")
        latitudes, longitudes = generate_random_coordinates(state, count, state_geometries)
        new_latitudes.extend(latitudes)
        new_longitudes.extend(longitudes)
        new_states.extend([state] * count)
    
    return pd.DataFrame({
        'latitude': new_latitudes,
        'longitude': new_longitudes,
        'state': new_states
    })

def save_dummy_dataset(df, output_path):
    """Save the dummy dataset to a CSV file."""
    df.to_csv(output_path, index=False)

def main():
    original_dataset_path = os.path.join('..', 'in', 'datacenters_usa_clean.csv')
    shapefile_path = os.path.join('..', 'in', 'States_shapefile-shp', 'States_shapefile.shp')
    output_path = os.path.join('..', 'out', 'dummy_coordinates.csv')

    # Load the original dataset
    original_df = load_original_dataset(original_dataset_path)
    
    # Count locations per state
    state_counts = count_locations_per_state(original_df)

    # Load state geometries from shapefile
    state_geometries = load_state_geometries(shapefile_path)
    
    print(state_geometries[['State_Name']])  # Print the state names from the shapefile for debugging
    
    # Create dummy dataset
    dummy_df = create_dummy_dataset(state_counts, state_geometries)
    
    # Save the dummy dataset
    save_dummy_dataset(dummy_df, output_path)

if __name__ == "__main__":
    main()
