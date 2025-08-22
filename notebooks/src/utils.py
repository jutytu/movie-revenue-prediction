import pandas as pd
import os

def split_csv(input_path, output_dir, base_name, chunk_size=1000):
    """
    Split a large CSV into multiple smaller CSVs.
    
    Parameters:
        input_path (str): Path to the original CSV file.
        output_dir (str): Directory to save split parts.
        base_name (str): Base name for split files (e.g., "credits_split").
        chunk_size (int): Number of rows per chunk.
    """
    os.makedirs(output_dir, exist_ok=True)
    df_iter = pd.read_csv(input_path, chunksize=chunk_size)
    
    for i, chunk in enumerate(df_iter):
        output_path = os.path.join(output_dir, f"{base_name}_part{i+1}.csv")
        chunk.to_csv(output_path, index=False)
        print(f"Saved {output_path} ({len(chunk)} rows)")

# split_csv(r"C:\Users\Ja\OneDrive\Dokumenty\Materiały\DA\Project Movies\tmdb_5000_credits.csv",
#           r"C:\Users\Ja\OneDrive\Dokumenty\Materiały\DA\Project Movies",
#           'tmdb_5000_credits', 1000)

import ast

def parse_names(x):
    try:
        data = ast.literal_eval(x)
        return [d['name'] for d in data]
    except:
        return []

def get_director(x):
    try:
        data = ast.literal_eval(x)
        for d in data:
            if d.get('job') == 'Director':
                return d['name']
    except:
        return None