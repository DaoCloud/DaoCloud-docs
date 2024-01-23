# CoreDNS Performance Test Report

## Test Background

Latency data of CoreDNS in a standard environment.

## Benchmark

This article is based on the environment installed with DCE 5.0, where one group of environments only installed CoreDNS, and another group installed CoreDNS and nodelocaldns, with the remaining parameters set to default configuration.

### Physical Machine

| Name        | CPU                                       |  CPU  | MEM  | Network    |
|:------------|:------------------------------------------|:------|:-----|:-------------|
| Node 1      | Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz |  56C  | 128G | 10G Mellanox |
| Node 2      | Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz |  56C  | 128G | 10G Mellanox |

The following are the data obtained from load testing on physical servers:

- With nodelocaldns

    |        Scenario        |      nslookup Time    |     Total Time     |
    | :-----------------:|:-------------------: | :-----------: |
    | Same Node Pod          |       0.001250       |    0.001867   |
    | Cross Node Pod          |       0.001319       |    0.002238   |
    | External Website            |       0.002954       |    0.019675   |

- Without nodelocaldns

    |        Scenario        |      nslookup Time    |     Total Time     |
    | :-----------------:|:-------------------: | :-----------: |
    | Same Node Pod          |       0.001495       |    0.002200   |
    | Cross Node Pod          |       0.001563       |    0.002700   |
    | External Website            |       0.007863       |    0.027283   |

### Virtual Machine

| Name         | CPU                                       |  CPU  | MEM  |
|:------------|:------------------------------------------|:------|:-----|
| Node 1      | Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz  |  16C  | 16G  |
| Node 2      | Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz  |  16C  | 16G  |

The following are the data obtained from load testing on virtual servers.

- With nodelocaldns

    |        Scenario        |      nslookup Time    |     Total Time     |
    | :-----------------:|:-------------------: | :-----------: |
    | Same Node Pod          |       0.001765       |    0.003267   |
    | Cross Node Pod          |       0.002251       |    0.003593   |
    | External Website            |       0.003656       |    0.064317   |

- Without nodelocaldns

    |        Scenario        |      nslookup Time    |     Total Time     |
    | :-----------------:|:-------------------: | :-----------: |
    | Same Node Pod          |       0.002059       |    0.003544   |
    | Cross Node Pod          |       0.002246       |    0.003788   |
    | External Website            |       0.010509       |    0.072507   |
