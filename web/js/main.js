var app = new Vue({
    el: '#root',
    data: {
      loading_model: false,
      model: 'vector',
      directory: '',
      configured: false
    },
    methods: {
      load_model (model){
        this.loading_model = true;
        this.model = model;

        this.loading_model = false;
      },
      config (){
        // Validate directory

        // Load model

        // Allow queries
        this.configured = true;
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