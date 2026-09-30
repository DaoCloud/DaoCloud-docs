---
hide:
  - navigation
---

# OceanStor A Series Storage and DaoCloud d.run Computing Scheduling Platform Compatibility Test Report

## 1 Environment Configuration

### 1.1 Verification Network Diagram

![img](./images/clip_image008.png)

<div style="text-align:center;">Figure 1-1 Functional Verification Network Diagram</div>

### 1.2 Hardware and Software Configuration

#### 1.2.1 Storage System Configuration

This test requires a set of Huawei OceanStor A800 storage system, configuration reference as follows:

Table 1-1 OceanStor A800 Configuration

| Name | Description | Model | Unit Height | Quantity |
| --- | ------- | -------- | -------- | -------- |
| AI Storage | OceanStor A800 <br />Control enclosure: 2 controllers <br />CPU per controller: 4*Kunpeng920-7260X <br />Memory per controller: 1TB <br />Disk: 1.746TB NVMe PALM disk 20 pieces <br />Network: 4 * 2-port 25GE RoCE NIC; 2 * 4-port 25GE ETH NIC | OceanStor A800 | 8U | 1 |

#### 1.2.2 Supporting Test Hardware

Table 1-2 Supporting Hardware Configuration

| Name | Description | Model | Unit Height | Quantity |
| --- | --- | -----| ------ | ---- |
| Inference Server | <br />CPU: 2 * HUAWEI Kunpeng 920 <br />NPU: 8 * Ascend 910B (64G VRAM) <br />NIC 1: 4 * 2-port 200GE ROCE NIC (parameter plane, optional) <br />NIC 2: 1 * 2-port 25GE ROCE NIC (data plane) <br />NIC 3: 1 * 4-port 25GE ETH NIC (business plane) <br />System Disk: 2 * 480GB SATA SSD | Atlas 800T A2 | 4U | 1 |
| Business Switch | Used for connecting business and storage plane network | CE6865 | 1U | 1 |
| Parameter Plane Switch (not required for single node) | Used for computing server parameter plane network, using 400GE 1-to-2 cable to connect computing server | XH9210 | 1U | 1 |

#### 1.2.3 Test Software and Tools

Table 1-3 Test Software and Tools

| Software Type | Description |
| ------ | ---- |
| Compute Server OS | OpenEuler 22.03 LTS (5.10.0-60.18.0.50.oe2203) |
| DataTurbo | File acceleration engine |
| NFS Client | NFS file system mount |
| NPU Driver | Version 24.1.rc3 |
| Docker | Container control software, version 20.10.9 |
| Python | Common AI programming language, version 3.10 |
| CANN | Heterogeneous computing architecture for AI scenarios, version 8.0.RC3 |
| Inference Model | Qwen3-32B |

## 2 Verification Results

### 2.1 Basic Information

Table 2-1 Basic Information

| Field | Description |
| --- | -------------- |
| Vendor | Huawei Technologies Co., Ltd. |
| Product | Huawei OceanStor A Series Storage System |
| Location | |
| Personnel | |
| Date | |
| Other Information | |

### 2.2 Verification Purpose

This test aims to verify the compatibility between the DaoCloud d.run Computing Scheduling Platform and Huawei A Series storage, and to verify the inference acceleration capability of A Series storage UCM on the d.run Computing Scheduling Platform, focusing on TTFT, throughput improvement, and concurrency improvement.

### 2.3 Verification Summary

The DaoCloud d.run Computing Scheduling Platform is compatible with Huawei A Series storage and supports the Unified Cache Manager inference acceleration capability for AI scenarios. In scenarios with long-sequence inputs and high concurrency for LLM model inference, the Unified Cache solution provides features such as Prefix Cache and GSA based on the Huawei OceanStor A Series storage system. By changing the way KV Cache is reused, slicing the input sequence, and sparsifying long sequences, it effectively shortens TTFT and improves throughput and concurrency.

For the Qwen3-32B model with a sequence length of 32K + 1K, TTFT improves by up to 47% and E2E throughput improves by up to 75%. When the concurrency exceeds 15, the maximum E2E throughput with UCM disabled is 102 tok/s, and the throughput fluctuates as concurrency increases.

