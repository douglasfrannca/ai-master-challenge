"""Dados do challenge para o Decision Gate, sem versionar o dataset bruto.

Usa data/raw/ se o arquivo já foi baixado (scripts/download_data.py); senão baixa do
Kaggle na primeira abertura (kagglehub, sem login) e o kagglehub guarda em cache.
"""

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
LOCAL_RAW = ROOT / "data" / "raw" / "social_media_dataset.csv"
DATASET = "omenkj/social-media-sponsorship-and-engagement-dataset"
CSV_NAME = "social_media_dataset.csv"
TIER_BINS = [0, 10_000, 50_000, 100_000, 500_000, np.inf]
TIER_LABELS = ["<10K", "10–50K", "50–100K", "100–500K", "500K–1M"]


def raw_path() -> Path:
    if LOCAL_RAW.exists():
        return LOCAL_RAW
    import kagglehub

    return Path(kagglehub.dataset_download(DATASET)) / CSV_NAME


def build_posts(df: pd.DataFrame) -> pd.DataFrame:
    """Colunas que o painel e o health check usam, com a faixa de seguidores já calculada."""
    out = pd.DataFrame({
        "platform": df.platform,
        "content_type": df.content_type,
        "content_category": df.content_category,
        "tier": pd.cut(df.follower_count, TIER_BINS, labels=TIER_LABELS, right=False).astype(str),
        "is_sponsored": df.is_sponsored,
        "disclosure_type": df.disclosure_type,
        "audience_age": df.audience_age_distribution,
        "audience_gender": df.audience_gender_distribution,
        "audience_location": df.audience_location,
        "creator_id": df.creator_id,
        "creator_name": df.creator_name,
        "post_date": df.post_date,
        "views": df.views.astype("int32"),
        "likes": df.likes.astype("int32"),
        "shares": df.shares.astype("int32"),
        "comments_count": df.comments_count.astype("int32"),
    })
    out["er"] = (out.likes + out.shares + out.comments_count) / out.views * 100
    for col in ["platform", "content_type", "content_category", "tier", "disclosure_type",
                "audience_age", "audience_gender", "audience_location"]:
        out[col] = out[col].astype("category")
    return out


def load_posts() -> pd.DataFrame:
    return build_posts(pd.read_csv(raw_path()))
