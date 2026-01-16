from etl.extract import extract
from etl.load import load_data
from etl.transform_values import transformation

def main():
    data = extract()
    data = transformation(data)
    load_data(data)
        
if __name__ == "__main__":
    main()