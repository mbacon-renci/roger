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
