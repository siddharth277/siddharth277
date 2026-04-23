import json
import re

with open("repos.json") as f:
    repos = json.load(f)

# Filter out forked repos (remove this line to include forks)
repos = [r for r in repos if not r.get("fork", False)]

repos = sorted(repos, key=lambda x: x["stargazers_count"] + x["forks_count"], reverse=True)

top = repos[:2]

content = ""
for repo in top:
    desc = repo.get("description") or ""
    content += (
        f'### [{repo["name"]}]({repo["html_url"]})\n'
        f'{desc}\n\n'
        f'![Stars](https://img.shields.io/github/stars/siddharth277/{repo["name"]}?style=flat-square) '
        f'![Forks](https://img.shields.io/github/forks/siddharth277/{repo["name"]}?style=flat-square)\n\n'
    )

with open("README.md") as f:
    readme = f.read()

new_readme = re.sub(
    r"<!--START_SECTION:top_repos-->.*?<!--END_SECTION:top_repos-->",
    f"<!--START_SECTION:top_repos-->\n{content}<!--END_SECTION:top_repos-->",
    readme,
    flags=re.DOTALL
)

with open("README.md", "w") as f:
    f.write(new_readme)

print("Done! Top repos:", [r["name"] for r in top])
