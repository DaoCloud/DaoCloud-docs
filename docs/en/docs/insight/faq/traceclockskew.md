---
MTPE: windsonsea
date: 2024-06-11
hide:
   - toc
---

# Clock offset in trace data

In a distributed system, due to [Clock Skew (clock skew adjustment)](https://en.wikipedia.org/wiki/Clock_skew) influence,
Time drift exists between different hosts. Generally speaking, the system time of different hosts at the same time has a slight deviation.

The traces system is a typical distributed system, and it is also affected by this phenomenon in terms of
time data collection. For example, in a link, the start time of the server-side span is earlier than
that of the client-side span. This phenomenon does not exist logically, but due to the influence of clock skew,
there is a deviation in the system time between the hosts at the moment when the trace data is collected in each service, which eventually leads to the phenomenon shown in the following figure:

The phenomenon in the above figure cannot be eliminated theoretically. However, this phenomenon is rare,
and even if it occurs, it will not affect the calling relationship between services.

Currently Insight uses Jaeger UI to display trace data, and the UI will remind when encountering such a link:

Currently Jaeger's community is [trying to optimize this problem through the UI level](https://github.com/jaegertracing/jaeger-ui/issues/197).

For more information, refer to:

- [Clock Skew Adjuster considered harmful](https://github.com/jaegertracing/jaeger/issues/1459#issuecomment-582519000)
- [Add ability to display unadjusted trace in the UI](https://github.com/jaegertracing/jaeger-ui/issues/197)
- [Clock Skew Adjustment](https://www.jaegertracing.io/docs/1.40/deployment/#clock-skew-adjustment)
