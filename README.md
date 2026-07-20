# HomeGround

A daily sports geography game: 5 questions a day, tap the world map where the moment in sports history happened, and score up to 1,000 points per question based on distance (full points inside 25 km, decaying from there). Inspired by [GeoHistory](https://geohistory.gg/).

## Features

- **Daily round** — the same 5 questions for everyone each day, drawn deterministically from the question bank by date.
- **Chalkboard map** — a hand-drawn-feel SVG world map with tap-to-guess, drag to pan, and zoom.
- **Leaderboard** — post your score under a name after full time.
- **Admin page** — passcode-gated (default `coach123`, changeable in the app). Add, edit, and delete questions; set each answer's location by tapping the map.
- Ships with 20 classic moments: the Rumble in the Jungle, the Maracanazo, the Miracle on Ice, Senna at Imola, and more.

## Run locally

```bash
npm install
npm run dev
```

## Deploy

Pushing to `main` auto-deploys to GitHub Pages via the included workflow.
One-time setup: in the repo go to **Settings → Pages → Source → GitHub Actions**.

## Storage note

`src/storage.js` backs the game with `localStorage`, so scores, questions, and the
leaderboard are **per-browser**. For a real shared leaderboard, replace that shim
with calls to a small backend (any key-value store works — the API surface is just
`get/set/delete/list`).
