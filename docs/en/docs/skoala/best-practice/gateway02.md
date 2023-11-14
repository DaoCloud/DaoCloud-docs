# Gateway API Policies

DCE 5.0 cloud-native gateway supports several API policies, including load balancing, timeout, retries, and blacklisting/whitelisting. This article demonstrates how to configure these policies and their specific effects using a real microservice application.

!!! note

    - For detailed configuration steps and parameter explanations for each policy, refer to [API Policy Configuration](../gateway/api/api-policy.md).
    - This article focuses on showcasing the effects of each policy and may omit some configuration steps.

## Prerequisites

- Prepare a demo service, such as `my-otel-demo-adservice`.
- Create a [gateway](../gateway/index.md), [domain](../gateway/domain/index.md), and [API](../gateway/api/index.md).
- Connect the demo service to the gateway as explained in [Connecting Services to the Gateway](gateway01.md).

## Load Balancing

1. Scale the demo service to multiple replicas for load balancing demonstration.
2. Configure the load balancing policy following the instructions in [Load Balancing](../gateway/api/api-policy.md#_2).
3. Write a script to record the traffic received by each service replica.

    ??? note "Click to view the script content"

        ```python
        import requests
        
        def lb_pod_count():
            pod1_ip = "10.244.1.135" # IP address of the service replica's node
            pod2_ip = "10.244.2.207" # IP address of the service replica's node
            pod3_ip = "10.244.3.193" # IP address of the service replica's node
            pod1_count = 0
            pod2_count = 0
            pod3_count =0
        
            host = "http://10.6.222.24:30040/ip" # Service access address
            headers = {"Host": "ad.service.virtualhost"}
            for i in range(300):
                res_ip = requests.get(host, headers=headers).text[11:]
                if res_ip == pod1_ip:
                    pod1_count += 1
                elif res_ip == pod2_ip:
                    pod2_count += 1
                elif res_ip == pod3_ip:
                    pod3_count += 1
        
            print("Traffic directed to %s: %d" %(pod1_ip,pod1_count))
            print("Traffic directed to %s: %d" %(pod2_ip,pod2_count))
            print("Traffic directed to %s: %d" %(pod3_ip,pod3_count))
        
        if __name__ == '__main__':
            lb_pod_count() 
        ```       

4. The effect of random load balancing is as follows. Each replica receives traffic randomly, resulting in some replicas being under more load.

    ![random](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw11.png)

5. The effect of round-robin load balancing is as follows. Each replica receives traffic in a round-robin fashion, resulting in a similar total traffic load for each replica.

    ![random](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw12.png)

## Path Rewriting

1. In the initial state, accessing the root path of the service returns the content as shown in the image.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw09.png)

2. Configure the path rewriting policy to change the access from the root path to the `/test2` endpoint.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw13.png)

3. The effect is shown in the image. From the returned content, it can be seen that the accessed endpoint has changed, and the returned data has also changed.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw14.png)

## Timeout Configuration

1. Enable the timeout configuration and set it to consider the request as failed if the response exceeds 3 seconds.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw15.png)

2. Use the dedicated test endpoint `/timeout` to make the request respond within 1 second. The expectation is that the request will succeed.

    The image below shows a successful access, and the interface returns the set request time.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw16.png)

3. Use the dedicated test endpoint `/timeout` to make the request respond within 4 seconds. The expectation is that the request will fail.

    The image below shows a failed access, and the interface returns an upstream request timeout message.
    
    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw17.png)

## Retry Mechanism

1. Enable the retry configuration with a maximum of 6 retries when the request fails, and consider it a retry failure if the retry response time exceeds 1 second.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw18.png)

2. Use the dedicated test endpoint `/set-retry-count` to make the `/retry` endpoint of the service require 3 requests to succeed.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw19.png)

    Access the `retry` endpoint.

    With 6 retries, it is expected to succeed.
    
    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw20.png)

3. Use the dedicated test endpoint `/set-retry-count` to make the `/retry` endpoint of the service require 7 requests to succeed.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw21.png)

    Access the `retry` endpoint.

    With 6 retries, it is expected to succeed as well. Because the initial successful request plus the 6 retries after failure adds up to the required 7 requests.
    
    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw22.png)

