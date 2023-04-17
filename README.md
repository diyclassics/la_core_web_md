<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: la_core_cltk_md

Code required to train spaCy-compatible md core model for Latin, i.e pipeline with POS tagger, morphologizer, lemmatizer, dependency parser, and NER trained on all available Latin UD treebanks, i.e. Perseus, PROIEL, ITTB, UDante, and LLCT (see below). The model contains floret vectors trained on Wikipedia, Oscar, and UD data. NER is based on custom tagged data based on tagger output and manual annotation; this data is included in `assets/local/ud-ner.tsv`. Note also that a sm model (i.e. without vectors) is trained in the same pipeline.

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
| `package-sm-core` | Package the trained sm core model |
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
| `all` | `assets` &rarr; `preprocess` &rarr; `convert` &rarr; `norm-corpus` &rarr; `extract-wikipedia` &rarr; `tokenize-wikipedia` &rarr; `tokenize-oscar` &rarr; `tokenize-ud` &rarr; `create-input` &rarr; `train-floret-vectors` &rarr; `load-vectors` &rarr; `init-labels` &rarr; `train-sm` &rarr; `train` &rarr; `evaluate-sm` &rarr; `evaluate` &rarr; `convert-ner` &rarr; `create-ner-config` &rarr; `train-ner-sm` &rarr; `assemble-sm-core` &rarr; `assemble-md-core` &rarr; `assemble-meta` &rarr; `package-sm-core` &rarr; `package-md-core` &rarr; `document` |

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
    - `pip install https://huggingface.co/diyclassics/la_core_cltk_md/resolve/main/la_core_cltk_md-3.5.0/dist/la_core_cltk_md-3.5.0.tar.gz`

## Model repository

- The model itself can be found here:
    - https://huggingface.co/diyclassics/la_core_cltk_md

## Current version

| Feature | Description |
| --- | --- |
| **Name** | `la_core_cltk_md` |
| **Version** | `3.5.0` |
| **spaCy** | `>=3.5.1,<3.6.0` |
| **Default Pipeline** | `normer`, `tok2vec`, `tagger`, `morphologizer`, `trainable_lemmatizer`, `parser`, `lemma_fixer`, `ner` |
| **Components** | `senter`, `normer`, `tok2vec`, `tagger`, `morphologizer`, `trainable_lemmatizer`, `parser`, `lemma_fixer`, `ner` |
| **Vectors** | -1 keys, 50000 unique vectors (300 dimensions) |
| **Sources** | UD_Latin-Perseus<br />UD_Latin-PROIEL<br />UD_Latin-ITTB<br />UD_Latin-LLCT<br />UD_Latin-UDante<br /> [Herodotos Project](https://github.com/Herodotos-Project/Herodotos-Project-Latin-NER-Tagger-Annotation/tree/master/Annotation_1-1-19) |
| **License** | `MIT` |
| **Author** | [Patrick J. Burns; with Nora Bernhardt [ner], Tim Geelhaar [tagger, morphologizer, parser], Vincent Koch [ner]](https://diyclassics.github.io/) |


### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 85.27 |
| `ENTS_P` | 82.34 |
| `ENTS_R` | 88.41 |
| `NER_LOSS` | 3268.99 |
| `NER_TOK2VEC_LOSS` | 488.66 |
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

### Bibliography
- Cecchini, F.M., Passarotti, M., Marongiu, P., and Zeman, D. 2018. “Challenges in Converting the Index Thomisticus Treebank into Universal Dependencies.” In Proceedings of the Second Workshop on Universal Dependencies (UDW 2018). 27–36.
- Cecchini, F.M., Sprugnoli, R., Moretti, G., and Passarotti, M. 2020. “UDante: First Steps Towards the Universal Dependencies Treebank of Dante’s Latin Works.” In Dell’Orletta, F., Monti, J., and Tamburini, F. eds. Proceedings of the Seventh Italian Conference on Computational Linguistics CLiC-It 2020. Accademia University Press. 99–105. doi:10.4000/books.aaccademia.8653. http://books.openedition.org/aaccademia/8653.
- Celano, G.G.A., Crane, G., Almas, B., and et al. 2014. “The Ancient Greek and Latin Dependency Treebank v.2.1.” https://perseusdl.github.io/treebank_data/.
- Erdmann, A., Wrisley, D.J., Allen, B., Brown, C., Bodénès, S.C., Elsner, M., Feng, Y., Joseph, B., Joyeaux-Prunel, B., and Marneffe, M.-C. 2019. “Practical, Efficient, and Customizable Active Learning for Named Entity Recognition in the Digital Humanities.” In Proceedings of North American Association of Computational Linguistics (NAACL 2019). Minneapolis, Minnesota.
- Haug, D.T., and Jøhndal, M. 2008. “Creating a Parallel Treebank of the Old Indo-European Bible Translations.” In Proceedings of the Second Workshop on Language Technology for Cultural Heritage Data (LaTeCH 2008). 27–34.
- Honnibal, M., and Montani, I. 2023. “SpaCy: Industrial-Strength Natural Language Processing in Python” (version v. 3.5.0). https://spacy.io/.
- Korkiakangas, T. 2021. “Late Latin Charter Treebank: Contents and Annotation.” Corpora 16 (2) (August 1): 191–203. doi:10.3366/cor.2021.0217.
- Passarotti, M., and Dell’Orletta, F. 2010. “Improvements in Parsing the Index Thomisticus Treebank. Revision, Combination and a Feature Model for Medieval Latin.” In Proceedings of the Seventh International Conference on Language Resources and Evaluation (LREC’10). Valletta, Malta: European Language Resources Association (ELRA). http://www.lrec-conf.org/proceedings/lrec2010/pdf/178_Paper.pdf.
