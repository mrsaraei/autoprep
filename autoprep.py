import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.impute import SimpleImputer
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import MinMaxScaler

def load_data(input_path):
    return pd.read_csv(input_path)

def encode_categorical_data(df):
    obj_cols = df.select_dtypes(include='object').columns
    LE = preprocessing.LabelEncoder()
    df_encoded = df.copy()
    for col in obj_cols:
        df_encoded[col] = LE.fit_transform(df[col])
    return df_encoded

def normalize_data(df):
    scaler = MinMaxScaler(feature_range=(0, 1))
    return scaler.fit_transform(df)

def handle_missing_values(df):
    df.replace("?", np.nan, inplace=True)
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    return imp.fit_transform(df)

def remove_duplicates(df):
    df_deduplicated = pd.DataFrame(df).drop_duplicates()
    df_deduplicated.reset_index(drop=True, inplace=True)
    return df_deduplicated

def remove_outliers(df):
    ISF = IsolationForest(contamination=0.1)
    outliers = ISF.fit_predict(df)
    return df[outliers != -1]

def visualize_data(df):
    plt.hist(df)
    plt.xlabel('Data Value', fontsize=11)
    plt.ylabel('Data Frequency', fontsize=11)
    plt.title('Visualize the Preprocessed Data')
    plt.savefig('result/AutoPrep_Data_Distribution.tif', dpi=600)
    plt.savefig('result/AutoPrep_Data_Distribution.jpg', dpi=600)
    plt.show()
    plt.close()

def save_data(df):
    df.to_csv('result/PreprocessedData.csv', index=True)

def save_feature_name(df, output_file):
    row_names = df.columns.values.tolist()
    first_row_df = pd.DataFrame([row_names], columns=row_names)
    first_row_df.to_csv(output_file, index=False)

def preprocess_csv(input_path):
    # Load CSV-based input data
    df = load_data(input_path)

    # Convert feature names to string type
    df.columns = df.columns.astype(str)

    # Encode categorical columns
    df_encoded = encode_categorical_data(df)

    # Combine encoded data with the main DataFrame
    df_obj = df.select_dtypes(exclude='object')
    df = pd.concat([df_obj.reset_index(drop=True), df_encoded.reset_index(drop=True)], axis=1)

    # Normalize features
    df_normalized = normalize_data(df)

    # Handle missing values
    df_preprocessed = handle_missing_values(pd.DataFrame(df_normalized).fillna(method='ffill'))

    # Remove duplicates
    df_preprocessed = remove_duplicates(df_preprocessed)

    # Remove outliers
    df_preprocessed = remove_outliers(df_preprocessed)

    # Visualize the preprocessed data
    visualize_data(df_preprocessed)

    # Save the preprocessed data
    save_data(df_preprocessed)

    # Save the names of the features as a CSV file
    save_feature_name(df.iloc[:, :-1], 'result/FeatureName.csv')

    # Return the preprocessed DataFrame
    return df_preprocessed

# Main program
print("")
print("Hi there, I am Mohammadreza Saraei, who is interested in Medical AI.")
print("** This project is entitled [AutoPrep: Automated CSV Clinical Data Preprocessing].")
print("** This project has been modified on October 20, 2023.")
print("")

# Call the function with the file path as an argument
preprocessed_df = preprocess_csv('data_sample/BreastCancer.csv')

print("")
print("Thank you! The input dataset has been preprocessed and prepared.")
print("If you have any questions, please feel free to contact mrsaraei3@gmail.com.")
print("")