4. Use the dedicated test endpoint `/set-retry-count` to make the `/retry` endpoint of the service require 8 requests to succeed.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw23.png)

    Access the `retry` endpoint.

    With 6 retries, the first attempt is expected to fail. Because the initial successful request plus the 6 retries after failure can only reach a maximum of 7 requests, which is not enough for the required 8 requests.
    
    However, manually accessing the endpoint again will show a successful access. At this point, the accumulated number of accesses has reached 8.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw24.png)

## Request Header Rewriting

1. Enable the request header rewriting policy to remove the `user-agent` (case-insensitive) header and add `demo-req` when making requests to the service.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw25.png)

2. Use Postman tool to view the request headers present in the initial state. It can be seen that `user-agent` exists, but `demo-req` is not present.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw28.png)

3. Use the dedicated test endpoint `/request-header` to check if the request includes the `user-agent` header.

    The returned value of `user-agent` is null, indicating that the header has been removed and the rewriting policy is effective.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw26.png)

4. Use the dedicated test endpoint `/request-header` to check if the request includes the `user-agent` header.

    The expected value is returned, indicating that the header has been added and the rewriting policy is effective.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw27.png)

## Response Header Rewriting

1. Enable the response header rewriting policy to remove the `x-envoy-upstream-service-time` (case-insensitive) response header and add `demo-res`.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw29.png)

2. Use Postman tool to view the response headers in the initial state. It can be seen that `x-envoy-upstream-service-time` exists, but `demo-res` is not present.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw30.png)

3. Access the service directly.

    The response headers do not include `x-envoy-upstream-service-time`, but `demo-res` is present, indicating that the rewriting policy is effective.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw31.png)

## WebSocket

1. Write a script to test WebSocket connections.

    ??? note "Click to view the script"

        ```html
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>本地websocket测试</title>
                <meta name="robots" content="all" />
                <meta name="keywords" content="本地,websocket,测试工具" />
                <meta name="description" content="本地,websocket,测试工具" />
                <style>
                    .btn-group{
                        display: inline-block;
                    }
                </style>
            </head>
            <body>
                <input type='text' value='通信地址, ws://开头..' class="form-control" style='width:390px;display:inline'
                id='wsaddr' />
                <div class="btn-group" >
                    <button type="button" class="btn btn-default" onclick='addsocket();'>连接</button>
                    <button type="button" class="btn btn-default" onclick='closesocket();'>断开</button>
                    <button type="button" class="btn btn-default" onclick='$("#wsaddr").val("")'>清空</button>
                </div>
                <div class="row">
                    <div id="output" style="border:1px solid #ccc;height:365px;overflow: auto;margin: 20px 0;"></div>
                    <input type="text" id='message' class="form-control" style='width:810px' placeholder="待发信息" onkeydown="en(event);">
                    <span class="input-group-btn">
                        <button class="btn btn-default" type="button" onclick="doSend();">发送</button>
                    </span>
                    </div>
                </div>
            </body>      
                
                <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
                <script language="javascript" type="text/javascript">
                    function formatDate(now) {
                        var year = now.getFullYear();
                        var month = now.getMonth() + 1;
                        var date = now.getDate();
                        var hour = now.getHours();
                        var minute = now.getMinutes();
                        var second = now.getSeconds();
                        return year + "-" + (month = month < 10 ? ("0" + month) : month) + "-" + (date = date < 10 ? ("0" + date) : date) +
                            " " + (hour = hour < 10 ? ("0" + hour) : hour) + ":" + (minute = minute < 10 ? ("0" + minute) : minute) + ":" + (
                                second = second < 10 ? ("0" + second) : second);
                    }
                    var output;
                    var websocket;
          
                    function init() {
                        output = document.getElementById("output");
                        testWebSocket();
                    }
          
                    function addsocket() {
                        var wsaddr = $("#wsaddr").val();
                        if (wsaddr == '') {
                            alert("请填写websocket的地址");
                            return false;
                        }
                        StartWebSocket(wsaddr);
                    }
          
                    function closesocket() {
                        websocket.close();
                    }
          
                    function StartWebSocket(wsUri) {
                        websocket = new WebSocket(wsUri);
                        websocket.binaryType = "arraybuffer";
                        websocket.onopen = function(evt) {
                            onOpen(evt)
                        };
                        websocket.onclose = function(evt) {
                            onClose(evt)
                        };
                        websocket.onmessage = function(evt) {
                            onMessage(evt)
                        };
                        websocket.onerror = function(evt) {
                            onError(evt)
                        };
                    }
          
                    function onOpen(evt) {
                        writeToScreen("<span style='color:red'>连接成功，现在你可以发送信息啦！！！</span>");
                    }
          
                    function onClose(evt) {
                        writeToScreen("<span style='color:red'>websocket连接已断开!!!</span>");
                        websocket.close();
                    }
          
                    function onMessage(evt) {
                        writeToScreen('<span style="color:blue">服务端回应 ' + formatDate(new Date()) + '</span><br/><span class="bubble">' +
                            evt.data + '</span>');
                    }
          
                    function onError(evt) {
                        writeToScreen('<span style="color: red;">发生错误:</span> ' + evt.data);
                    }
          
                    function doSend() {
                        var message = $("#message").val();
                        if (message == '') {
                            alert("请先填写发送信息");
                            $("#message").focus();
                            return false;
                        }
                        if (typeof websocket === "undefined") {
                            alert("websocket还没有连接，或者连接失败，请检测");
                            return false;
                        }
                        if (websocket.readyState == 3) {
                            alert("websocket已经关闭，请重新连接");
                            return false;
                        }
                        console.log(websocket);
                        $("#message").val('');
                        writeToScreen('<span style="color:green">你发送的信息 ' + formatDate(new Date()) + '</span><br/>' + message);
                        websocket.send(message);
                    }
          
                    function writeToScreen(message) {
                        var div = "<div class='newmessage'>" + message + "</div>";
                        var d = $("#output");
                        var d = d[0];
                        var doScroll = d.scrollTop == d.scrollHeight - d.clientHeight;
                        $("#output").append(div);
                        if (doScroll) {
                            d.scrollTop = d.scrollHeight - d.clientHeight;
                        }
                    }
          
          
                    function en(event) {
                        var evt = evt ? evt : (window.event ? window.event : null);
                        if (evt.keyCode == 13) {
                            doSend()
                        }
                    }
                </script>
        </html>
        ```

