var vm = new Vue({
    el: '#app',
    data: {
        projects: []
    },
    ready: function () {
        this.$http.get('/projects').then(function (response) {
            this.projects = response.data
        })
    }
});