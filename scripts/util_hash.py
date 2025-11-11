from pathlib import Path
import hashlib, datetime

def write_sha256(path: str) -> str:
    p = Path(path)
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    (p.parent / (p.stem + ".sha256")).write_text(h)
    return h

def write_acquisition_log(path: str, source_slug: str, note: str = ""):
    out_dir = Path("data/hashes")
    out_dir.mkdir(parents=True, exist_ok=True)
    log = out_dir / (Path(path).stem + "_acquisition_log.txt")
    ts = datetime.datetime.utcnow().isoformat() + "Z"
    log.write_text(f"timestamp_utc={ts}\nsource={source_slug}\noutput={path}\n{note}\n")

