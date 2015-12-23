var CommonListPageVue = Vue.extend({
    el: function(){
        return '#commonDataTableRow';
    },
    data: function(){
        return {
            items: [],
            userName: $("#adminlte_page_user_name").val(),
            appName: $("#adminlte_page_app_name").val(),
            modelName: $("#adminlte_page_model_name").val(),
            currentPage: 1,
            totalPage: 1,
            perPage: 10,
            count: 0
        }
    },
    methods: {
        toggleAllBox: function (event) {
            $("input[name='checkboxRow']").prop(
                'checked',
                $(event.target).prop('checked')
            );
        },
        detail: function () {
            window.location.href = Urls['adminlte:common_detail_page'](
                this.appName,
                this.modelName,
                $(event.target).data('pk')
            );
        },
        create: function (event, modelName) {
            var name = this.modelName;
            if(modelName){
                name = modelName;
            }
            window.location.href = Urls['adminlte:common_create_page'](
                this.appName,
                name
            );
        },
        update: function (event) {
            window.location.href = Urls['adminlte:common_update_page'](
                this.appName,
                this.modelName,
                $(event.target).data('pk')
            );
        },
        remove: function (ids) {
            var self = this,
                delUrl = Urls['adminlte:common_delete_page'](
                    self.appName,
                    self.modelName
                );
            swal({
                title: "确定要删除吗?",
                text: "您确定要删除所选数据吗?",
                type: "warning",
                showCancelButton: true,
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "确定!",
                cancelButtonText: "取消",
                closeOnConfirm: false,
                showLoaderOnConfirm: true
            }, function () {
                $.AdminLTE.ajaxPost(
                    delUrl,
                    {'pk': ids.toString()},
                    function (resp) {
                        swal({
                            title: "删除成功!",
                            type: "success"
                        }, function () {
                            self.loadData({});
                        });
                    }
                );
            });
        },
        removeSelected: function () {
            var ids = [],
                box = $("input[name='checkboxRow']:checked");
            $.each(box, function (i, b) {
                ids.push($(b).val());
            });
            if (ids.length === 0) {
                swal({
                    title: "请选择数据!",
                    type: "warning"
                });
                return;
            }
            this.remove(ids);
        },
        removeOne: function (event) {
            this.remove($(event.target).data('pk'));
        },
        search: function (event) {
            this.loadData(
                $.param({'search': $("#tableSearch").val()})
            );
        },
        resetSearch: function (event) {
            $("#tableSearch").val('');
            this.search(event);
        },
        page: function (event) {
            var num = $(event.target).attr('page');
            this.loadData({'page': num});
        },
        loadData: function (data) {
            var self = this,
                url = $.AdminLTE.getApiUrl(self.appName, self.modelName);
            if(arguments.length === 2){
                url = arguments[1];
            }
            $.AdminLTE.apiGet(
                url,
                data,
                function (resp) {
                    self.items = resp.results;
                    self.count = resp.count;
                    self.perPage = resp.per_page;
                    self.totalPage = resp.total_page;
                    self.currentPage = resp.current_page;
                }
            );
        }
    }
});