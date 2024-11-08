import pandas as pd
import os

def main():
    # หา path ของไฟล์ scores_student.csv โดยอัตโนมัติ
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'scores_student.csv')
    print(file_path)
    df = pd.read_csv(file_path)
    
    func = input("Enter function (Q1, Q2, Q3): ")
    
    if func == 'Q1':
        # Return the shape of the dataframe
        return df.shape
    elif func == 'Q2':
        # Return the maximum score
        return df['score'].max()
    elif func == 'Q3':
        # Count rows where score >= 80
        return df[df['score'] >= 80].shape[0]
    else:
        # Invalid input
        return "No output"

if __name__ == "__main__":
    output = main()
    print(output)
