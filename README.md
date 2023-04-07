<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: la_core_cltk_md

Code required to train spaCy-compatible md core model for Latin, i.e pipeline with POS tagger, morphologizer, lemmatizer, dependency parser, and NER trained on all available Latin UD treebanks, i.e. Perseus, PROIEL, ITTB, UDante, and LLCT (see below). The model contains floret vectors trained on Wikipedia, Oscar, and UD data. NER is based on custom tagged data based on tagger output and manual annotation; this data is included in `assets/local/ud-ner.tsv`. Note also that a sm model (i.e. without vectors) is trained in the same pipeline as are dep models (i.e. with NER component).

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `assets` | Download assets |
| `preprocess` | Convert different UD treebanks so that they use shared formatting, feature defs, etc. |
| `convert` | Convert the data to spaCy's format |
| `norm-corpus` | Convert norm attribute to u-v and i-j norm |
| `extract-wikipedia` | Convert Wikipedia XML to JSONL with wikiextractor |
| `tokenize-wikipedia` | Tokenize and sentencize Wikipedia |
| `tokenize-oscar` | Tokenize and sentencize OSCAR dataset |
| `tokenize-ud` | Tokenize and sentencize UD; following wikipedia/oscar pattern |
| `create-input` | Concatenate tokenized input texts |
| `train-floret-vectors` | Train floret vectors |
| `load-vectors` | Load floret vectors |
| `init-labels` | Initialize labels for components |
| `train-sm` | Train sm tagger/parser/etc. on Latin UD treebanks |
| `train` | Train md tagger/parser/etc. on Latin UD treebanks |
| `evaluate-sm` | Evaluate sm model on the test data and save the metrics |
| `evaluate` | Evaluate md model on the test data and save the metrics |
| `convert-ner` | Convert the NER data to spaCy's binary format |
| `create-ner-config` | Create a new config with an NER pipeline component |
| `train-ner-sm` | Train the NER model for the sm model |
| `train-ner-md` | Train the NER model for the md model |
| `assemble-sm-core` | Assemble sm core model, i.e. add NER component to dep model |
| `assemble-md-core` | Assemble md core model, i.e. add NER component to dep model |
| `assemble-meta` | Assemble meta.json files so that all metrics are included |
| `package-sm-dep` | Package the trained sm dep model |
| `package-sm-core` | Package the trained sm core model |
| `package-md-dep` | Package the trained md dep model |
| `package-md-core` | Package the trained md core model |
| `document` | Document core_cltk_md |
| `clean` | Remove intermediate files |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `assets` &rarr; `preprocess` &rarr; `convert` &rarr; `norm-corpus` &rarr; `extract-wikipedia` &rarr; `tokenize-wikipedia` &rarr; `tokenize-oscar` &rarr; `tokenize-ud` &rarr; `create-input` &rarr; `train-floret-vectors` &rarr; `load-vectors` &rarr; `init-labels` &rarr; `train-sm` &rarr; `train` &rarr; `evaluate-sm` &rarr; `evaluate` &rarr; `convert-ner` &rarr; `create-ner-config` &rarr; `train-ner-sm` &rarr; `assemble-sm-core` &rarr; `assemble-md-core` &rarr; `assemble-meta` &rarr; `package-sm-dep` &rarr; `package-sm-core` &rarr; `package-md-dep` &rarr; `package-md-core` &rarr; `document` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `assets/original/UD_Latin-Perseus` | Git |  |
| `assets/original/UD_Latin-PROIEL` | Git |  |
| `assets/original/UD_Latin-ITTB` | Git |  |
| `assets/original/UD_Latin-LLCT` | Git |  |
| `assets/original/UD_Latin-UDante` | Git |  |
| `vectors/downloaded/wikipedia/lawiki-latest-pages-articles.xml.bz2` | URL |  |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->

## Install

- To install the current version...
    - `pip install https://huggingface.co/diyclassics/la_core_cltk_md/resolve/main/la_core_cltk_md-0.4.0/dist/la_core_cltk_md-0.4.0.tar.gz`

## Model repository

- The model itself can be found here:
    - https://huggingface.co/diyclassics/la_core_cltk_md

## Current version

| Feature | Description |
| --- | --- |
| **Name** | `la_core_cltk_md` |
| **Version** | `0.4.0` |
| **spaCy** | `>=3.5.1,<3.6.0` |
| **Default Pipeline** | `normer`, `tok2vec`, `tagger`, `morphologizer`, `trainable_lemmatizer`, `parser`, `lemma_fixer`, `ner` |
| **Components** | `senter`, `normer`, `tok2vec`, `tagger`, `morphologizer`, `trainable_lemmatizer`, `parser`, `lemma_fixer`, `ner` |
| **Vectors** | -1 keys, 50000 unique vectors (300 dimensions) |
| **Sources** | UD_Latin-Perseus<br />UD_Latin-PROIEL<br />UD_Latin-ITTB<br />UD_Latin-LLCT<br />UD_Latin-UDante |
| **License** | `MIT` |
| **Author** | [Patrick J. Burns; with Nora Bernhardt [ner], Tim Geelhaar [tagger, morphologizer, parser], Vincent Koch [ner]](https://diyclassics.github.io/) |

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 85.32 |
| `ENTS_P` | 79.30 |
| `ENTS_R` | 92.33 |
| `NER_LOSS` | 4173.84 |
| `NER_TOK2VEC_LOSS` | 256.54 |
| `SENTS_F` | 92.75 |
| `SENTS_P` | 93.09 |
| `SENTS_R` | 92.41 |
| `TAG_ACC` | 93.58 |
| `POS_ACC` | 96.92 |
| `MORPH_ACC` | 91.72 |
| `LEMMA_ACC` | 94.25 |
| `DEP_UAS` | 81.86 |
| `DEP_LAS` | 75.84 |
| `TOK2VEC_LOSS` | 8284457.01 |
| `TAGGER_LOSS` | 913771.50 |
| `MORPHOLOGIZER_LOSS` | 1997175.68 |
| `TRAINABLE_LEMMATIZER_LOSS` | 761110.79 |
| `PARSER_LOSS` | 6647260.73 |

NB: For full details on tags etc., see the README.md in the model package.
