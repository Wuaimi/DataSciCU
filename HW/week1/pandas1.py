import pandas as pd

def main():
    file = input()
    func = input()

    data = pd.read_csv(file)
    if func == 'Q1':
        print(data.shape)
    elif func == 'Q2':
        print(data['score'].max())
    elif func == 'Q3':
        value_counts = ((data['score'] >= 80).value_counts())
        if True in value_counts:
            print(value_counts[True])
    else:
        print('No Output')

if __name__ == "__main__":
    main()