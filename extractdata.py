import pandas as pd
df = pd.read_json (r'data-Transformation/cma-artworks.db')
df.to_csv (r'data-Transformation/artworks.txt', index = False)