| Input Length | Output Length | Concurrency | | TTFT ms | | | E2E Throughput tok/s | |
| ------ | ------- | ----- | ------- | ------------ | ----- | -- | -- | -- |
| | | | UCM On | UCM Off | Improvement | UCM On | UCM Off | Improvement |
| 32000 | 1000 | 10 | 26,174.26 | 29755.01 | 12.03% | 103.59 | 92.85 | 11.57% |
| 32000 | 1000 | 15 | 38,726.93 | 42776.58 | 9.47% | 125.81 | 102.16 | 23.15% |
| 32000 | 1000 | 20 | 52,450.65 | 70537.73 | 25.64% | 142.62 | 82.25 | 73.40% |
| 32000 | 1000 | 25 | 59,713.67 | 100254.08 | 40.44% | 151.25 | 88.32 | 71.25% |
| 32000 | 1000 | 30 | 65,833.11 | 124975.91 | 47.32% | 162.47 | 92.71 | 75.25% |

For the Qwen3-32B model with a sequence length of 32K + 1K, when UCM is disabled, requests start queuing after the maximum concurrency of 17 is exceeded; when UCM is enabled, requests start queuing after the maximum concurrency of 32 is exceeded. In the above cases, enabling UCM improves concurrency by 88.24% compared with disabling UCM.

| (4*910B)/Qwen3 | | UCM On | UCM Off | Concurrency Improvement |
| -------------- | ------- | ------- | ------- | -- |
| Input Length | Output Length | Max Concurrency | Max Concurrency | 88.24% |
| 32000 | 1000 | 32 | 17 | |

## 3 Verification Test Cases

### 3.1 Resource Management Test

#### 3.1.1 Storage Backend Resource Management

- **Test Purpose**

    Verify that the Shanghai DaoCloud platform manages Huawei storage backend resources through the Huawei CSI plugin.

- **Test Network**

    Huawei Container Storage Solution Verification Network Diagram

- **Prerequisites**

    1. The Kubernetes cluster is running properly.
    2. A storage pool has been created on the Huawei storage system and is running properly.
    3. The Huawei CSI plugin has been installed and is running properly.

- **Test Steps**

    1. Refer to the backend.yaml template file in the examples/backend directory of the Huawei CSI software package, and create a storage backend configuration file based on the actual environment information.
       
        ![333](./images/clip_image010.png)

    2. Use the configuration file to create a storage backend, enter the username and password of the storage backend as prompted, and check whether the storage backend is created successfully.
       
        ![444](./images/clip_image012.png)

    3. Delete the created storage backend and check whether it is deleted successfully.
       
        ![555](./images/clip_image014.png)

- **Expected Results**
   
    1. In step 2, the storage backend is created successfully as seen on Kubernetes.
    2. In step 3, the storage backend is deleted successfully as seen on Kubernetes.

- **Actual Results**
   
    1. The configuration file is modified  
       
        ![img](./images/clip_image016.png)

    2. The storage backend is created successfully  
       
        ![img](./images/clip_image018.png)

    3. The storage backend is deleted successfully  
       
        ![img](./images/clip_image020.png)

- **Test Conclusion**
    
    Passed

- **Remarks**

    (None)

#### 3.1.2 StorageClass Resource Management

- **Test Purpose**

    Verify that Kubernetes can manage StorageClass resources through the Huawei CSI plugin.

- **Test Network**

    Huawei Container Storage Solution Verification Network Diagram

- **Prerequisites**

    1. The Kubernetes cluster is running properly.
    2. A storage pool has been created on the Huawei storage system and is running properly.
    3. The Huawei CSI plugin has been installed and is running properly.
    4. The storage backend has been configured in Kubernetes.

- **Test Steps**
   
    1. Refer to the sc-lun.yaml template file in the examples directory of the Huawei CSI software package, and create a StorageClass configuration file based on the actual environment information.
       
        ![img](./images/clip_image022.png)

    2. Use the configuration file to create a StorageClass and check whether it is created successfully.
      
        ![img](./images/clip_image024.png)

    3. Delete the created StorageClass.
       
        ![img](./images/clip_image026.png)

    4. Check whether the StorageClass is deleted successfully.
       
        ![img](./images/clip_image028.png)

