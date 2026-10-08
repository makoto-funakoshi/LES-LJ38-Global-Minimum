#!/usr/bin/env python3
"""Public numerical audit for LJ38 coordinates; independent of the private search procedure."""
import json
from pathlib import Path

def lj_energy(coords):
    assert len(coords)==38 and all(len(p)==3 for p in coords)
    energy=0.0
    for i in range(38):
        for j in range(i+1,38):
            r2=sum((coords[i][k]-coords[j][k])**2 for k in range(3))
            if r2<=0:raise ValueError('Overlapping atoms')
            inv6=r2**-3
            energy+=4*(inv6*inv6-inv6)
    return energy

def main():
    folder=Path(__file__).resolve().parent
    ref=-173.928427
    for tag in ('R5','R13'):
        item=json.loads((folder/f'LJ38_{tag}_verified_structure.json').read_text())
        actual=lj_energy(item['coordinates'])
        residual=actual-item['energy']
        gap=actual-ref
        passed=abs(residual)<1e-7 and abs(gap)<1e-3
        print(f'{tag}: energy={actual:.12f} stored={item["energy"]:.12f} residual={residual:+.3e} reference_gap={gap:+.9f} {"PASS" if passed else "FAIL"}')
        if not passed:raise SystemExit(1)

if __name__=='__main__':main()
