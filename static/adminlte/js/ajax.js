/**
 * Created by lyhapple on 15/11/6.
 */

// todo: ajax部分方法待优化

(function ($) {
    var getCookie = function (name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };

    var csrftoken = getCookie('csrftoken');

    var csrfSafeMethod = function (method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    };

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var sendRequest = function(type, url, data, callback){
        $.ajax({
            type: type,
            url: url,
            data: data,
            dataType: 'json',
            statusCode: {
                403: function () {
                    window.location.href = Urls['adminlte:http403']();
                },
                400: function () {
                    alert('未找到资源');
                },
                500: function () {
                    alert('服务器错误');
                }
            },
            success: callback
        });
    };

    $.AdminLTE.getApiUrl = function(app, model){
        return '/api/v1/' + app + '/' + model;
    };

    $.AdminLTE.apiGet = function (url, data, callback) {
        sendRequest('GET', url, data, callback)
    };

    $.AdminLTE.apiPost = function (url, data, callback) {
        sendRequest('POST', url, data, callback)
    };

    $.AdminLTE.apiPatch = function (url, data, callback) {
        sendRequest('PATCH', url, data, callback);
    };

    $.AdminLTE.ajaxPost = function (url, data, callback) {
        $.ajax({
            type: 'POST',
            url: url,
            data: $.param(data),
            dataType: 'json',
            statusCode: {
                403: function () {
                    alert('无权限');
                },
                400: function () {
                    alert('未找到资源');
                },
                500: function () {
                    alert('服务器错误');
                }
            },
            success: callback
        });
    };
}(jQuery));