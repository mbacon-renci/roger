### Indexing

The Indexing phase performs a "crawl" on the knowledge graph (i.e. queries the graph with specific questions) that was created in phase 2 and stores the results inside a Elasticsearch index, the other two steps create and concepts index and a variable index. All of these indexes are used by the Dug API which services the UI.

Biggest issue here is in the crawl. When you perform a crawl you must run a massive cypher query that returns all nodes and associations twice (one for crawling nodes and one for crawling edges?). This query takes a very long time **(at least 10 minutes)**. How can we speed this up or remove it?