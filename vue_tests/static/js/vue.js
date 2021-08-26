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
