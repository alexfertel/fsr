var app = new Vue({
    el: '#root',
    data: {
      active: '0'
    },
    methods: {
      load_vector_model: function() {
        // Vector Model call here
        console.log("aaaa");
        this.active = '1';
      },
      load_latent_model() {
        // Latent Semantic model here
        this.active = '1';
      }
    }
  })