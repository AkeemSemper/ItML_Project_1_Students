
import pandas as pd
import numpy as np
import pytest

student_file = "output/out.csv"
solution_file = "output/SOL_test_labels.csv"

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


@pytest.mark.parametrize("test_input, expected", tests)
def test(test_input, expected):
    assert test_input == expected
