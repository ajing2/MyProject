/**
 * Created by lingjing on 2018/6/19.
 */



function get_param_appinstall() {
    var param = {
        "ip": $("#ipList").val(),
        "app": $("#appName").val(),
        "tool": $("#tool input:radio:checked").val(),
    };
    return param
}



function get_ip_list() {
    var url = "http://127.0.0.1:8000/salt/iplist/"
    var data;
    $.ajax({
        type: "GET",
        timeout: 10000, // 超时时间 10 秒
        url: url,
        dataType: 'json',
        // data: data,
        contentType: 'application/json',
        success: function (callback) {
            if (callback.message == 'success') {
                // data = JSON.parse(callback.data);
                data = callback.data;
                for(var i=0; i<data.length; i++){
                    $("#ipList").append("<option value='" + data[i]["fields"]["ip"] + "'>" + data[i]["fields"]["ip"] + "</option>");
                }
                //缺一不可
                $('.selectpicker').selectpicker('refresh');
                $('.selectpicker').selectpicker('render');
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            debugger;
            console.log(err);
        },
        // complete: function(XMLHttpRequest, status) { //请求完成后最终执行参数　
        // }
    })

}



$(window).on('load', function () {
    get_ip_list();
});