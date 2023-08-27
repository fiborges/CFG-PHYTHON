import csv
import statistics
import matplotlib.pyplot as plt

def read_data(file_name):
    data = []
    with open(file_name, 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data

def calculate_total_sales(data):
    sales = [int(row['sales']) for row in data]
    total = sum(sales)
    return total

def calculate_monthly_changes(data):
    sales = [int(row['sales']) for row in data]
    monthly_changes = [(sales[i] - sales[i - 1]) / sales[i - 1] * 100 for i in range(1, len(sales))]
    return monthly_changes

def calculate_yearly_total_sales(data):
    yearly_sales = {}
    for row in data:
        year = row['year']
        sales = int(row['sales'])
        if year in yearly_sales:
            yearly_sales[year] += sales
        else:
            yearly_sales[year] = sales
    return yearly_sales

def plot_monthly_changes(months, monthly_changes):
    plt.figure(figsize=(10, 6))
    plt.plot(months[1:], monthly_changes, marker='o', color='green')
    plt.xlabel('Months')
    plt.ylabel('Percentage Change')
    plt.title('Monthly Percentage Changes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid()
    plt.show()

def visualize_data(data):
    # Visualize sales data using a bar chart
    months = [row['month'] for row in data]
    sales = [int(row['sales']) for row in data]
    expenditures = [int(row['expenditure']) for row in data]
    
    plt.figure(figsize=(10, 6))
    
    # Bar chart for sales
    bars = plt.bar(months, sales, color='blue', label='Sales')
    
    # Add values on top of each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, f"{int(yval):,}$", va='bottom', ha='center', fontsize=10, color='black')
    
    # Line chart for expenditures
    plt.plot(months, expenditures, color='red', marker='o', label='Expenditures')
    
    # Add expenditure values as annotations on the line
    for i, txt in enumerate(expenditures):
        plt.annotate(f"{txt:,}$", (months[i], expenditures[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10, color='red')
    
    plt.xlabel('Months')
    plt.ylabel('Amount')
    plt.title('Monthly Sales and Expenditures Analysis')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()


def analyze_profit_loss(data):
    print("\n\033[1m\033[92mMonthly Profit/Loss Analysis:\033[0m")
    for row in data:
        month = row['month']
        sales = int(row['sales'])
        expenditure = int(row['expenditure'])
        profit_loss = sales - expenditure

        if profit_loss > 0:
            result = f"\033[1m\033[32mProfit: ${profit_loss}\033[0m"
        else:
            result = f"\033[1m\033[31mLoss: ${profit_loss}\033[0m"
        print(f"{month}: {result}")

def run():
    file_name = 'sales.csv'
    data = read_data(file_name)
    months = [row['month'] for row in data]

    total_sales = calculate_total_sales(data)
    print(f"\033[1m\033[92mTotal sales across all months:\033[0m ${total_sales}")

    average_sales = statistics.mean([int(row['sales']) for row in data])
    print(f"\033[1m\033[92mAverage monthly sales:\033[0m ${average_sales:.2f}")

    max_sale = max(data, key=lambda x: int(x['sales']))
    min_sale = min(data, key=lambda x: int(x['sales']))
    print(f"\033[1m\033[92mHighest sales:\033[0m {max_sale['month']} - ${max_sale['sales']}")
    print(f"\033[1m\033[92mLowest sales:\033[0m {min_sale['month']} - ${min_sale['sales']}")

    monthly_changes = calculate_monthly_changes(data)
    print("\n\033[1;36mMonthly changes in sales compared to previous month:\033[0m")
    for month, change in zip(months[1:], monthly_changes):
        if change > 0:
            change_info = f"\033[1m\033[32m+{change:.2f}%\033[0m"
        else:
            change_info = f"\033[1m\033[31m{change:.2f}%\033[0m"
        print(f"{month}: {change_info}")

    analyze_profit_loss(data)

    visualize_data(data)

    yearly_total_sales = calculate_yearly_total_sales(data)
    print("\n\033[1m\033[92mYearly Total Sales:\033[0m")
    for year, total_sales in yearly_total_sales.items():
        print(f"{year}: ${total_sales}")

    plot_monthly_changes(months, monthly_changes)

if __name__ == "__main__":
    run()





