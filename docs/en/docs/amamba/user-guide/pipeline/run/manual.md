# Manually run the pipeline

This page describes manual pipeline execution on the GUI, including immediate execution, rerun, and cancel run.

## Run the pipeline immediately

1. Select a pipeline on the pipeline list page, click __︙__, and click __Run Now__ in the pop-up menu.

   <!--![]()screenshots-->

2. Depending on whether the pipeline is configured with __build parameters__, the following two situations will occur after execution:

   - If __Build Parameters__ is configured, a dialog box will appear and display relevant content for parameter configuration.

     <!--![]()screenshots-->

   - If no __build parameter__ is configured, the pipeline executes immediately.

3. The pipeline starts executing.

   <!--![]()screenshots-->

## Rerun the pipeline

On the pipeline details page, according to the execution ID in the pipeline running record, you can __rerun__ the pipeline that has already been run.

1. In the pipeline list, click the name of a certain pipeline to enter the pipeline details page.

2. In the __Run Record__ area, find the __Execution ID__ that needs to be re-run.

3. Click __︙__ on the right, and click __Rerun__ in the pop-up menu.

   <!--![]()screenshots-->

4. The pipeline reruns successfully.

   <!--![]()screenshots-->

## Cancel running the pipeline

On the pipeline details page, according to the __execution ID__ in the pipeline running record, you can __cancel__ the executing pipeline.

1. In the pipeline list, click the name of a certain pipeline to enter the pipeline details page.

2. In the __Operation Record__ area, find the __Execution ID__ that needs to be canceled.

3. Click __︙__ on the right, and click __Cancel__ in the pop-up menu (applicable to pipelines whose status is __Executing__).

   <!--![]()screenshots-->

4. The pipeline cancellation operation is successful.

   <!--![]()screenshots-->