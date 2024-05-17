
import pandas as pd
import numpy as np
import pytest

student_file = "data/out.csv"
solution_file = "data/SOL_test_labels.csv"

df_student = pd.read_csv(student_file)
df_solution = pd.read_csv(solution_file)

# Check if the student file has the same number of rows as the solution file
assert df_student.shape[0] == df_solution.shape[0], "Number of rows in student file does not match the number of rows in the solution file"

for i, row in df_solution.iterrows():
    assert df_student.loc[i, 'label'] == row['label'], "Mismatch in row {} between student and solution files".format(i)

corr_cols = ["toxic_y", "severe_toxic_y", "obscene_y", "threat_y", "insult_y", "identity_hate_y"]
sub_cols = ["toxic_x", "severe_toxic_x", "obscene_x", "threat_x", "insult_x", "identity_hate_x"]
tests = []
for i, row in df_solution.iterrows():
    for j in range(len(corr_cols)):
        student_val = df_student.loc[i, sub_cols[j]]
        correct_val = row[corr_cols[j]]
        tests.append((student_val, correct_val))
'''    student_toxic = df_student.loc[i, 'toxic']
    correct_toxic = row['toxic']
    tests.append((student_toxic, correct_toxic))
    student_severe_toxic = df_student.loc[i, 'severe_toxic']
    correct_severe_toxic = row['severe_toxic']
    tests.append((student_severe_toxic, correct_severe_toxic))
    student_obscene = df_student.loc[i, 'obscene']
    correct_obscene = row['obscene']
    tests.append((student_obscene, correct_obscene))
    student_threat = df_student.loc[i, 'threat']
    correct_threat = row['threat']
    tests.append((student_threat, correct_threat))
    student_insult = df_student.loc[i, 'insult']
    correct_insult = row['insult']
    tests.append((student_insult, correct_insult))
    student_identity_hate = df_student.loc[i, 'identity_hate']
    correct_identity_hate = row['identity_hate']
    tests.append((student_identity_hate, correct_identity_hate))'''


@pytest.mark.parametrize("test_input, expected", tests)
def test(test_input, expected):
    assert test_input == expected

'''def scoreChecker(df_sub, df_correct):
    check_full = pd.merge(df_sub, df_correct, how='inner', left_on = 'id', right_on = 'id')
    corr_cols = ["toxic_y", "severe_toxic_y", "obscene_y", "threat_y", "insult_y", "identity_hate_y"]
    sub_cols = ["toxic_x", "severe_toxic_x", "obscene_x", "threat_x", "insult_x", "identity_hate_x"]
    first_val = "toxic_y"
    correct = 0
    total = 0
    #print(check_full)
    for index, sub_row in check_full.iterrows():
        if sub_row[first_val] >= 0:
            total += len(corr_cols)
            for i in range(len(corr_cols)):
                if sub_row[sub_cols[i]] == sub_row[corr_cols[i]]:
                    correct += 1
    
    return correct, total, check_full'''