# 网关 API 策略

DCE 5.0 云原生网关支持支持负载均衡、超时重试、黑白名单等十几项 API 策略。本文借助真实的微服务应用演示如何配置各项策略以及每项策略的具体效果。

!!! note

    - 有关各项策略的配置步骤、参数说明等细节，可参考[配置 API 策略](../gateway/api/api-policy.md)。
    - 本文侧重于展示各项策略的使用效果，会省略一些配置步骤。

## 前提条件

- 准备一个演示服务，例如 `my-otel-demo-adservice`
- 创建[网关](../gateway/index.md)、[域名](../gateway/domain/index.md)、[API](../gateway/api/index.md)
- 将演示[服务接入网关](gateway01.md)

## 负载均衡

1. 将演示服务扩展为多副本，便于演示负载均衡
2. 参考[负载均衡](../gateway/api/api-policy.md#_2)配置负载均衡策略
3. 编写脚本记录各个服务副本接收到的流量

    ??? note "点击查看脚本内容"

        ```python
        import requests
        
        def lb_pod_count():
            pod1_ip = "10.244.1.135" # 服务副本所在节点的 IP
            pod2_ip = "10.244.2.207" # 服务副本所在节点的 IP
            pod3_ip = "10.244.3.193" # 服务副本所在节点的 IP
            pod1_count = 0
            pod2_count = 0
            pod3_count =0
        
            host = "http://10.6.222.24:30040/ip" # 服务访问地址
            headers = {"Host": "ad.service.virtualhost"}
            for i in range(300):
                res_ip = requests.get(host, headers=headers).text[11:]
                if res_ip == pod1_ip:
                    pod1_count += 1
                elif res_ip == pod2_ip:
                    pod2_count += 1
                elif res_ip == pod3_ip:
                    pod3_count += 1
        
            print("指向%s的流量为：%d" %(pod1_ip,pod1_count))
            print("指向%s的流量为：%d" %(pod2_ip,pod2_count))
            print("指向%s的流量为：%d" %(pod3_ip,pod3_count))
        
        if __name__ == '__main__':
            lb_pod_count() 
        ```       

4. 随机负载均衡的效果如下。每个副本随机接受流量，导致个别副本压力过大。

    ![random](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw11.png)

5. 轮询负载均衡的效果如下。每个副本轮流接受流量，因此各个副本处理的流量总数基本相同。

    ![random](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw12.png)

## 路径改写

1. 初始状态下，访问的是服务根路径，返回内容如图。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw09.png)

2. 配置路径改写策略，原先访问服务根路径，改为访问 `/test2` 接口。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw13.png)

3. 效果如图。从返回内容可以看出，现在访问的接口已经改变了，返回的数据也变了。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw14.png)

## 超时配置

1. 启用超时配置，设置响应超过 3 秒时判断访问失败。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw15.png)

2. 通过测试专用接口 `timeout` 让请求响应 1 秒，预期可以成功访问。

    下图说明访问成功，接口返回了所设置的请求时间

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw16.png)

3. 通过测试专用接口 `timeout` 让请求响应 4 秒，预期会访问失败

    下图说明访问失败，接口返回上游请求超时的信息。
    
    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw17.png)

## 重试机制

1. 启用重试配置，访问失败时最多重试 6 次，重试响应时间超过 1 秒时视为重试失败。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw18.png)

2. 通过测试专用接口 `set-retry-count` 使得服务的 `/retry` 接口必须请求 3 次才能访问成功。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw19.png)

    访问 `retry` 接口。

    在重试次数为 6 的情况下，预期可以访问成功。
    
    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw20.png)

3. 通过测试专用接口 `set-retry-count` 使得服务的 `/retry` 接口必须请求 7 次才能访问成功。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw21.png)

    访问 `retry` 接口。

    在重试次数为 6 的情况下，预期也能访问成功。因为首次正常访问加失败后的 6 次重试，正好达到了所需的 7 次访问。
    
    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw22.png)

