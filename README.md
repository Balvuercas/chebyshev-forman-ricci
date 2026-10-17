# An Exact Rational Invariant for Forman–Ricci Curvature on Chebyshev Toroidal Lattices

Reproduction package for the paper:

> **J. C. Alves Tabernero**, *An Exact Rational Invariant for Forman–Ricci Curvature on Chebyshev Toroidal Lattices*, Physical Review E (submitted).

## Overview

This repository contains the complete computational and symbolic verification of the paper's main results:

1. **Closed-form formula** for the mean Forman–Ricci curvature:
   ⟨κ_e⟩(λ) = −(47λ⁵ + 141λ⁴ + 156λ³ + 85λ² + 24λ + 3) / [2(4λ² + 6λ + 3)]

2. **Exact rational invariant** in the dense limit:
   I_∞ = 47/512 = 0.091796875…

3. **Geometric origin** via the ℓ∞ continuum integral:
   C_κ = −47/8, C_k = 8, I_∞ = |C_κ| / C_k² = 47/512

## Repository structure

```text
paper_chebyshev_forman/
├── README.md                                     # This file
├── LICENSE                                       # CC BY-SA 4.0
├── requirements.txt                              # Python dependencies
├── .gitignore                                    # Git ignore rules
├── paper/                                        # LaTeX source of the paper
│   ├── main.tex
│   ├── main.pdf
│   ├── references.bib
│   └── cover_letter.pdf
├── code/                                         # Python scripts
│   ├── verification_sympy.py
│   ├── continuum_integration_scipy.py
│   ├── exact_invariant_table.py
│   ├── verify_brute_force_lambda3.py
│   ├── generate_figure1.py
│   └── generate_figures.py
├── data/                                         # Numerical data
│   ├── chebyshev_invariant.csv                   # Curvature and invariant for λ = 1..8 (Table I)
│   ├── brute_force_lambda3.txt                   # Brute-force verification output for λ = 3
│   └── brute_force_verification_lambda1_8.csv    # Direct graph construction for λ = 1..8
└── figures/                                      # Figures of the paper
    ├── figure1_network.pdf
    ├── figure1_network.png
    ├── figure2_curvature.pdf
    ├── figure2_curvature.png
    ├── figure3_invariant.pdf
    └── figure3_invariant.png