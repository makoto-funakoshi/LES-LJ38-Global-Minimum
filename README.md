# LES × GPT — LJ38 numerical benchmark reproduction (R5 and R13)

**Researcher / project author:** Makoto Funakoshi (舟越 誠) — LES collaborative research with GPT.

## 日本語

38原子の Lennard-Jones クラスター（LJ38）の既知最良エネルギーを、LES研究の2つの計算実験で数値的に再現しました。単位はLennard-Jones換算単位です。エネルギーは低いほど良くなります。

| 指標 | エネルギー |
|---|---:|
| 公開最良既知値（小数6桁） | −173.928427 |
| LES R5（fcc幾何学を利用） | −173.92842659062606 |
| LES R13（複数のFold/隣接関係ルーティング） | −173.92842657297103 |

**結論:** R5とR13の両方で公開最良既知値を数値的に再現しました。**新しい最小エネルギーの世界記録ではありません。世界最速アルゴリズムも主張しません。** 既知のfcc構造など、先行研究由来の知識を利用しています。両経路の完全な探索アルゴリズムは今回の公開セットには含めず、検証可能な最終座標と独立したエネルギー計算コードを公開します。

**誰でも再計算:** `python verify_lj38.py` （標準ライブラリのみで動作）

原子間の全703組について、LJポテンシャル `4*(r^-12 - r^-6)` を合計します。検算結果の差は数値丸めの範囲です。公開最良既知値は小数6桁に丸めた参照値であり、差の最後の桁が0ではないことは記録更新を意味しません。

## English

Two LES × GPT experiments reproduced the published best-known LJ38 cluster energy in reduced Lennard-Jones units. R5 used an FCC-lattice structural hypothesis; R13 used a multi-fold / contact-based routing experiment. The independently auditable final coordinates are provided in JSON alongside `verify_lj38.py`, which recomputes all 703 pair interactions with Python's standard library.

**This is a numerical reproduction of a known result, not a new energy world record, proof of global optimality, or demonstrated speed record.** Search-method internals are not included in this public verification package.

## Files

- `LJ38_R5_verified_structure.json` — optimized final structure R5.
- `LJ38_R13_verified_structure.json` — optimized final structure R13.
- `verify_lj38.py` — independent LJ 12–6 energy audit.
- `SHA256SUMS.txt` — file hashes.

## Prior work / baseline

- D. J. Wales, *The Cambridge Cluster Database*, LJ cluster minimum-energy structures: https://www-wales.ch.cam.ac.uk/CCD.html
- D. J. Wales and J. P. K. Doye, *Global Optimization by Basin-Hopping and the Lowest Energy Structures of Lennard-Jones Clusters Containing up to 110 Atoms*, J. Phys. Chem. A 101 (1997), 5111–5116.

**Scope:** Development runs. These two reproduced energies should not be confused with blind out-of-sample success rates or benchmarking under standardized starting conditions.
