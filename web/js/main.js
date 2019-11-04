let app = new Vue({
    el: '#root',
    data: {
        start: false,
        loading_model: false,
        model: 'vector',
        directory: '',
        query: '',
        configured: false,
        files: [],
        result_size: 5,
    },
    methods: {
        load_model(model) {
            this.loading_model = true;

            this.model = model;

            this.loading_model = false;
        },
        config() {
            // Load model
            switch (this.model) {
                case 'vector':
                    eel.use_vector_model()();
                    break;
                case 'latent semantic':
                    eel.use_lsi_model()();
                    break;
                default:
                    break;
            }

            // Change directory; let back end handle validations
            eel.change_directory(this.directory)();

            // Allow queries
            this.configured = true;
        },
        run_query() {
            // Make the query if the retrieval model has been loaded
            if (this.configured) {
                files = eel.query(this.query);
            }
        },
        load_files() {
            eel.extract_text(this.directory)(read_files);
        }
        // load_vector_model: function() {
        //   this.loading_model = true;
        //   this.model = 'vector';
        //   // Vector Model call here


        //   this.loading_model = false;
        // },
        // load_latent_model() {
        //   this.loading_model = true;
        //   this.model = 'latent semantic';


        //   // Latent Semantic model here
        //   this.loading_model = false;
        // }
    }
})


function read_files(files) {
    console.log(files);
}