#!/usr/bin/env python3

"""
==========================================================
AutoDock Vina Final CSV Generator
Author : Shubhada Khare

Description:
Extracts docking scores from AutoDock Vina log files and
generates a consolidated CSV containing:

- Batch
- Ligand
- Mode
- Binding Affinity (kcal/mol)
- RMSD Lower Bound
- RMSD Upper Bound

==========================================================
"""

import os
import csv
import re

# ----------------------------------------------------------
# Results Directory
# ----------------------------------------------------------

BASE_DIR = os.path.expanduser(
    "~/Desktop/IRSHA_PROJECT/docking/results"
)

OUTPUT_FILE = "FINAL_ALL_BATCHES.csv"

# ----------------------------------------------------------
# Locate Batch Result Folders
# ----------------------------------------------------------

batch_folders = sorted([
    folder for folder in os.listdir(BASE_DIR)
    if folder.startswith("batch") and
    os.path.isdir(os.path.join(BASE_DIR, folder))
])

all_results = []

# ----------------------------------------------------------
# Read Every Docking Log
# ----------------------------------------------------------

for batch in batch_folders:

    batch_path = os.path.join(BASE_DIR, batch)

    txt_files = sorted([
        file for file in os.listdir(batch_path)
        if file.endswith(".txt")
    ])

    for txt in txt_files:

        ligand = txt.replace(".txt", "")

        file_path = os.path.join(batch_path, txt)

        with open(file_path, "r") as file:

            for line in file:

                match = re.search(
                    r'^\s*(\d+)\s+(-?\d+\.\d+)\s+([0-9.]+)\s+([0-9.]+)',
                    line
                )

                if match:

                    mode, affinity, rmsd_lb, rmsd_ub = match.groups()

                    all_results.append([
                        batch,
                        ligand,
                        mode,
                        affinity,
                        rmsd_lb,
                        rmsd_ub
                    ])

# ----------------------------------------------------------
# Write Final CSV
# ----------------------------------------------------------

output_path = os.path.join(BASE_DIR, OUTPUT_FILE)

with open(output_path, "w", newline="") as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow([
        "Batch",
        "Ligand",
        "Mode",
        "Affinity (kcal/mol)",
        "RMSD_lb",
        "RMSD_ub"
    ])

    writer.writerows(all_results)

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("=" * 55)
print("Final CSV Generated Successfully")
print("=" * 55)
print(f"Output File : {output_path}")
print(f"Total Records : {len(all_results)}")
print("=" * 55)