- **Expected Results**

    1. In step 2, the StorageClass is created successfully as seen on Kubernetes.
    2. In step 4, the StorageClass is deleted successfully as seen on Kubernetes.

- **Actual Results**
   
    1. The configuration file is modified  
       
        ![img](./images/clip_image030.png)

    2. The StorageClass is created successfully  
       
        ![img](./images/clip_image032.png)

    3. The StorageClass is deleted successfully  
      
        ![img](./images/clip_image034.png)

- **Test Conclusion**

    Passed

- **Remarks**

    (None)

#### 3.1.3 PVC Resource Management

- **Test Purpose**

    Verify that Kubernetes can manage PVC resources through the Huawei CSI plugin.

- **Test Network**

    Huawei Container Storage Solution Verification Network Diagram

- **Prerequisites**

    1. The Kubernetes cluster is running properly.
    2. The Huawei CSI plugin has been installed and is running properly.
    3. The StorageClass has been created.

- **Test Steps**
    
    1. Refer to the pvc.yaml template file in the examples directory of the Huawei CSI software package, and create a PVC configuration file based on the actual environment information.
     
        ![img](./images/clip_image036.png)

    2. Use the configuration file to create a PVC and check whether it is created successfully.
      
        ![img](./images/clip_image038.png)

    3. Log in to the storage device and check whether the corresponding file system is created automatically.
       
        ![img](./images/clip_image040.png)

        ![img](./images/clip_image042.png)

    4. Delete the created PVC and check whether it is deleted successfully.
       
        ![img](./images/clip_image044.png)

    5. Log in to the storage device and check whether the corresponding file system is deleted automatically.
      
        ![img](./images/clip_image046.png)

- **Expected Results**
    
    1. In step 2, the PVC is created successfully as seen on Kubernetes, and the corresponding file system name can be seen.
    2. In step 3, the corresponding file system is created automatically on the storage, and the capacity is consistent with the PVC.
    3. In step 4, the PVC is deleted successfully as seen on Kubernetes.
    4. In step 5, the corresponding file system is deleted automatically on the storage.

- **Actual Results**
    
    1. The configuration file is modified  
       
        ![img](./images/clip_image048.png)

    2. The PVC is created successfully  
       
        ![img](./images/clip_image050.png)

    3. The file system is created successfully in the storage  
       
        ![img](./images/clip_image052.png)

    4. The PVC is deleted successfully  
       
        ![img](./images/clip_image054.png)

    5. The file system is deleted successfully in the storage  
       
        ![img](./images/clip_image056.png)

- **Test Conclusion**
    
    Passed

- **Remarks**
    
    (None)

#### 3.1.4 Pod Resource Management

- **Test Purpose**
    
    Verify that Kubernetes can manage Pod resources through the Huawei CSI plugin.

- **Test Network**
    
    Huawei Container Storage Solution Verification Network Diagram

- **Prerequisites**
    
    1. The Kubernetes cluster is running properly.
    2. The Huawei CSI plugin has been installed and is running properly.
    3. The PVC to be mounted by the Pod has been created successfully.

- **Test Steps**
   
    1. Refer to the pod.yaml template file in the examples directory of the Huawei CSI software package, and create a Pod configuration file based on the actual environment information.
       
        ![img](./images/clip_image058.png)

    2. Use the configuration file to create a Pod and check whether it is created successfully.
       
        ![img](./images/clip_image060.png)

        ![666](./images/clip_image062.png)

    3. Check whether the file system is mounted successfully on the Kubernetes node where the Pod resides.

    4. Enter the container of the Pod and check whether the PVC is mounted to the specified path.
       
        ![img](./images/clip_image064.png)

    5. Enter the Pod command line interface from the web GUI

        ![img](./images/vllm-workspace.png)

    6. Delete the created Pod and check whether it is deleted successfully.
       
        ![777](./images/clip_image066.png)

- **Expected Results**
   
    1. In step 2, the Pod is created successfully as seen on Kubernetes.
    2. In step 3, the file system is mounted successfully, and the mount information of the file system can be seen.
    3. In step 4, the PVC is mounted successfully to the specified path as seen in the container.
    4. In step 5, the Pod is deleted successfully as seen on Kubernetes.

