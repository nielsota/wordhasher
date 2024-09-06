import pandas as pd
import random
import uuid

def generate_word_uuid():
    adjectives = ['silly', 'happy', 'clever', 'brave', 'shiny', 'fluffy', 'gentle', 'wild']
    nouns = ['bean', 'hammer', 'pencil', 'cloud', 'tiger', 'pizza', 'river', 'mountain']
    return f"the{random.choice(adjectives)}{random.choice(nouns)}{uuid.uuid4().hex[:6]}"

def add_word_uuid_column(df, column_name='word_uuid'):
    df[column_name] = [generate_word_uuid() for _ in range(len(df))]
    return df

# Example usage:
# df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
# df_with_uuid = add_word_uuid_column(df)
# print(df_with_uuid)
