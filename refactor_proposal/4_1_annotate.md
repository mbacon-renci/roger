### Annotate

The annotate phase corresponds to the following makefile: `bin/dug_annotate/Makefile`. This phase has three steps that each execute the `cli.py` with specific arguments. (These steps must be done in the order lsited)

- get_input_files: Exracts all source data (studies) from the S3 bucket
- annotate_and_normalize: Parse all `Dug Elements` from study variables and run the elements through multiple APIs to get matching biolink ID, associated biolink data, and synonyms. **Any errors in this step crash the process... better error handling here!**
- create_kgx_files: create the files that will be used to generate the knowledge graph in the next phase. **Redis indexes are created here and this requires huge amounts of processing power from the worker and Redis... apparently Howard is working on a fix?**