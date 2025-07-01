"""
Chain Latency Tracker — анализ временных задержек между блоками в сети Bitcoin.
"""

import requests
import time

API = "https://blockstream.info/api/blocks"
BLOCK_COUNT = 10

def fetch_recent_blocks(n=BLOCK_COUNT):
    r = requests.get(API)
    r.raise_for_status()
    return r.json()[:n]

def analyze_delays(blocks):
    delays = []
    print(f"
⛓️ Chain Latency Tracker: последние {len(blocks)} блоков
")
    for i in range(1, len(blocks)):
        t1 = blocks[i-1]["timestamp"]
        t2 = blocks[i]["timestamp"]
        delta = t1 - t2
        delays.append(delta)
        print(f"Блок {blocks[i-1]['height']} → {blocks[i]['height']}: задержка {delta} сек")
        if delta > 900:
            print("⚠️ Задержка более 15 минут — возможно замедление сети!")
    avg = sum(delays) / len(delays)
    print(f"
📊 Средняя задержка: {avg:.1f} сек")

def main():
    try:
        blocks = fetch_recent_blocks()
        analyze_delays(blocks)
    except Exception as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    main()
