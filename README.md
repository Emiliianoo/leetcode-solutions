# leetcode-solutions

My accepted solutions to [LeetCode](https://leetcode.com) problems.

LeetCode profile: [Fishy_](https://leetcode.com/u/Fishy_/)

Solutions are uploaded automatically by [Leetcode-Sync](https://github.com/Emiliianoo/leetcode-sync), a Chrome extension I built that commits each submission as soon as LeetCode marks it **Accepted**.

## Layout

Each problem has its own folder, named with its zero-padded number and slug. Inside it there is one file per language I solved it in:

```
0001-two-sum/
  solution.cpp
  solution.py
```

Every commit message includes the problem title, runtime and memory reported by LeetCode, for example `Two Sum (0 ms, 20.4 MB)`. When I resubmit a problem in the same language, the file is overwritten and earlier versions stay in the git history, so `git log -- <folder>` shows how a solution changed over time.
