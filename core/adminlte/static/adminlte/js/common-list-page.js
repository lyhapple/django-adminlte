var commonListPageVue = new CommonListPageVue({
    ready: function () {
        if (this.appName && this.modelName) {
            this.loadData({});
        }
    }
});