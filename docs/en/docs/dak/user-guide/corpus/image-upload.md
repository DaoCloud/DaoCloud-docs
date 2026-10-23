# Image Import

Before importing image and text data, the corpus needs to be processed (currently only supports image and text processing for Word and Excel).

## Preprocessing Docx Documents

1. Directly supports splitting Docx documents containing images and text according to the specified character length.

    <!-- !\[.*?\]\((?:https?:\/\/)?\S+\.(?:png|jpg|jpeg|gif|bmp)\) -->

2. Also supports manual splitting using the `<split></split>` tags to plan the document's paragraph divisions in advance.

    <!-- !\[.*?\]\((?:https?:\/\/)?\S+\.(?:png|jpg|jpeg|gif|bmp)\) -->

    For images in the Docx document, please paste them directly into the document (do not use shapes or text boxes to wrap the images) to avoid the program being unable to detect them and thus missing the image processing.

## Preprocessing xlsx Documents

The xlsx file must conform to a fixed template format:

<!-- !\[.*?\]\((?:https?:\/\/)?\S+\.(?:png|jpg|jpeg|gif|bmp)\) -->

Q: Question, A: Answer.

For xlsx documents, please organize them according to the template requirements, and try to place illustrations within a single cell, avoiding spanning multiple cells.

## Generating Image and Text Corpus

1. Log into the environment: https://console.d.run/ai-tools/lab? Password: aitools.

    <!-- !\[.*?\]\((?:https?:\/\/)?\S+\.(?:png|jpg|jpeg|gif|bmp)\) -->

2. Upload the corpus file. Navigate to the directory /app/corpus_processing/input and upload the corpus file to this directory.

    <!-- !\[.*?\]\((?:https?:\/\/)?\S+\.(?:png|jpg|jpeg|gif|bmp)\) -->

3. Click to run the code.

    <!-- !\[.*?\]\((?:https?:\/\/)?\S+\.(?:png|jpg|jpeg|gif|bmp)\) -->

4. Download the generated image and text corpus file. Go to the directory /app/corpus_processing/output to download the zip file.

    <!-- !\[.*?\]\((?:https?:\/\/)?\S+\.(?:png|jpg|jpeg|gif|bmp)\) -->

5. Clean up the environment. Clear the input and output files, as well as the running log files.

    <!-- !\[.*?\]\((?:https?:\/\/)?\S+\.(?:png|jpg|jpeg|gif|bmp)\) -->

    !!! note

        This environment is public; it is recommended to perform the cleanup operation after handling private corpus files.

### Importing the Downloaded Files

1. Click **Corpus Import** -> **Image and Text Import**.

2. Upload the processed file and proceed with vectorization, waiting for successful processing.
