# Imports
import re
import json
import pandas as pd

# Constants
GROUPS = ["LOC", "PERSON", "GROUP"]


# Helper functions
# NB: Posted spaCy project on NER addition to pipeline includes only train/dev
def get_split(x):
    if "-train" in x:
        return "train"
    elif "-dev" in x:
        return "dev"
    elif "-test" in x:
        return "dev"
    else:
        return None


# Process ner data
df = pd.read_csv("assets/ner/ud-ner.tsv", sep="\t")
df["split"] = df["file"].apply(lambda x: get_split(x))
df.dropna(inplace=True)
df["type"] = df["type"].apply(lambda x: x.upper().strip())
df[["start", "end"]] = df[["start", "end"]].astype(int)

# Create ner json files in splits
for split in ["train", "dev"]:
    filename = f"assets/processed/ner_{split}.json"
    df_data = df.copy()
    df_data.drop(["file"], axis=1, inplace=True)
    df_data = df_data[(df["type"].isin(groups)) & (df["split"] == split)]
    df_data.drop_duplicates(inplace=True)
    df_data = dict(tuple(df_data.groupby("text")))

    data = []

    from collections import defaultdict

    for k, v in df_data.items():
        entities = defaultdict(list)
        for item in v.iterrows():
            entities["entities"].append(
                [item[1]["start"], item[1]["end"], item[1]["type"]]
            )
        data.append([k, dict(entities)])

    json.dump(data, open(filename, "w"), indent=4)

    # Fix integer keys
    with open(filename, "r") as f:
        content = f.read()
        content = re.sub(r'"(\d+)":', r"\1:", content)
    with open(filename, "w") as f:
        f.write(content)
