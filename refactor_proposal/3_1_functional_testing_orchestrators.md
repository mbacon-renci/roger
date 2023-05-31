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
