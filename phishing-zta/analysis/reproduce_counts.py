"""Re-computes the numbers in Table 4, Figure 1 and Figure 2 of the report from the CSV files."""
import csv, collections, os
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
log = list(csv.DictReader(open(os.path.join(base, "screening/screening_log.csv"), encoding="utf-8")))
sel = list(csv.DictReader(open(os.path.join(base, "extraction/selected_studies.csv"), encoding="utf-8")))
print("Retrieved:", len(log), dict(collections.Counter(r["Database"] for r in log)))
print("Duplicates removed:", sum(r["Exclusion criterion"] == "EC5" for r in log))
s1 = [r for r in log if r["Stage 1 (title/abstract)"] == "Passed"]
print("After stage 1:", len(s1), dict(collections.Counter(r["Database"] for r in s1)))
s2 = [r for r in log if r["Stage 2 (second pass)"] == "Selected"]
print("Selected (stage 2):", len(s2), dict(collections.Counter(r["Database"] for r in s2)))
print("Exclusions by criterion:", sorted(collections.Counter(r["Exclusion criterion"] for r in log if r["Exclusion criterion"]).items()))
for col in ["Year", "Venue type", "Attack type", "Defence evaluated", "Method"]:
    print(col, sorted(collections.Counter(r[col] for r in sel).items()))