2. Save the above script as an HTML file and double-click to open it.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw32.png)

3. Without enabling the WebSocket policy, click on `Connect`, and it will display an access failure.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw33.png)

4. Enable the WebSocket policy.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw35.png)

5. Click on `Connect` again, and it will display a successful connection, indicating that the WebSocket policy is effective.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw34.png)

## Local Rate Limiting

1. Enable the local rate limiting policy.

    The settings in the image below mean that only 3 normal requests are allowed per minute, but 2 overflow requests are allowed. So, a total of 5 requests are allowed per minute.
    If the number of requests exceeds 5, it will return a `429` status code with the `ratelimit=done` and `ratelimit1=done1` response headers.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw36.png)

2. Access the service using the curl command.

    It can be seen that on the sixth access, it returns the `local_rate_limit` information, indicating that the access failed due to rate limiting.

    Additionally, the response includes the 429 status code and the two newly added response headers.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw37.png)

## Health Checks

1. Enable the health check policy.

    Without setting a path rewrite, the normal access is to the root path `/` of the service. However, if the check path is set to `/test`, the health check is expected to fail, resulting in the service being inaccessible.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw38.png)
   
    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw39.png)

2. Modify to the correct check path. It is expected to pass the health check, and the service can be accessed normally.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw40.png)
   
    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw41.png)

## Cookie Rewriting

1. Enable the cookie rewriting policy.

    When rewriting, make sure that the cookie name matches the existing cookie name so that the original attributes can be overridden by the newly set attributes.

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw42.png)

2. Use the test-specific endpoint `/cookie-set` to set the cookie attributes in the request and carry the actual effective cookie attributes in the response headers.

    The cookie set by the gateway request is:
    `Cookie{name='cookie-name', value='cookie-value', maxAge=PT-1S, domain='test.domain', path='/path', secure=false, httpOnly=false, sameSite='Lax'}`

    The response headers show the actually effective cookie:
    `cookie-name=cookie-value; Secure; Domain=rewrite.domain; SameSite=Strict; Path=/rewrite/path`

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw43.png)
