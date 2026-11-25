# Entrypoint for the news-image-20261125 entry (v1 page).
# The judged artifact is entry.png (1024x1024 PNG, <= 1 MiB): one front
# page — masthead "The World at Midweek" — summing up Wednesday
# 25 November 2026 in 35 stories across 7 regions — 3 illustrated
# hero panels, 8 more numbered panels, a pinned world map,
# 24 briefs and a date-check box.
# The page source is index.html; the per-story verification record is
# STORIES.md. This program copies entry.png into $MAKEFUN_OUTPUT_DIR
# (default /output) and prints a one-line dossier describing the page.
# It runs with no network, and two runs write the same bytes: the copy
# is the whole program's output.
import json
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

COMPETITION = "news-image-20261125"
DATE = "2026-11-25"
WEEKDAY = "Wednesday"
TITLE = "The World at Midweek"
STORIES = 35
ILLUSTRATED = 11
REGIONS = 7
FIELDS = 20

HEROES = [
    "Russia's own published figures put its Ukraine war dead at almost 500,000",
    "Saudi-led coalition strikes Hodeidah port; Houthis threaten Jeddah and all Saudi Red Sea ports",
    "China's Shenzhou-24 carries Muhammad Zeeshan Ali, Pakistan's first astronaut, into orbit",
]

REGIONS_COUNT = {
    "Europe": 8,
    "Middle East": 3,
    "Asia": 8,
    "Africa": 5,
    "Americas": 6,
    "Oceania": 3,
    "Global": 2,
}

NUMBERS = {
    "russian_war_dead_own_figures": 500000,
    "bangladesh_wage_rise_pct": 36,
    "bangladesh_new_minimum_taka": 17000,
    "bogor_miners_trapped": 26,
    "bogor_bodies_recovered": 3,
    "england_heat_deaths_estimate": 5200,
    "kospi_fall_pct": -6.2,
    "nikkei_fall_pct": -2.8,
    "cartagena_hostages_taken": 30,
    "gaza_shati_killed": 4,
    "blue_nile_women_girls_abducted": 28,
    "west_kordofan_killed": 13,
    "nz_cyber_losses_nzd_m": 5.9,
}


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(OUT_DIR, "entry.png")
    shutil.copyfile(src, dst)
    dossier = {
        "competition": COMPETITION,
        "date": DATE,
        "weekday": WEEKDAY,
        "title": TITLE,
        "stories": STORIES,
        "illustrated": ILLUSTRATED,
        "regions": REGIONS_COUNT,
        "fields": FIELDS,
        "heroes": HEROES,
        "numbers": NUMBERS,
        "output": dst,
        "bytes": os.path.getsize(dst),
    }
    print(json.dumps(dossier, ensure_ascii=False))


if __name__ == "__main__":
    main()
