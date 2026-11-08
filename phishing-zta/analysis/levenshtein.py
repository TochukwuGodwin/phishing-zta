"""Normalised Levenshtein similarity used for lookalike-domain scoring (Equation 6 in the report).
s(a, b) = 1 - d_L(a, b) / max(|a|, |b|)"""

def levenshtein(a: str, b: str) -> int:
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]

def similarity(a: str, b: str) -> float:
    if not a and not b:
        return 1.0
    return 1 - levenshtein(a, b) / max(len(a), len(b))

if __name__ == "__main__":
    # worked example from the report (Table 10): d_L = 1, s = 1 - 1/9 = 0.89
    print(levenshtein("micr0soft", "microsoft"), round(similarity("micr0soft", "microsoft"), 2))
