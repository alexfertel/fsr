let app = new Vue({
    el: '#root',
    data: {
        start: false,
        loading: false,
        model: 'vector',
        directory: '/home/alex/code/fsr/src/corpus/others',
        query: '',
        configured: false,
        files: [],
        displayed_files: [],
        result_size: 5,
    },
    methods: {
        load_model(model) {
            this.loading = true;

            eel.use_model(model)(() => {
                this.model = model;
                this.loading = false;
            });
        },
        config() {

            // Change directory; let back end handle validations
            eel.change_directory(this.directory)();

            // Allow queries
            this.configured = true;
        },
        run_query() {
            this.loading = true;

            // Make the query if the retrieval model has been loaded
            eel.query(this.query)(files => {
                this.files = files;
                this.displayed_files = files.slice(0, this.relevant_size)
                this.loading = false;
                // console.log(files);
            });
        },
        load_files() {
            eel.extract_text(this.directory)(read_files);
        }
        // load_vector_model: function() {
        //   this.loading = true;
        //   this.model = 'vector';
        //   // Vector Model call here


        //   this.loading = false;
        // },
        // load_latent_model() {
        //   this.loading = true;
        //   this.model = 'latent semantic';


        //   // Latent Semantic model here
        //   this.loading = false;
        // }
    }
})


function read_files(files) {
    console.log(files);
}