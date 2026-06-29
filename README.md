# AutoDock-Vina Multiple Docking Pipeline

An automated high-throughput molecular docking pipeline developed using **AutoDock Vina** for screening multiple ligands against a target protein receptor. This workflow performs automated docking of ligand libraries and generates a consolidated CSV file containing binding affinity and RMSD values for downstream analysis.

---

## Features

- Automated multiple ligand docking
- High-throughput virtual screening
- AutoDock Vina based docking
- Automated docking log generation
- Automatic extraction of docking scores
- Final CSV summary generation
- Simple and reproducible workflow

---

## Repository Structure

```
AutoDock-Vina-Multiple-Docking-Pipeline/
│
├── README.md
├── vina_config.txt
├── multiple_docking.sh
├── final_csv_generator.py
│
├── Protein/
│   └── sample_receptor.pdbqt
│
├── Ligands/
│   └── sample_ligand.pdbqt
│
└── Output/
```

---

## Requirements

- Ubuntu Linux
- AutoDock Vina (v1.2 or later)
- Python 3
- Bash Shell

---

## Workflow

```
Protein Preparation
        │
        ▼
Ligand Preparation
        │
        ▼
Multiple Ligand Docking
        │
        ▼
Docking Log Generation
        │
        ▼
Final CSV Generation
```

---

## Usage

### 1. Prepare the receptor

Convert the protein receptor into **PDBQT** format and place it inside the `Protein/` directory.

### 2. Prepare ligands

Convert all ligands into **PDBQT** format and place them in the docking input directory.

### 3. Edit the configuration

Update the receptor path, grid center, and grid box dimensions in:

```
vina_config.txt
```

### 4. Run molecular docking

```bash
bash multiple_docking.sh
```

### 5. Generate the final docking summary

```bash
python3 final_csv_generator.py
```

---

## Output

The workflow automatically generates:

- Docked ligand structures (`.pdbqt`)
- Docking log files (`.txt`)
- Final docking summary (`.csv`)

---

## Example Output

| Ligand | Mode | Affinity (kcal/mol) | RMSD_lb | RMSD_ub |
|---------|------|---------------------|----------|----------|
| Ligand1 | 1 | -9.7 | 0.000 | 0.000 |
| Ligand2 | 1 | -9.4 | 0.000 | 0.000 |
| Ligand3 | 1 | -8.9 | 0.000 | 0.000 |

---

## Applications

- Structure-based drug discovery
- Virtual screening
- Lead identification
- Computational medicinal chemistry
- Bioinformatics research

---

