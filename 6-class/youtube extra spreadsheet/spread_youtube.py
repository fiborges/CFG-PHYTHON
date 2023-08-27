import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
csv_file = "youtube.csv"
df = pd.read_csv(csv_file)

# Display basic information about the DataFrame
basic_info = [["Basic Info:", ""]]  # Create a header
basic_info.extend([["Column", "Non-Null Count", "Dtype"]] + 
                  [list(row) for row in df.dtypes.reset_index().values])

# Display summary statistics for numerical columns
summary_stats = [["Summary Statistics:", ""]]  # Create a header
summary_stats.extend([["Statistic", "rank", "subscribers", "video views"]] +
                     [list(row) for row in df.describe().reset_index().values])

# Calculate the average subscribers and video views
average_subscribers = df['subscribers'].mean()
average_video_views = df['video views'].mean()

# Calculate the most common category
most_common_category = df['category'].mode()[0]

# Calculate the top 5 YouTubers with the highest subscribers
top_youtubers = df.nlargest(5, 'subscribers')[['Youtuber', 'subscribers']]

# Calculate the average uploads by channel type
average_uploads_by_type = df.groupby('channel_type')['uploads'].mean().reset_index()

# Formatting for tabulate
tablefmt = "pretty"

# Display results using tabulate
print(tabulate(basic_info, headers='firstrow', tablefmt=tablefmt))
print(tabulate(summary_stats, headers='firstrow', tablefmt=tablefmt))

print("\nAverage Subscribers:", average_subscribers)
print("Average Video Views:", average_video_views)

print("\nMost Common Category:", most_common_category)

print("\nTop YouTubers:")
print(tabulate(top_youtubers, headers='keys', tablefmt=tablefmt))

print("\nAverage Uploads by Channel Type:")
print(tabulate(average_uploads_by_type, headers='keys', tablefmt=tablefmt))

# Visualization
plt.figure(figsize=(10, 6))
average_uploads_by_type.plot(kind='bar', x='channel_type', y='uploads', color='c')
plt.title('Average Uploads by Channel Type')
plt.xlabel('Channel Type')
plt.ylabel('Average Uploads')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('nome_do_arquivo.png')  # Salva a figura em um arquivo
plt.show()

# Show the plot
plt.show()



