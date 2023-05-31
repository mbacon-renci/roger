## Generalization and abstraction

Currently the roger code largely assumes an Airflow orchestrator, and
adapting it to work with other orchestrators, whether Makefile or
command line oriented or larger, like Argo, requires some awkward
execution patterns.

This section proposes several changes which should facilitate the work
of making roger more flexible and adaptable.
