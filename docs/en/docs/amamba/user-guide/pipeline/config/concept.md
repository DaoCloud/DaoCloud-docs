# Concepts in the pipeline

Regardless of the graphical or text type, the editor is essentially used to facilitate users to view and edit the core of the construction process: Jenkinsfile (process description file). Therefore, before discussing the editor, it is necessary to understand several important concepts of the "process description file".

<!--![]()screenshots-->

- Pipeline

    __Pipeline__ is a working model defined by the user. The code of the pipeline defines the complete process of software delivery, generally including the stages of building, testing and delivering applications.
    See the [Jenkins official documentation](https://www.jenkins.io/doc/book/pipeline/jenkinsfile/) for pipeline syntax.

- Agent

    Agent describes the entire __pipeline__ execution process or the execution environment of a certain __stage__, and must appear in the __description file__ at the top or each __stage__.
    See [Selecting a Jenkins Agent](agent.md) for more information.

- stage

    A __phase__ defines a sequence of closely related __steps__. Each __stage__ assumes independent and well-defined responsibilities in the entire pipeline.
    Such as "Build", "Test" or "Deploy" phases. Generally speaking, all the actual build process is placed inside __Stages__.
    See [Choosing a Jenkins Stage](https://www.jenkins.io/doc/book/pipeline/#stage) for more information.

- Parallel stage

    Parallel is used to declare some __stages__ that are executed in parallel, and it is usually applicable to the case where there is no dependency between __stages__ and __stages__ to speed up execution.
    See [Selecting a Jenkins Agent](agent.md) for more information.

- steps

    The __step list__ describes what to do in a __stage__ and what commands to execute. For example, there is a __step (step)__ that requires the system to print a message of __Building...__, that is, run the command __echo 'Building...'__.
    See [Choosing a Jenkins Step](https://www.jenkins.io/doc/book/pipeline/#stage) for more information.