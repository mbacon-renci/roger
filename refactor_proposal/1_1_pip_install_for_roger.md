## Pip install for roger

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
