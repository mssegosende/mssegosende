#!/usr/bin/env python3
"""Generates the GitHub stats cards for the profile README (light and dark SVGs).

Runs in a GitHub Action once a day. Reads real data from the GitHub GraphQL API.
Env: GH_TOKEN (a token; a personal token also counts private repos), GH_USER (the username).
Writes: assets/stats/stats.svg and assets/stats/languages.svg (each holds the light and dark card)
Only the Python standard library is used, so the workflow needs no installs.
"""
import json
import os
import sys
import urllib.request
from html import escape

QUERY = """
query($login: String!) {
  user(login: $login) {
    name
    login
    repositories(ownerAffiliations: OWNER, isFork: false, first: 100) {
      nodes {
        stargazerCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
    contributionsCollection {
      totalCommitContributions
      totalPullRequestContributions
      totalIssueContributions
    }
    repositoriesContributedTo(first: 1, contributionTypes: [COMMIT, ISSUE, PULL_REQUEST, REPOSITORY]) {
      totalCount
    }
  }
}
"""

THEMES = {
    "light": {"title": "#0969DA", "text": "#1F2328", "muted": "#59636E", "border": "#D0D7DE", "track": "#EAEEF2"},
    "dark": {"title": "#58A6FF", "text": "#E6EDF3", "muted": "#9198A1", "border": "#30363D", "track": "#21262D"},
}
FONT = "'Segoe UI', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"
W, H = 450, 200

ICONS = {
    "star": "M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Z",
    "commit": "M11.93 8.5a4.002 4.002 0 0 1-7.86 0H.75a.75.75 0 0 1 0-1.5h3.32a4.002 4.002 0 0 1 7.86 0h3.32a.75.75 0 0 1 0 1.5Zm-1.43-.75a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z",
    "pr": "M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354Z",
    "issue": "M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z",
    "repo": "M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z",
}


def fetch(user, token):
    body = json.dumps({"query": QUERY, "variables": {"login": user}}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", data=body, headers={
        "Authorization": f"bearer {token}", "Content-Type": "application/json", "User-Agent": "profile-stats"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    if data.get("errors"):
        sys.exit(f"GraphQL errors: {data['errors']}")
    return data["data"]["user"]


def summarize(u):
    repos = u["repositories"]["nodes"]
    cc = u["contributionsCollection"]
    langs = {}
    for repo in repos:
        for e in repo["languages"]["edges"]:
            name = e["node"]["name"]
            size, color = langs.get(name, (0, e["node"]["color"] or "#8B949E"))
            langs[name] = (size + e["size"], color)
    total = sum(s for s, _ in langs.values()) or 1
    top = sorted(langs.items(), key=lambda kv: -kv[1][0])[:6]
    return {
        "name": u["name"] or u["login"],
        "rows": [
            ("star", "Total stars earned", sum(r["stargazerCount"] for r in repos)),
            ("commit", "Commits (last year)", cc["totalCommitContributions"]),
            ("pr", "Pull requests (last year)", cc["totalPullRequestContributions"]),
            ("issue", "Issues (last year)", cc["totalIssueContributions"]),
            ("repo", "Contributed to (last year)", u["repositoriesContributedTo"]["totalCount"]),
        ],
        "langs": [(n, round(100 * s / total, 1), c) for n, (s, c) in top],
    }


def frame(t, title, inner):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(title)}">'
            f'<title>{escape(title)}</title>'
            f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="6" fill="none" stroke="{t["border"]}"/>'
            f'<text x="24" y="38" font-family="{FONT}" font-size="17" font-weight="600" fill="{t["title"]}">{escape(title)}</text>'
            f"{inner}</svg>")


def stats_svg(s, t):
    rows = ""
    for i, (icon, label, value) in enumerate(s["rows"]):
        y = 70 + i * 26
        rows += (f'<g transform="translate(24 {y - 12})"><path d="{ICONS[icon]}" fill="{t["muted"]}"/></g>'
                 f'<text x="50" y="{y}" font-family="{FONT}" font-size="14" fill="{t["text"]}">{escape(label)}:</text>'
                 f'<text x="{W - 24}" y="{y}" text-anchor="end" font-family="{FONT}" font-size="14" font-weight="600" fill="{t["text"]}">{value:,}</text>')
    return frame(t, f"{s['name']}'s GitHub stats", rows)


def langs_svg(s, t):
    langs = s["langs"]
    if not langs:
        inner = f'<text x="24" y="100" font-family="{FONT}" font-size="14" fill="{t["muted"]}">No code in repositories yet.</text>'
        return frame(t, "Most used languages", inner)
    bar, x, bw = "", 24.0, W - 48
    for _, pct, color in langs:
        w = bw * pct / 100
        bar += f'<rect x="{x:.2f}" y="56" width="{w:.2f}" height="8" fill="{color}"/>'
        x += w
    legend = ""
    for i, (name, pct, color) in enumerate(langs):
        cx, cy = 24 + (i % 2) * 205, 98 + (i // 2) * 30
        legend += (f'<circle cx="{cx + 5}" cy="{cy - 4}" r="5" fill="{color}"/>'
                   f'<text x="{cx + 16}" y="{cy}" font-family="{FONT}" font-size="13" fill="{t["text"]}">{escape(name)}</text>'
                   f'<text x="{cx + 190}" y="{cy}" text-anchor="end" font-family="{FONT}" font-size="12" fill="{t["muted"]}">{pct}%</text>')
    clip = f'<clipPath id="r"><rect x="24" y="56" width="{bw}" height="8" rx="4"/></clipPath>'
    return frame(t, "Most used languages", f'<defs>{clip}</defs><rect x="24" y="56" width="{bw}" height="8" rx="4" fill="{t["track"]}"/><g clip-path="url(#r)">{bar}</g>{legend}')

def themed(light, dark):
    """One SVG that holds both cards and shows the one that matches the reader's theme."""
    dark = dark.replace('id="r"', 'id="r-dark"').replace("url(#r)", "url(#r-dark)")
    style = ("<style>.dark{display:none}"
             "@media (prefers-color-scheme: dark){.light{display:none}.dark{display:inline}}</style>")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{style}'
            + light.replace("<svg ", '<svg class="light" ', 1)
            + dark.replace("<svg ", '<svg class="dark" ', 1) + "</svg>")

def write_all(summary, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    with open(f"{out_dir}/stats.svg", "w", encoding="utf-8") as f:
        f.write(themed(stats_svg(summary, THEMES["light"]), stats_svg(summary, THEMES["dark"])))
    with open(f"{out_dir}/languages.svg", "w", encoding="utf-8") as f:
        f.write(themed(langs_svg(summary, THEMES["light"]), langs_svg(summary, THEMES["dark"])))

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "assets/stats"
    if os.environ.get("STATS_FIXTURE"):  # local test only
        user = json.load(open(os.environ["STATS_FIXTURE"], encoding="utf-8"))
    else:
        user = fetch(os.environ["GH_USER"], os.environ["GH_TOKEN"])
    write_all(summarize(user), out)
    print("stats cards written to", out)
