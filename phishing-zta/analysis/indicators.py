"""Minimal indicator coder for Part 2 (Table 9 of the report).
Input : data/samples/samples.csv with columns
        sample_id, from_display, from_address, subject, body, link_text, link_target   (all DEFANGED)
Output: data/samples/coded_samples.csv and the prevalence f_i = n_i / N (Equation 5)."""
import csv, re, sys
from levenshtein import similarity

URGENT = re.compile(r"urgent|immediately|within \d+ hours|suspend|expire|final notice|verify now|action required", re.I)
GENERIC = re.compile(r"dear (user|customer|client|member)", re.I)
BRANDS = ["microsoft", "paypal", "google", "amazon", "apple", "uefa", "dhl"]

def domain(addr):
    return addr.split("@")[-1].lower().strip("<> ")

def host(url):
    url = url.replace("hxxp", "http").replace("[.]", ".")
    m = re.match(r"https?://([^/]+)", url)
    return m.group(1).lower() if m else ""

def label(domain_name):
    parts = domain_name.split(".")
    return parts[-2] if len(parts) >= 2 else domain_name

def code(row):
    d, h = domain(row["from_address"]), host(row["link_target"])
    lab = label(d)
    best = max((similarity(lab, b), b) for b in BRANDS)
    return {
        "urgency": bool(URGENT.search(row["subject"] + " " + row["body"])),
        "generic_greeting": bool(GENERIC.search(row["body"])),
        "sender_mismatch": any(b in row["from_display"].lower() and b not in d for b in BRANDS),
        "lookalike_domain": best[0] >= 0.8 and lab != best[1],
        "lookalike_score": round(best[0], 2),
        "link_target_differs_from_sender": bool(h) and label(h) != lab,
        "link_text_mismatch": bool(row["link_text"]) and host(row["link_text"]) not in ("", h),
    }

if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "../data/samples/samples.csv"
    rows = list(csv.DictReader(open(src, encoding="utf-8")))
    coded = [{**r, **code(r)} for r in rows]
    n = len(coded)
    if n:
        out = src.replace("samples.csv", "coded_samples.csv")
        with open(out, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(coded[0].keys())); w.writeheader(); w.writerows(coded)
        for k in ["urgency", "generic_greeting", "sender_mismatch", "lookalike_domain",
                  "link_target_differs_from_sender", "link_text_mismatch"]:
            c = sum(x[k] for x in coded); print(f"{k}: {c}/{n} = {c/n:.2f}")
