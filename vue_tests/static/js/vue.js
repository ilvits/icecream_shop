const app = Vue.createApp({
    el: '#app',
    delimiters: ['[[', ']]'],
    data() {
        return {
            returned_task: '',
            new_task: '',
            create_modify: '',
            modify_id: -1,
            modify_index: -1,
            tasks: []
        }
    },
    created() {
        this.tasks = ['do this 🐱‍🐉', 'and that 🤳'];
    },
});

app.mount('#app')

new Vue({
    delimiters: ['${', '}$'],
    el: '#app',
    data: {
        products: []

    },
    http: {
        root: 'http://localhost:8000',
        headers: {
            Authorization: '<TOKEN_HERE>'
        }
    },
    methods: {
        getProducts: function () {
            this.$http.get('products/').then(function (data,status,request) {
                if (status == 200) {
                    this.products = data.body.results;
                }
            })
        }
    },
    mounted: function () {
        this.getProducts();
    }
})