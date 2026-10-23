---
hide:
  - toc
---

# File Import

1. Click the **┇** button next to the corpus and select the **File Import** method.

    <!-- !\[.*?\]\((?:https?:\/\/)?\S+\.(?:png|jpg|jpeg|gif|bmp)\) -->

2. **Import Data**: Click **Upload File** and choose the processing method for file segments: Standard Processing or Custom Processing (i.e., plugin processing; please refer to the plugin integration section).

    <!-- !\[.*?\]\((?:https?:\/\/)?\S+\.(?:png|jpg|jpeg|gif|bmp)\) -->

    !!! note

        - Currently, formats supported include pdf, txt, docx, doc, csv, and xlsx. It is recommended that the size of a single file does not exceed 50MB, and the limit for the number of files uploaded is 50.
        
        - Standard processing rules for segmentation.
   
            ```template
            1. PDF, TXT, DOC, DOCX support custom delimiters;
            2. Set a delimiter, do not set segment size, and divide the document based solely on the delimiter;
            3. Do not set a delimiter, set segment size, and split the document solely based on segment size;
            4. Set a delimiter and set segment size; within the segment size, ultimately split based on the delimiter match.
            ```

3. **Segment Preview**: Preview whether the segments are correct. If incorrect, you can go back to the previous step to modify the segmentation rules or file content.

    <!-- !\[.*?\]\((?:https?:\/\/)?\S+\.(?:png|jpg|jpeg|gif|bmp)\) -->

4. **Data Vectorization**: Check the number of file segments, the number of duplicate segments, the number of segments imported this time, and the vectorization status. Once the vectorization process is successful, click **Next**.

    <!-- !\[.*?\]\((?:https?:\/\/)?\S+\.(?:png|jpg|jpeg|gif|bmp)\) -->

5. Once the file status indicates that the file processing is complete, click **OK**.

    <!-- !\[.*?\]\((?:https?:\/\/)?\S+\.(?:png|jpg|jpeg|gif|bmp)\) -->
