from pathlib import Path
from shutil import copy2

try:
    from util_hash import write_sha256, write_acquisition_log
except Exception:
    import hashlib, datetime
    def write_sha256(path: str) -> str:
        p = Path(path)
        out_dir = Path("data/hashes"); out_dir.mkdir(parents=True, exist_ok=True)
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        (out_dir / (p.stem + ".sha256")).write_text(h)
        return h
    def write_acquisition_log(path: str, source_slug: str, note: str = ""):
        out_dir = Path("data/hashes"); out_dir.mkdir(parents=True, exist_ok=True)
        log = out_dir / (Path(path).stem + "_acquisition_log.txt")
        ts = datetime.datetime.utcnow().isoformat() + "Z"
        log.write_text(f"timestamp_utc={ts}\nsource={source_slug}\noutput={path}\n{note}\n")

SRC = Path("ai_job_market_insights.csv")             # this file already exists at repo root
DST = Path("data/raw/ai_job_market_insights.csv")
DST.parent.mkdir(parents=True, exist_ok=True)

if not SRC.exists():
    raise SystemExit("ai_job_market_insights.csv not found at repo root.")
copy2(SRC, DST)

write_sha256(str(DST))
write_acquisition_log(str(DST),
    "kaggle:uom190346a/ai-powered-job-market-insights",
    note="Copied existing repo file into data/raw for standardized layout.")
print("Wrote", DST)
