import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





# Sample data 
data = {
    "Date": ["2025-03-01", "2025-03-01", "2025-03-02", "2025-03-02", "2025-03-03", "2025-03-03", "2025-03-04", "2025-03-04"],
    "Product": ["Laptop", "Mouse", "Laptop", "Keyboard", "Monitor", "Mouse", "Laptop", "Keyboard"],
    "Quantity Sold": [5, 15, 3, 8, 4, 20, 6, 5],
    "Revenue ($)": [5000, 300, 3000, 800, 1200, 400, 6000, 500]
}

# Create a DataFrame and save it as a CSV file
df = pd.DataFrame(data)
df.to_csv("sales_data.csv", index=False)

print("✅ Sample CSV file 'sales_data.csv' created successfully!")


###################################


# Step 1: Load and Explore the Dataset
def load_data(filename):
    try:
        df = pd.read_csv(filename)
        print("✅ Dataset loaded successfully!")
    except FileNotFoundError:
        print("❌ Error: Dataset file not found. Please check the file path.")
        return None
    print("\n📝 First few rows of the dataset:")
    print(df.head())
    print("\n📊 Dataset Info:")
    print(df.info())
    print("\n🔍 Missing Values:")
    print(df.isnull().sum())
    df.dropna(inplace=True)  # Clean dataset
    print("\n✅ Cleaned dataset (Missing values removed).")
    return df

# Step 2: Basic Data Analysis
def analyze_data(df):
    print("\n📈 Basic Statistics:")
    print(df.describe())
    group_column = "Product"  # Change as needed
    numeric_column = "Revenue ($)"  # Change as needed
    grouped_data = df.groupby(group_column)[numeric_column].mean()
    print(f"\n🛒 Average {numeric_column} per {group_column}:")
    print(grouped_data)
    print("\n🔹 Interesting Findings:")
    print(f"- Best-selling product: {df.groupby(group_column)['Quantity Sold'].sum().idxmax()}")
    print(f"- Highest revenue day: {df.groupby('Date')['Revenue ($)'].sum().idxmax()}")

# Step 3: Data Visualization
def visualize_data(df):
    # Line chart: Time-series trends
    plt.figure(figsize=(8,5))
    df.groupby("Date")["Revenue ($)"].sum().plot(kind="line", marker="o", color="green")
    plt.title("📈 Revenue Trends Over Time")
    plt.xlabel("Date")
    plt.ylabel("Revenue ($)")
    plt.xticks(rotation=45)
    plt.show()

    # Bar chart: Comparison across categories
    plt.figure(figsize=(8,5))
    df.groupby("Product")["Revenue ($)"].mean().plot(kind="bar", color="skyblue")
    plt.title("📊 Average Revenue per Product")
    plt.xlabel("Product")
    plt.ylabel("Average Revenue ($)")
    plt.show()

    # Histogram: Distribution of numerical column
    plt.figure(figsize=(8,5))
    sns.histplot(df["Revenue ($)"], bins=10, kde=True, color="purple")
    plt.title("📉 Revenue Distribution")
    plt.xlabel("Revenue ($)")
    plt.ylabel("Frequency")
    plt.show()

    # Scatter plot: Relationship between two numerical variables
    plt.figure(figsize=(8,5))
    sns.scatterplot(x="Quantity Sold", y="Revenue ($)", data=df, color="red")
    plt.title("🔍 Relationship Between Quantity Sold & Revenue")
    plt.xlabel("Quantity Sold")
    plt.ylabel("Revenue ($)")
    plt.show()

# Main function
if __name__ == "__main__":
    filename = "sales_data.csv"  
    df = load_data(filename)
    if df is not None:
        analyze_data(df)
        visualize_data(df)