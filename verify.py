#!/usr/bin/env python3
"""Autonomous Claude Ops — 本書の数字を読者が自分の環境で再計測するためのスクリプト。
使い方: python3 verify.py
出力: セッション数、応答回数の中央値/平均、完全な空回りの件数と割合。
本書のすべての数字は、この種の直接計測で裏を取っている。推測値は載せない。
"""
import json, glob, os, statistics, collections

files = glob.glob(os.path.expanduser('~/.claude/projects/*/*.jsonl'))
if not files:
    print("セッション記録が見つからない: ~/.claude/projects/*/*.jsonl")
    raise SystemExit

counts = []
for f in files:
    a = 0
    try:
        for line in open(f):
            if '"type":"assistant"' in line:
                a += 1
    except OSError:
        pass
    counts.append(a)

total = len(counts)
zero = sum(1 for a in counts if a == 0)
over100 = sum(1 for a in counts if a > 100)

print(f"セッション数              : {total}")
print(f"応答回数 中央値           : {statistics.median(counts):.0f}")
print(f"応答回数 平均             : {statistics.mean(counts):.1f}")
print(f"100回超のセッション        : {over100} ({over100/total*100:.1f}%)")
print(f"完全な空回り(応答0回)      : {zero} ({zero/total*100:.1f}%)")

buckets = collections.Counter()
for a in counts:
    if a == 0: buckets['0'] += 1
    elif a <= 5: buckets['1-5'] += 1
    elif a <= 20: buckets['6-20'] += 1
    elif a <= 100: buckets['21-100'] += 1
    else: buckets['100+'] += 1
print("\n応答回数の分布:")
for k in ['0', '1-5', '6-20', '21-100', '100+']:
    print(f"  {k:>7}回: {buckets[k]:>4} セッション")
