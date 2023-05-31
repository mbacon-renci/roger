# Roger/Dug refactor proposal

The purpose of this document is to outline a set of proposals for
reorganizing the Roger code to make it easier to collaborate on and to
facilitate the adoption of orchestrators other than Apache Airflow.

## Code reorganization

The changes in this section do not change anything with the code
itself, but rather how the code is organized and installed. These
changes are both in service of making roger more flexible with regards
to orchestrators and making it easier for third parties to install and
work on.
### Pip install for roger

Currently roger is installed with a git pull (managed by the Docker
helm chart) to the dag directory of the Airflow scheduler
instance. This requires that all library code be under the `dag`
directory of the Roger repository, which makes for awkward usage when
using the command line tools, makefiles, or another non-Airflow
orchestrator.

We propose to move the library code out of the dag directory and have
the main Roger code be installed into the local python environment
using `pip` (or similar) such that the main library functions can be
imported from any working directory uniformly.

In addition, having it be installable as a python package would allow
for the command line scripts to be reliably placed into the
environment execution path, which would require setting fewer
environment variables on install of roger.
### Move classes out of core.py

The file `core.py` currently has gotten very large and has multiple
classes which are largely independent of each other defined in
it. These classes would move to submodules that were more explicitly
organized by function.

The purpose of this move is to reduce potential conflicts in parallel
development and simply to make the code in the module, some of which
is the most important and critical, easier to read and review.
### Python standardization

In a few places, roger code has some coding patterns which are
functional but unusual in most python coding. Some very small changes
which will not affect execution could lead to more canonical python
code.
## Generalization and abstraction

Currently the roger code largely assumes an Airflow orchestrator, and
adapting it to work with other orchestrators, whether Makefile or
command line oriented or larger, like Argo, requires some awkward
execution patterns.

This section proposes several changes which should facilitate the work
of making roger more flexible and adaptable.
### File I/O abstraction layer

Currently the roger code anticipates that all reads and writes will be
done to a local, standard block file system. In cloud systems, many
deploying roger may wish to write to S3, or in the case of RENCI, to
LakeFS.

This work will introduce an abstraction layer for storage. The storage
class can be defined or adjusted using configuration parameters. That
storage class will define methods for reading or writing result data,
or for obtaining basic file metadata about those data.

With this, multiple different storage types may be included in the
roger code, and the user deploying the code may then select which
storage class to use at runtime using the configuration architecture.
## Documentation and testing

This section perhaps needs no introduction, as all code can generally
benefit from greater documentation and testing. In this case, the
documentation will come from lessons learned from the deployment at
RTI. Testing in particular will focus on functionally proofing the
code under a number of different orchestration scenarios.
### Functional testing orchestrators

Maintaining working code that correctly implements across a range of
orchestrators is difficult when any given developer is only targeting
making it functional for one or perhaps two.

This work would implement a set of functional tests using Docker, each
of which would ensure correct implementation for a given
orchestrator.

While not necessarily part of the scope of this work, this could in
turn facilitate CI/CD configuration which ensured that each
orchestrator was functional upon commit to the main `develop` branch.
