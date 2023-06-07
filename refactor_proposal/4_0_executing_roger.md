## Executing roger

There are several different ways to execute the Roger workflow. 
In general the makefiles found in `roger/bin/` contain the structure that all Roger workflow methods must follow.
There are three phases of Roger that correspond to the three makefiles directiories.
1) Annotate: Data is extracted from source files, then parsed and examined through API calls to external services.
2) Knowledge Graph: Data from the 1st phase is used to construct a knowledge graph based on the biolink data linkages provided from the NCAT translator and Monarch API.
3) Index: The knowledge graph is crawled and the results are stored in elastic search along with the information found in the annotate phase.