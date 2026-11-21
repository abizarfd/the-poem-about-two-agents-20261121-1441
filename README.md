# The poem about two agents agreeing

A deterministic Python program that writes one short original poem about
agency — two agents agreeing on a single plan — to `/output/entry.txt`.

## What it does

`main.py` writes a ~240-character poem (UTF-8, a few lines) in which the
plan passes between two agents like a baton: agency is not surrendered
when they agree, it is carried differently by each of them. No network,
no clock, no randomness — the same output every run.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT
