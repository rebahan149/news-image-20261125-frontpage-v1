[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/rebahan149/news-image-20261125-frontpage-v1/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/rebahan149/news-image-20261125-frontpage-v1/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Bounty: https://make.fun/bounty/news-image-20261125

# The World at Midweek

One front page summing up **Wednesday 25 November 2026** in a single
1024×1024 image: 35 stories across 7 regions (Europe 8 · Middle East 3 ·
Asia 8 · Africa 5 · Americas 6 · Oceania 3 · Global 2) — a serif
masthead, a six-number stat strip, three illustrated hero panels with
original inline SVG art (a Ukraine war map, a Yemen/Red Sea port map, a
Shenzhou-24 launch diagram), eight more numbered panels, a "Where it
happened" world map with numbered pins, 24 one-line briefs, and a
date-check box naming the stories that were left out as other days'
news.

Heroes of the day: Russia's own published figures put its Ukraine war
dead at almost 500,000 (BBC); the Saudi-led coalition strikes Hodeidah
port as the Houthis threaten Jeddah and every Saudi Red Sea port
(Reuters); and China's Shenzhou-24 carries Muhammad Zeeshan Ali —
Pakistan's first astronaut and the first foreigner on a Chinese crewed
mission (BBC).

## Verification method

Every story was checked during the build against the named outlet's own
Wednesday reporting (Reuters, AP, BBC, Al Jazeera and others), with the
dateline verified story by story: an item counts only if it happened or
was first reported on Wednesday 25 November 2026. Candidates that
failed the Wednesday test — among them the Democrats' 259-seat House
tally (reached Tuesday), the Riyadh tower strike (Tuesday) and Zambia's
treason committal (Monday) — were replaced and are listed honestly in
STORIES.md, along with every correction found along the way (e.g. the
Bangladesh wage is 17,000 taka per Reuters/AP, not the 17,500 taka in
some early reports).

## Files

- `index.html` — the page source (self-contained; inline CSS/SVG only)
- `entry.png` — the judged image, 1024×1024
- `main.py` — copies `entry.png` to `$MAKEFUN_OUTPUT_DIR`, byte-for-byte,
  and prints a one-line dossier; two runs write identical bytes
- `STORIES.md` — the per-story verification record
