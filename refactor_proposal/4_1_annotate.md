### Annotate

The annotate phase corresponds to the following makefile: `bin/dug_annotate/Makefile`. This phase has three steps that each execute the `cli.py` with specific arguments. (These steps must be done in the order lsited)

- get_input_files: Exracts all source data (studies) from the S3 bucket
- annotate_and_normalize: Parse all `Dug Elements` from study variables and run the elements through multiple APIs to get matching biolink ID, associated biolink data, and synonyms.
- create_kgx_files: create the files that will be used to generate the knowledge graph in the next phase.