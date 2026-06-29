#!/bin/bash

# ============================================================
# AutoDock Vina Multiple Molecular Docking Pipeline
# Description:
# Performs automated docking of multiple ligands against a
# protein receptor using AutoDock Vina.
# ============================================================

# -------------------------
# Batch Number
# -------------------------
BATCH_NUM=1

# -------------------------
# Directory Paths
# -------------------------
WORKDIR="$HOME/Desktop/IRSHA_PROJECT/docking"
CONFIG="$HOME/Desktop/IRSHA_PROJECT/vina_config.txt"

INPUT_DIR="$WORKDIR/batch${BATCH_NUM}"
OUTPUT_DIR="$WORKDIR/results/batch${BATCH_NUM}_results"

# -------------------------
# Create Output Directory
# -------------------------
mkdir -p "$OUTPUT_DIR"

cd "$WORKDIR" || {
    echo "Error: Working directory not found."
    exit 1
}

# -------------------------
# Check Configuration File
# -------------------------
if [ ! -f "$CONFIG" ]; then
    echo "Error: Configuration file not found."
    exit 1
fi

# -------------------------
# Check Ligand Folder
# -------------------------
if [ ! -d "$INPUT_DIR" ]; then
    echo "Error: Ligand folder not found."
    exit 1
fi

# -------------------------
# Read Ligands
# -------------------------
shopt -s nullglob
ligands=("$INPUT_DIR"/*.pdbqt)

if [ ${#ligands[@]} -eq 0 ]; then
    echo "No ligand files found."
    exit 1
fi

IFS=$'\n' ligands=($(printf '%s\n' "${ligands[@]}" | sort -V))
unset IFS

echo "=============================================="
echo " AutoDock Vina Multiple Docking Pipeline"
echo "=============================================="

echo "Total Ligands : ${#ligands[@]}"
echo ""

# -------------------------
# Dock Each Ligand
# -------------------------
for ligand in "${ligands[@]}"
do

    ligand_name=$(basename "$ligand" .pdbqt)

    echo "----------------------------------------"
    echo "Docking : $ligand_name"
    echo "----------------------------------------"

    vina \
        --config "$CONFIG" \
        --ligand "$ligand" \
        --out "$OUTPUT_DIR/${ligand_name}_out.pdbqt" \
        2>&1 | tee "$OUTPUT_DIR/${ligand_name}.txt"

    echo ""

done

echo "=============================================="
echo "Docking Completed Successfully."
echo "Results saved in:"
echo "$OUTPUT_DIR"
echo "=============================================="
