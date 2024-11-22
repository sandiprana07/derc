from data_processing import load_data, preprocess_data

def main():
    data = load_data("data/dataset.csv")
    processed_data = preprocess_data(data)
    print(processed_data)

if __name__ == "__main__":
    main()
