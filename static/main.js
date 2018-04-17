window.onload = function () {
    new Vue({
        el: '#song',
        data: {
            items: []
        },
        created: function () {
            const vm = this;
            axios.get('/songs')
                .then(function (response) {
                    console.log(response.data);
                    vm.items = response.data
                })
        }
    })
};