- **Actual Results**
    
    1. The configuration file is modified  
       
        ![img](./images/clip_image068.png)

    2. The Pod is created successfully  
       
        ![img](./images/clip_image070.png)

    3. The file system is mounted successfully  
      
        ![img](./images/clip_image072.png)

    4. The PVC is mounted to the specified path in the container  
      
        ![img](./images/clip_image074.png)

    5. The Pod is deleted successfully  
       
        ![img](./images/clip_image076.png)

- **Test Conclusion**

    Passed

- **Remarks**

    (None)

### 3.2 Inference Scenario Test

#### 3.2.1 Basic Function Interconnection Test

##### 3.2.1.1 Ascend Ecosystem Interconnection Test

- **Test Purpose**

    Verify the capability of the Unified Cache solution to interconnect with the Ascend ecosystem

- **Test Network**

    Functional Verification Network Diagram

- **Prerequisites**

    1. The storage device has been installed and deployed and has been connected to the Ascend compute server through the NFS over RDMA protocol  
    2. The model files have been downloaded to the specified location on the compute server  
    3. The Unified Cache environment has been set up and the service has been started

- **Test Steps**

    1. On the client, send a POST request to the /v1/chat/completions API of the Unified Cache service. The request body template is as follows, and the model parameter needs to be changed to the actual model path:  
       
        ```bash
        curl --location 'http://127.0.0.1:8071/v1/chat/completions' \
        --header 'Content-Type: application/json' \
        --data '{
            "messages": [
                { "role": "user", "content": "你好" }
            ],
            "model": "DeepSeek-V3-128K",
            "max_tokens": 512,
            "stream": false,
            "temperature": 0.1,
            "top_p": 1.0,
            "best_of": 1,
            "n": 1
        }'
        ```

    2. Send the request and wait for the service to return the request result

- **Expected Results**
    
    In step 2, the request returns the result successfully, and the Unified Cache service runs properly without errors

- **Actual Results**
    
    ![img](./images/clip_image078.png)

- **Test Conclusion**
   
    Passed

- **Remarks**
    
    (None)

#### 3.2.2 Inference Performance Test

##### 3.2.2.2 Long Sequence Sparsification Scenario Test

- **Test Purpose**
   
    Verify the inference performance of the Unified Cache solution in the long sequence sparsification scenario

- **Test Network**
   
    Functional Verification Network Diagram

- **Prerequisites**
    
    1. The storage device has been installed and deployed and has been connected to the compute server through the NFS over RDMA protocol  
    2. The model files have been downloaded to the specified location  
    3. The Unified Cache environment has been set up, and the primary and secondary server services have been started  
    4. The UC-Eval test tool software has been installed on the compute server

- **Test Steps**
    
    1. Modify the pvc mount configuration  
      
        ![img](./images/clip_image080.png)

    2. Ensure that the Chunk Prefill feature and the GSA (sparsification) feature of the Unified Cache service are enabled  
      
        ![img](./images/clip_image082.png)

    3. Enable the UC-eval test software
    4. Refer to the README.md file and import the environment variables  
      
        ![img](./images/clip_image084.png)

    5. In the test script configuration, set the concurrency to 8-64, the number of input tokens to 32K, and the number of output tokens to 1K  
       
        ![img](./images/clip_image086.png)

    6. Set the test case to run only the current test case  
       
        ![img](./images/clip_image088.png)

    7. Run the UC-Eval test software and record the E2E latency (ms), TBT latency (ms), equivalent throughput TPS (Token/s), etc. of the test results
    8. Disable the Unified Cache service. After disabling features such as GSA and Chunk Prefill in the service configuration, restart the service and test the performance of the bare inference scenario  
      
        ![img](./images/clip_image090.png)

        Repeat steps 2-6 and compare the results with those obtained when UCM is enabled

- **Expected Results**
    
    In the long input sequence inference scenario, after the GSA feature is enabled, the TBT latency is significantly reduced and the throughput increases exponentially

