#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reproduce Table I of the paper: mean curvature and invariant for lambda = 1..8.

Author: Juan Carlos Alves Tabernero
License: CC BY-SA 4.0
"""

import os
import csv

# Ensure output directory exists
os.makedirs('data', exist_ok=True)


def mean_triangles(lam):
    total = 0
    n_edges = 0
    for dx in range(-lam, lam + 1):
        for dy in range(-lam, lam + 1):
            for dz in range(-lam, lam + 1):
                if (dx, dy, dz) == (0, 0, 0):
                    continue
                if max(abs(dx), abs(dy), abs(dz)) > lam:
                    continue
                s = ((2*lam + 1 - abs(dx)) *
                     (2*lam + 1 - abs(dy)) *
                     (2*lam + 1 - abs(dz))) - 2
                total += max(0, s)
                n_edges += 1
    return total / n_edges


def main():
    rows = []
    for lam in range(1, 9):
        k = (2*lam + 1)**3 - 1
        tri = mean_triangles(lam)
        kappa = 4 - 2*k + 3*tri
        I = abs(kappa) * lam**3 / k**2
        rows.append((lam, k, tri, kappa, I))
        print(f"lambda={lam}: k={k}, <tri>={tri:.4f}, "
              f"<kappa>={kappa:.4f}, I={I:.6f}")

    with open('data/chebyshev_invariant.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['lambda', 'k', 'triangles', 'kappa', 'I'])
        for row in rows:
            w.writerow(row)

    print("\nCSV saved to data/chebyshev_invariant.csv")


if __name__ == "__main__":
    main()