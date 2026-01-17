from etl.extract import extract
from etl.load import load_data,load_top_20_porcent_amount
from etl.transform_values import transformation
from etl.transformation.To_20_porcento_amount import pareto_amount

def main():
    data = extract()
    data = transformation(data)
    load_data(data)
    
    pareto = pareto_amount(data)
    load_top_20_porcent_amount(pareto)
        
if __name__ == "__main__":
    main()