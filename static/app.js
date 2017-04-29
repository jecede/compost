var vm = new Vue({
    el: '#wrapper',
    data: {
        projects: []
    },
    ready: function () {
        this.$http.get('/projects').then(function (response) {
            this.projects = response.data
        })
    }
});