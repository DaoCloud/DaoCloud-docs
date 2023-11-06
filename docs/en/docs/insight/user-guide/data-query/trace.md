# Trace Query

On the trace query page, you can query detailed information about a call trace by TraceID or filter call traces based on various conditions.

## Glossary

- TraceID: Used to identify a complete request call trace.
- Operation: Describes the specific operation or event represented by a Span.
- Entry Span: The entry Span represents the first request of the entire call.
- Latency: The duration from receiving the request to completing the response for the entire call trace.
- Span: The number of Spans included in the entire trace.
- Start Time: The time when the current trace starts.
- Tag: A collection of key-value pairs that constitute Span tags. Tags are used to annotate and supplement Spans, and each Span can have multiple key-value tag pairs.

## Steps

Please follow these steps to search for a trace:

1. Go to the `Insight` product module.
2. Select `Data Query` -> `Trace Query` from the left navigation bar.
3. Query the trace by multiple conditions or use the TraceID for an exact search.

    !!! note

        Sorting by span count, latency, and start time is supported in the list.

4. Click the TraceID name to view the detailed invocation information for that trace.


!!! note

    To search using a TraceID, please enter the complete TraceID.

### Associated Logs

1. Click the icon on the right side of the trace data to search for associated logs.

    - By default, it queries the log data within the duration of the trace and one minute after its completion.
    - The queried logs include those with the trace's TraceID in their log text and container logs related to the trace invocation process.
  
2. Click `View More` to jump to the `Log Search` page with conditions.
3. Supports filtering based on pod and fuzzy keyword search.

    !!! note

        1. If the trace spans across clusters or namespaces and the user does not have sufficient permissions, the associated logs cannot be queried.
        2. After jumping to `Log Search,` a default search will be performed based on the user's permissions.
