#!/usr/bin/env python
"""Script for generation table with data/models from list.json in .md format"""
import argparse
import json


def generate_table(fn):
    with open(fn) as infile:
        data = json.loads(infile.read())

    datasets = sorted(data["corpora"].items(), key=lambda kv: kv[0])
    models = sorted(data["models"].items(), key=lambda kv: kv[0])

    print("## Datasets")
    print("| name | source | description |")
    print("|------|--------|-------------|")
    for name, other in datasets:
        if name.startswith("__testing_"):
            continue
        print("| {name} | {source} | {description} |".format(
            name=name, source=other["source"], description=other["description"]
        ))

    print("")
    print("## Models")
    print("| name | description | papers | preprocessing | parameters |")
    print("|------|-------------|------------|--------|---------------|")
    for name, other in models:
        if name.startswith("__testing_"):
            continue
        print("| {name} | {description} | {papers} | {preprocessing} | {parameters} |".format(
            name=name, description=other["description"], parameters=other.get("parameters", "-"),
            papers=other.get("papers", "-"), preprocessing=other.get("preprocessing", "-")
        ))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_file", help="Path to 'list.json' from repo")
    args = parser.parse_args()
    generate_table(args.input_file)


if __name__ == "__main__":
    main()
