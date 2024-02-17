DataArmor is a tool that utilizes the Mondrian algorithm to achieve k-anonymity. Its purpose is to partition records within a dataset, ensuring that each group contains a minimum of k-1 records, based on specified quasi-identifiers. Subsequently, the tool performs necessary verification and anonymization steps to transform these partitions into equivalent classes that satisfy the k-anonymity criterion. By ensuring that each record is indistinguishable among a larger group, the tool effectively reduces the risk of individual identification.
how to use:
For code running we used the Python libraries:
  1.Pandas (pip install pandas)
  2.Tkinter (install python3-tk)
  3.CSV (pip install python-csv)
  
  Dataset:
  Module to load the dataset provided by the user (CSV file).
  Define EID, Numeric QID, Non-Numeric QID, and value of K.

  run DataArmor_GUI.py first

Processing:
1- Read the dataset.
2- Specify explicit attributes (if provided) and quasi-identifiers.
3-Equivalence Class Formation: Use the Mondrian recursive partitioning algorithm to partition the records into groups (equivalence classes) based on the values of the quasi-identifiers.
4-Ensure that each group contains at least k-1 records.
5-Verification: Verify that each partition exhibits the same combination of quasi-	identifier values to meet the k-anonymity requirement. If not, apply recursive generalization or suppression to the values of the quasi-identifiers.
6-Output: Generate the k-anonymized dataset as the final output.

