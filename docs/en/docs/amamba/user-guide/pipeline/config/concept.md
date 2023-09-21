# Concepts in the pipeline

Regardless of the graphical or text type, the editor is essentially used to facilitate users to view and edit the core of the construction process: Jenkinsfile (process description file). Therefore, before discussing the editor, it is necessary to understand several important concepts of the "process description file".

<!--![]()screenshots-->

- Pipeline

    `Pipeline` is a working model defined by the user. The code of the pipeline defines the complete process of software delivery, generally including the stages of building, testing and delivering applications.
    See the [Jenkins official documentation](https://www.jenkins.io/doc/book/pipeline/jenkinsfile/) for pipeline syntax.

- Agent

    Agent describes the entire `pipeline` execution process or the execution environment of a certain `stage`, and must appear in the `description file` at the top or each `stage`.
    See [Selecting a Jenkins Agent](agent.md) for more information.

- stage

    A `phase` defines a sequence of closely related `steps`. Each `stage` assumes independent and well-defined responsibilities in the entire pipeline.
    Such as "Build", "Test" or "Deploy" phases. Generally speaking, all the actual build process is placed inside `Stages`.
    See [Choosing a Jenkins Stage](https://www.jenkins.io/doc/book/pipeline/#stage) for more information.

- Parallel stage

    Parallel is used to declare some `stages` that are executed in parallel, and it is usually applicable to the case where there is no dependency between `stages` and `stages` to speed up execution.
    See [Selecting a Jenkins Agent](agent.md) for more information.

- steps

    The `step list` describes what to do in a `stage` and what commands to execute. For example, there is a `step (step)` that requires the system to print a message of `Building...`, that is, run the command `echo 'Building...'`.
    See [Choosing a Jenkins Step](https://www.jenkins.io/doc/book/pipeline/#stage) for more information.