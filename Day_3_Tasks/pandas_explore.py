# Description: Processes a structured student dataset evaluating metrics and grouped categories via Pandas.

import pandas as pd

if __name__ == "__main__":
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
        'city': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'Chicago', 'New York', 'Chicago', 'Los Angeles', 'New York'],
        'math_score': [85, 68, 92, 78, 88, 60, 74, 95, 71, 82],
        'science_score': [90, 72, 96, 81, 84, 65, 78, 89, 73, 85],
        'english_score': [88, 75, 91, 85, 89, 70, 82, 92, 77, 80]
    }
    df = pd.DataFrame(data)
    df['total_score'] = df['math_score'] + df['science_score'] + df['english_score']

    print(df.loc[:, 'math_score':'english_score'].mean())
    print(df.loc[df['total_score'].idxmax(), 'name'])
    print(df['city'].value_counts())
    print(df[df['math_score'] > 75])

    print(df.nlargest(3, 'total_score'))