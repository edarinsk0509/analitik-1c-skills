import json, re, sys, io, glob, collections
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
root = Path.home()/".claude"/"projects"
uses = {}
tools = collections.Counter(); cmds = collections.Counter(); mcp = collections.Counter(); web = collections.Counter()
denied = []
DEN = re.compile(r"doesn't want to proceed|was rejected|denied|not allowed|blocked|Permission|классификатор|requires approval|user declined|Request interrupted", re.I)
def head(cmd):
    c = cmd.strip()
    c = re.sub(r"^(\$env:\w+\s*=\s*'[^']*';\s*)+", "", c)
    c = re.sub(r"^cd\s+[^;&]+(&&|;)\s*", "", c)
    m = re.match(r"[\"']?([^\s\"'|;&]+)", c)
    w = m.group(1) if m else c[:20]
    w = w.replace("\\", "/").split("/")[-1]
    second = c.split()[1] if len(c.split()) > 1 and w in ("git","uv","npm","python","py","claude","node","winget","pip","ant") else ""
    return (w + " " + second).strip()[:40]
for f in root.glob("*/*.jsonl"):
    for raw in open(f, encoding="utf-8", errors="replace"):
        try: e = json.loads(raw)
        except: continue
        m = e.get("message") or {}
        c = m.get("content")
        if not isinstance(c, list): continue
        for b in c:
            if b.get("type") == "tool_use":
                uses[b["id"]] = b; n = b["name"]; tools[n] += 1
                i = b.get("input", {})
                if n in ("Bash", "PowerShell"): cmds[(n, head(i.get("command", "")))] += 1
                elif n.startswith("mcp__"): mcp[n] += 1
                elif n == "WebFetch":
                    d = re.sub(r"https?://([^/]+).*", r"\1", i.get("url", "")); web[d] += 1
            if b.get("type") == "tool_result" and b.get("is_error"):
                x = b.get("content")
                if isinstance(x, list): x = " ".join(y.get("text", "") for y in x if isinstance(y, dict))
                x = str(x)
                if DEN.search(x[:400]):
                    u = uses.get(b["tool_use_id"]); inp = u and json.dumps(u.get("input", {}), ensure_ascii=False)[:220]
                    denied.append((f.parent.name, u and u["name"], inp, x[:200].replace("\n", " ")))
print("TOOLS", tools.most_common(40))
print("\nCMDS"); [print(n, k, v) for (n, k), v in cmds.most_common(90)]
print("\nMCP", mcp.most_common(40)); print("\nWEB", web.most_common(30))
print("\nDENIED", len(denied))
for d in denied: print(" |", d[0], "|", d[1], "|", d[2], "||", d[3])
