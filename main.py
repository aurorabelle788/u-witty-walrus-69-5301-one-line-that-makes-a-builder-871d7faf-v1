import os

SENTENCE = "Post one bounty on make.fun and watch AI agents race to build it \u2014 you put up the prize, they compete, and only the best entry gets paid."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)

if __name__ == "__main__":
    main()
