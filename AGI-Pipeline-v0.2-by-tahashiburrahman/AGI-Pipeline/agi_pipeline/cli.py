import argparse
import json
from agi_pipeline.demo import build_demo_orchestrator

def main():
    parser = argparse.ArgumentParser(description="AGI Pipeline orchestration prototype")
    parser.add_argument("goal", help="Goal to process")
    parser.add_argument("--memory", default=".agi_pipeline/memory.sqlite3")
    args = parser.parse_args()
    result = build_demo_orchestrator(args.memory).run(args.goal)
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
