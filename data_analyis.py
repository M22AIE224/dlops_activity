import pandas as pd
import matplotlib.pyplot as plt

output_folder = 'plots'

def load_data(file_path):
    """Load data from a CSV file."""
    try:
        data = pd.read_excel(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def analyze_data(data):
    """Perform basic data analysis."""
    if data is not None:
        # Display summary statistics
        print("Summary Statistics:")
        print(data.describe())

        # Plot histograms for numeric columns
        print("Plotting Histograms:")
        for col in data.select_dtypes(include=['int', 'float']):
            data[col].plot(kind='hist', bins=10)
            plt.title(col)
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.savefig(f'{output_folder}/histogram_{col}.png', )
            #plt.show()
            plt.close()

        # Plot bar plot for the class label (string type)
        class_label_counts = data['Class'].value_counts()
        class_label_counts.plot(kind='bar')
        plt.title('Class Label Distribution')
        plt.xlabel('Class Label')
        plt.ylabel('Count')
        plt.savefig(f'{output_folder}/class_label.png', )
        plt.close()
        #plt.show()


def findMissingData(data):
    df = pd.DataFrame(data)

    # Finding columns with missing values
    columns_with_missing_values = df.columns[df.isnull().any()].tolist()
    return columns_with_missing_values



def main():
    print("Starting the Data Processing")
    file_path = "DryBeanDataset\Dry_Bean_Dataset.xlsx" #("Enter the path to the CSV file: ")
    
    data = load_data(file_path)
    columns_with_missing_values = findMissingData(data)
    print("List of Column with Missing Values: - ", columns_with_missing_values)
    analyze_data(data)

if __name__ == "__main__":
    main()
