import pandas as pd
import os
from constants.settings import OUTPUT_FILE


def save_to_excel(data):

    df = pd.DataFrame([data])

    if os.path.exists(OUTPUT_FILE):
        existing_data = pd.read_excel(OUTPUT_FILE)
        updated_data = pd.concat([existing_data, df], ignore_index=True)
        updated_data.to_excel(OUTPUT_FILE, index=False)
    else:
        df.to_excel(OUTPUT_FILE, index=False)

    print("Pomyślnie zapisano dane")