- **Actual Results**
   
    1. Modify the input document length and concurrency according to the test scenario  
    2. When UCM is enabled, the UC-Eval test results are as follows:  
      
        [benchmark_static_latency.md](./attachments/image46__benchmark_static_latency.md)

        [benchmark_static_latency.csv](attachments/image46__benchmark_static_latency.csv)

        The recorded maximum concurrency is 32, with an incremental throughput of 292.7 tok/s  
        
        ![img](./images/clip_image094.png)

    3. The bare inference scenario test results are as follows:  
       
        [benchmark_static_latency_no_ucm.md](attachments/image48__benchmark_static_latency_no_ucm.md)

        [benchmark_static_latency_no_ucm.csv](attachments/image48__benchmark_static_latency_no_ucm.csv)

        The recorded maximum concurrency is 17, with an incremental throughput of 173.2 tok/s  
        
        ![img](./images/clip_image098.png)

- **Test Conclusion**

    Passed

- **Remarks**
    
    Long sequence sparsification selects tokens at key positions of the input sequence, limits the elements the model focuses on, reduces the attention computation scope, and lowers the computational complexity, thereby achieving a significant latency reduction and throughput improvement.

##### 3.2.2.3 Multi-turn Dialogue Scenario Test

- **Test Purpose**
    
    Verify the inference performance and effect of the Unified Cache solution in multi-turn dialogues

- **Test Network**
    
    Functional Verification Network Diagram

- **Prerequisites**
    
    1. The compute server has been connected through NFS over RDMA  
    2. The Unified Cache service has been started  
    3. The multi-turn dialogue simulation performance test tool has been installed on the compute server, and the simulated dialogue records have been uploaded (recommended: rounds ≤ 45, total tokens ≤ 32K)

- **Test Steps**

    1. Start the test environment  
       
        ```bash
        cd /home/UC-Eval-dev-zyc
        source uc-eval/bin/activate
        ```

    2. Refer to the README.md file, import the environment variables, and modify the model_url and model parameters  
      
        ![img](./images/clip_image100.png)

    3. Pre-embed the dialogue content  
      
        ```shell
        cd UC-Eval-datasets/qa/multi_turn_dialogues
        ```

        Modify multiturndialog.json  

        ![img](./images/clip_image102.png)

        Point to UC-Eval-datasets/qa/multi_turn_dialogues/kimi/kimi.json  

        ![img](./images/clip_image104.png)

    4. Modify the code so that only the multi-turn dialogue script is executed  
       
        ![img](./images/clip_image106.png)

    5. Modify the content of test_multi_turn_dialogue as needed

        ![img](./images/clip_image108.png)

    6. Calculate the TTFT/E2E/TBT latency according to the script return
    7. Enable the PrefixCache and RAGChunk features of Unified Cache  
       
        Set the dialogue rounds to 45 and run the test according to the dialogue records

    8. Calculate TTFT/E2E/TBT again and compare with step 1
    9. Plot the performance curve comparison chart

- **Expected Results (Example)**

    After the Prefix Cache feature is enabled, TTFT decreases significantly as the number of dialogue rounds increases.

- **Actual Results**

    [multi_turn_dialogue_latency.md](attachments/image55__multi_turn_dialogue_latency.md)

    [multi_turn_dialogue_latency.csv](attachments/image55__multi_turn_dialogue_latency.csv)

    ![img](./images/clip_image112.png)

- **Test Conclusion**

    Passed

- **Remarks**

    Prefix Cache can reuse the dialogue history prefix and significantly reduce the time to first token (TTFT).

## Appendix

### Definition and Calculation Method of Some Test Metrics

#### TTFT Latency

TTFT latency (ms), Time To First Token, refers to the time from when the user initiates a request to when the model returns the first token. This metric directly affects the user's perception of the model response speed.

#### TBT Latency

TBT latency (ms), Token Between Token, refers to the average incremental latency, that is, the average time between the generation of each token during large language model inference. This metric reflects the fluency of the tokens output by the model during generation.

#### E2E Latency

E2E latency (ms), End-to-End Delay, refers to the total time from when the user initiates a request to when the AI model returns the final result. This metric reflects the fluency of the tokens output by the model during generation.

E2E latency can be roughly estimated as the sum of TTFT + TBT*(number of generated tokens - 1) + data transmission time

#### Equivalent Throughput TPS

TPS (Token/s), Transactions Per Second, refers to the number of tokens generated per second during model inference. This metric measures the generation speed of the model. It can be calculated by dividing the total number of tokens generated by the model by the total time from input to completion of generation.
