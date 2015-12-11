/**
 * messageset app js
 * 右上角消息通知js
 */
var messagesetVue = new Vue({
    el: '#messagesetVue',
    data: {
        sitemail: [],
        notification: [],
        task: [],
        appName: 'messageset'
    },
    ready: function(){
        var data = {'status': 0};
        this.loadData('sitemail', {"status": 0, 'receiver': true});
        this.loadData('notification', data);
        this.loadData('task', data);
    },
    methods: {
        detail: function(model, event){
            var self = this;
            window.location.href = Urls['adminlte:common_detail_page'](
                self.appName,
                model,
                $(event.target).data('pk')
            );
        },
        sitemailDetail: function(event){
            this.detail('sitemail', event);
        },
        taskDetail: function(event){
            this.detail('task', event);
        },
        notificationDetail: function (event) {
            this.detail('notification', event);
        },
        loadData: function(modelName, data){
            var self = this,
                url = $.AdminLTE.getApiUrl(self.appName, modelName);
            $.AdminLTE.apiGet(
                url, data,
                function(resp){
                    self[modelName] = resp.results;
                }
            );
        }
    }
});