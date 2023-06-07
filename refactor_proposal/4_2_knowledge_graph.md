### Knowledge Graph

The annotate phase corresponds to the following makefile: `bin/roger_graph_build/Makefile`. This phase has three steps that each execute the `cli.py` with specific arguments. (These steps must be done in the order lsited)

- get: gets files from the last step of the annotate phase the output is saved in the `dags/roger/data/kgx/` as jsonl files.
- merge: merges duplicate nodes indexes in redis. The output is saved in `dags/roger/data/merge/`, creates two files that contain the official nodes and edges. (This file is huge and there may be better ways to do this, also this step is VERY SLOW)
- schema: Creates the schema for the redis nodes "categories", where the node data is stored and the "predicate" where the edge data is stored. Written to `dags/roger/data/schema/`.
- tables: NOTE: This step is called bulk.create in the code but the function doesn't exist? **How is this working? Python class magic??** Prepares for the bulk loader step by writing the csv files that are used to write nodes and edges. The data is saved in `dags/roger/data/bulk`.
- install: this starts the redis bulk loader of the nodes and edges. It reads the name of the file from the `dags/roger/data/bulk/nodes/` and `dags/roger/data/bulk/edges/` and creates a node or edge from each row of file contents.
- validate: prepared validation Redis queries and 1 major Tranql query are used to validate the the output. The success or failure of this step is not returned to the user though. **The problem here is that one must understand the data ahead of time to create a specific TranQL query. If someone does not have the data in their Dug version that is being tested then these queries are useless.**