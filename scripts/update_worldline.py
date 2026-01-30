from datetime import datetime
import random

def update_bar(path, label, percent):
    width = int(420 * percent / 100)
    with open(path, "w", encoding="utf-8") as f:
        f.write(f'''<svg width="420" height="36" viewBox="0 0 420 36" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="420" height="36" rx="8" fill="#1a1a1a"/>
  <rect x="0" y="0" width="{width}" height="36" rx="8" fill="#ff2a2a"/>
  <text x="12" y="23" font-size="14" fill="#ffffff" font-family="JetBrains Mono, monospace">
    {label} {percent}%
  </text>
</svg>''')

# 世界线参数，随便乱来才像真的
sanity = random.randint(15, 80)
timeline = random.randint(40, 90)
baka_count = random.randint(1, 12)

update_bar("assets/status/sanity.svg", "Sanity", sanity)
update_bar("assets/status/timeline.svg", "Timeline Integrity", timeline)

with open("assets/status/baka-counter.svg", "w", encoding="utf-8") as f:
    f.write(f'''<svg width="420" height="48" viewBox="0 0 420 48" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="420" height="48" rx="10" fill="#000000"/>
  <text x="14" y="30" font-size="16" fill="#ff2a2a" font-family="JetBrains Mono, monospace">
    あんたバカ？ × {baka_count}
  </text>
</svg>''')

print("Worldline updated at", datetime.utcnow())
