import matplotlib.pyplot as plt

# Billing data for cloud services
services = {
    "EC2": 120.50,
    "S3": 45.20,
    "RDS": 90.00,
    "Lambda": 15.75,
    "CloudFront": 35.00
}

# Function to calculate total cost of services
def calculate_total_cost(services):
    total_cost = sum(services.values())
    return total_cost

# Function to calculate the percentage breakdown of costs by service
def calculate_cost_percentage(services):
    total_cost = calculate_total_cost(services)
    percentages = {service: (cost / total_cost) * 100 for service, cost in services.items()}
    return percentages

# Function to design a pie chart for cost breakdown
def plot_pie_chart(services):
    plt.figure(figsize=(8, 6))
    plt.pie(services.values(), labels=services.keys(), autopct='%1.1f%%', startangle=140)
    plt.title("Cloud Cost Breakdown by Service")
    plt.show()

# Main function to display data
def main():
    print("Cloud Cost Analysis Tool\n")
    
    # Calculate and display total cost
    total_cost = calculate_total_cost(services)
    print(f"Total Cloud Cost: ${total_cost:.2f}\n")
    
    # Calculate and display cost percentages
    cost_percentages = calculate_cost_percentage(services)
    print("Cost Breakdown by Service:")
    for service, percentage in cost_percentages.items():
        print(f"  {service}: {percentage:.2f}%")
    
    # Plot pie chart
    plot_pie_chart(services)

# Entry point of the script
if __name__ == "__main__":
    main()