4. 通过测试专用接口 `set-retry-count` 使得服务的 `/retry` 接口必须请求 8 次才能访问成功。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw23.png)

    访问 `retry` 接口。

    在重试次数为 6 的情况下，预期第一次会访问失败。因为首次正常访问加失败后的 6 次重试，最多只能访问 7 次，达不到所需的 8 次访问。
    
    但此时手动再次访问该接口，就会显示访问成功，因此此时累计的访问次数已经达到了 8 次。
    
    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw24.png)

## 请求头重写

1. 启用请求头重写策略，在请求服务时移除 `user-agent` （不区分大小写，并添加 `demo-req`。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw25.png)

2. 使用 postman 工具查看服务初始状态下带有的请求头。可以看到存在 `user-agent`，但没有 `demo-req`。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw28.png)

3. 通过测试专用接口 `/request-header` 查看请求服务时是否带上了 `user-agent`。

    返回 `user-agent` 的值为 null，说明该请求头被移除了，重写策略生效。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw26.png)

4. 通过测试专用接口 `/request-header` 查看请求服务时是否带上了 `user-agent`。

    返回了预先设置的值，说明添加了该请求头，重写策略生效。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw27.png)

## 响应头重写

1. 启用响应头重写策略，在服务响应头中移除 `x-envoy-upstream-service-time` （不区分大小写）响应头，并添加 `demo-res`。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw29.png)

2. 使用 postman 工具查看初始状态下的响应头。可以看到存在 `x-envoy-upstream-service-time`，但没有 `demo-res`。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw30.png)

3. 直接访问该服务

    响应头中没有 `x-envoy-upstream-service-time`，但出现了 `demo-res` ，说明重写策略生效。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw31.png)

## WebSocket

1. 编写测试 WebSocket 的脚本

    ??? note "点击查看脚本内容"

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

2. 在上述脚本保存为 html 文件，双击打开该文件。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw32.png)

3. 在未开启 WebSocket 策略，点击`连接`，会显示访问失败。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw33.png)

4. 开启 WebSocket 策略。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw35.png)

5. 再次点击`连接`，显示访问成功，说明 WebSocket 策略生效。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw34.png)

## 本地限流

1. 启用本地限流策略。

    下图设置的含义是：每分钟只能正常请求 3 次，但允许溢出访问 2 次，所以每分钟累计允许访问 5 次。
    超过 5 次的访问会返回 `429` 代码，并附上 `ratelimit=done` 和 `ratelimit1= done1` 的响应头。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw36.png)

2. 通过 curl 命令访问服务。

    可以看到第六次访问时返回了 `local_rate_limit` 信息，表示由于限流而访问失败。

    并且返回内容也出现了 429 代码以及新增的两个响应头

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw37.png)

## 健康检查

1. 启用健康检查策略。

    在没有设置路径改写的情况下，正常访问的是服务的根路径 `/`。但如果将检查路径设置为 `/test`，预期会健康检查失败，导致服务无法访问。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw38.png)
   
    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw39.png)

2. 修改为正确的检查路径。预期会通过健康检查，服务可以正常访问。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw40.png)
   
    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw41.png)

## Cookie 重写

1. 启用 Cookie 重写策略。

    重写时需要确保 cookie 名称与已有 cookie 的名称相同，才能确保原先的属性被新设置的属性覆盖。

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw42.png)

2. 使用测试专用接口 `/cookie-set` 设置请求时的 cookie 属性，并在响应头中携带实际生效的 cookie 属性。

    网关请求时设置的 cookie 为
    `Cookie{name='cookie-name', value='cookie-value', maxAge=PT-1S, domain='test.domain', path='/path', secure=false, httpOnly=false, sameSite='Lax'}`

    而在响应头中 set-cookie 展示了实际生效的 cookie：
    `cookie-name=cookie-value; Secure; Domain=rewrite.domain; SameSite=Strict; Path=/rewrite/path`

    ![rewrite](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw43.png)
