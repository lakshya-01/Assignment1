import pandas as pd
import matplotlib.pyplot as plt

def plot_min_temperatures(dates: list, csv_file: str) -> None:
    """
    Plots a graph between dates and the minimum temperature for each date from a CSV file.
    
    Parameters:
    - dates (list): A list of dates in the format 'YYYY-MM-DD'.
    - csv_file (str): The path to the CSV file containing temperature data.
    """
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(csv_file)
        
        # Ensure 'Timestamp' and 'Temperature' columns are present in the DataFrame
        if 'Timestamp' not in df.columns or 'Temperature' not in df.columns:
            raise ValueError("CSV file must contain 'Timestamp' and 'Temperature' columns.")
        
        # Convert 'Timestamp' to datetime
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        
        min_temperatures = []

        for date in pd.to_datetime(dates):
            # Filter the DataFrame for the given date
            date_filtered_df = df[df['Timestamp'].dt.date == date.date()]
            
            if date_filtered_df.empty:
                min_temperatures.append(None)  # Append None if no data is available for the date
                print(f"No data available for the date {date.date()}.")
            else:
                # Get the minimum temperature for the filtered date
                min_temp = date_filtered_df['Temperature'].min()
                min_temperatures.append(min_temp)
        
        # Plotting the results
        plt.figure(figsize=(10, 5))
        plt.plot(dates, min_temperatures, marker='o', linestyle='-', color='b')
        plt.xlabel('Date')
        plt.ylabel('Minimum Temperature')
        plt.title('Minimum Temperature by Date')